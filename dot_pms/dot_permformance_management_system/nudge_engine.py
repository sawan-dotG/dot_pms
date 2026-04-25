import frappe
from frappe.utils import getdate, add_days

def send_nudge():
    # Find active employees who haven't had a 1-on-1 in the last 14 days
    fourteen_days_ago = add_days(getdate(), -14)
    
    # Mock query: In a real system, you'd check standard Employee doctype
    if not frappe.db.exists("DocType", "Employee"):
        return
        
    employees = frappe.get_all("Employee", filters={"status": "Active"}, fields=["name", "user_id", "reports_to"])
    
    for emp in employees:
        if not emp.user_id or not emp.reports_to:
            continue
            
        recent_1on1s = frappe.get_all("PMS 1-on-1", filters={
            "employee": emp.user_id,
            "date": [">=", fourteen_days_ago]
        })
        
        if not recent_1on1s:
            # Create a Continuous Feedback Nudge as a mock for Slack integration
            nudge = frappe.new_doc("PMS Feedback")
            nudge.from_user = emp.reports_to
            nudge.to_user = emp.user_id
            nudge.date = getdate()
            nudge.feedback_type = "Nudge"
            nudge.content = "It's been over 14 days since your last 1-on-1. Time to catch up!"
            nudge.insert(ignore_permissions=True)
            
            # Here you would typically use requests to post to a Slack webhook url
            # e.g., requests.post(slack_webhook_url, json={"text": nudge.content})
            frappe.logger().info(f"Nudge sent to {emp.user_id}")
