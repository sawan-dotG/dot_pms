import frappe
from frappe.model.document import Document

class PMSAppraisalCycle(Document):
	def on_update(self):
		if self.status == "Active":
			self.create_appraisals()

	def create_appraisals(self):
		# Check if appraisals already exist for this cycle
		existing = frappe.get_all("PMS Appraisal", filters={"cycle": self.name}, limit=1)
		if existing:
			return # Already generated

		if frappe.db.exists("DocType", "Employee"):
			# Check schema to see what the 'employee' field expects
			meta = frappe.get_meta("PMS Appraisal")
			employee_link_doctype = meta.get_field("employee").options if meta.get_field("employee") else "User"
			manager_link_doctype = meta.get_field("manager").options if meta.get_field("manager") else "User"

			employees = frappe.get_all("Employee", filters={"status": "Active"}, fields=["name", "user_id", "reports_to"])
			
			count = 0
			for emp in employees:
				doc = frappe.new_doc("PMS Appraisal")
				doc.cycle = self.name
				
				# Handle Employee vs User link for the 'employee' field
				if employee_link_doctype == "Employee":
					doc.employee = emp.name
				else:
					if not emp.user_id: continue
					doc.employee = emp.user_id
					
				# Handle Employee vs User link for the 'manager' field
				if emp.reports_to:
					if manager_link_doctype == "Employee":
						if frappe.db.exists("Employee", emp.reports_to):
							doc.manager = emp.reports_to
					else:
						# Need to find the user_id of the manager
						manager_user_id = frappe.db.get_value("Employee", emp.reports_to, "user_id")
						if manager_user_id and frappe.db.exists("User", manager_user_id):
							doc.manager = manager_user_id

				# Only set manager if it's required and we couldn't find one, to avoid reqd errors,
				# fallback to administrator just to avoid failing the whole cycle.
				if not doc.manager and meta.get_field("manager").reqd:
					doc.manager = frappe.session.user
					
				doc.status = "Draft"
				try:
					doc.insert(ignore_permissions=True)
					count += 1
				except frappe.exceptions.LinkValidationError as e:
					frappe.log_error(title="Appraisal Creation Error", message=f"Failed for {emp.name}: {str(e)}")
					continue
				
			frappe.msgprint(f"Generated {count} Appraisals for cycle {self.cycle_name}")
