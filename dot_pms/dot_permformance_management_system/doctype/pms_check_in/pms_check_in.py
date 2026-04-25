import frappe
from frappe.model.document import Document

class PMSCheckin(Document):
	def on_submit(self):
		self.update_key_result()
		self.update_objective()

	def update_key_result(self):
		kr = frappe.get_doc("PMS Key Result", self.key_result)
		kr.current_value = self.new_value
		if kr.target_value:
			kr.progress = (kr.current_value / kr.target_value) * 100
		else:
			kr.progress = 0
		kr.save()

	def update_objective(self):
		kr = frappe.get_doc("PMS Key Result", self.key_result)
		if kr.objective:
			obj = frappe.get_doc("PMS Objective", kr.objective)
			# Calculate average progress of all KRs for this objective
			krs = frappe.get_all("PMS Key Result", filters={"objective": obj.name}, fields=["progress"])
			if krs:
				total_progress = sum(k.progress for k in krs)
				obj.progress = total_progress / len(krs)
				obj.save()
