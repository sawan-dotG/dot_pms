import frappe

def create_doctype(name, module, fields, is_submittable=0, is_child_table=0):
    if not frappe.db.exists("DocType", name):
        doc_data = {
            "doctype": "DocType",
            "name": name,
            "module": module,
            "custom": 0,
            "autoname": f"format:{{{{name}}}}-{{{{####}}}}",
            "is_submittable": is_submittable,
            "istable": 1 if is_child_table else 0,
            "fields": fields,
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1
                }
            ]
        }
        
        if is_child_table:
            doc_data["autoname"] = "autoincrement"
            doc_data["permissions"] = []
            
        doc = frappe.get_doc(doc_data)
        doc.insert(ignore_permissions=True)
        print(f"Created DocType: {name}")
    else:
        print(f"DocType already exists: {name}")

def execute():
    print("Creating dot_pms DocTypes...")
    
    # 1. OKR Module
    create_doctype("PMS Objective", "dot Permformance Management System", [
        {"fieldname": "title", "fieldtype": "Data", "label": "Title", "reqd": 1, "in_list_view": 1},
        {"fieldname": "owner", "fieldtype": "Link", "options": "User", "label": "Owner", "reqd": 1, "in_list_view": 1},
        {"fieldname": "parent_objective", "fieldtype": "Link", "options": "PMS Objective", "label": "Parent Objective"},
        {"fieldname": "status", "fieldtype": "Select", "options": "Draft\nActive\nCompleted\nArchived", "label": "Status", "default": "Draft", "in_list_view": 1},
        {"fieldname": "visibility", "fieldtype": "Select", "options": "Public\nPrivate", "label": "Visibility", "default": "Public"},
        {"fieldname": "progress", "fieldtype": "Percent", "label": "Progress", "read_only": 1, "default": 0, "in_list_view": 1}
    ])
    
    create_doctype("PMS Key Result", "dot Permformance Management System", [
        {"fieldname": "objective", "fieldtype": "Link", "options": "PMS Objective", "label": "Objective", "reqd": 1, "in_list_view": 1},
        {"fieldname": "title", "fieldtype": "Data", "label": "Title", "reqd": 1, "in_list_view": 1},
        {"fieldname": "target_value", "fieldtype": "Float", "label": "Target Value", "reqd": 1},
        {"fieldname": "current_value", "fieldtype": "Float", "label": "Current Value", "default": 0},
        {"fieldname": "progress", "fieldtype": "Percent", "label": "Progress", "read_only": 1, "default": 0, "in_list_view": 1},
        {"fieldname": "update_frequency", "fieldtype": "Select", "options": "Weekly\nBi-Weekly\nMonthly", "label": "Update Frequency", "default": "Weekly"}
    ])

    create_doctype("PMS Check-in", "dot Permformance Management System", [
        {"fieldname": "key_result", "fieldtype": "Link", "options": "PMS Key Result", "label": "Key Result", "reqd": 1, "in_list_view": 1},
        {"fieldname": "new_value", "fieldtype": "Float", "label": "New Value", "reqd": 1, "in_list_view": 1},
        {"fieldname": "date", "fieldtype": "Date", "label": "Date", "reqd": 1, "in_list_view": 1},
        {"fieldname": "notes", "fieldtype": "Small Text", "label": "Notes"}
    ], is_submittable=1)

    # 2. Continuous Feedback Module
    create_doctype("PMS Feedback", "dot Permformance Management System", [
        {"fieldname": "from_user", "fieldtype": "Link", "options": "User", "label": "From", "reqd": 1, "in_list_view": 1},
        {"fieldname": "to_user", "fieldtype": "Link", "options": "User", "label": "To", "reqd": 1, "in_list_view": 1},
        {"fieldname": "date", "fieldtype": "Date", "label": "Date", "reqd": 1, "in_list_view": 1},
        {"fieldname": "feedback_type", "fieldtype": "Select", "options": "Shout-out\nConstructive\nNudge", "label": "Type", "reqd": 1, "in_list_view": 1},
        {"fieldname": "sentiment", "fieldtype": "Select", "options": "Positive\nNeutral\nConstructive", "label": "Sentiment (AI)", "read_only": 1},
        {"fieldname": "content", "fieldtype": "Text", "label": "Content", "reqd": 1}
    ])
    
    create_doctype("PMS 1-on-1 Agenda", "dot Permformance Management System", [
        {"fieldname": "topic", "fieldtype": "Data", "label": "Topic", "reqd": 1, "in_list_view": 1},
        {"fieldname": "discussed", "fieldtype": "Check", "label": "Discussed", "in_list_view": 1},
        {"fieldname": "action_item", "fieldtype": "Data", "label": "Action Item", "in_list_view": 1},
        {"fieldname": "carried_over", "fieldtype": "Check", "label": "Carried Over"}
    ], is_child_table=1)

    create_doctype("PMS 1-on-1", "dot Permformance Management System", [
        {"fieldname": "manager", "fieldtype": "Link", "options": "User", "label": "Manager", "reqd": 1, "in_list_view": 1},
        {"fieldname": "employee", "fieldtype": "Link", "options": "User", "label": "Employee", "reqd": 1, "in_list_view": 1},
        {"fieldname": "date", "fieldtype": "Date", "label": "Date", "reqd": 1, "in_list_view": 1},
        {"fieldname": "status", "fieldtype": "Select", "options": "Scheduled\nCompleted\nCancelled", "label": "Status", "default": "Scheduled", "in_list_view": 1},
        {"fieldname": "agenda_items", "fieldtype": "Table", "options": "PMS 1-on-1 Agenda", "label": "Agenda Items"}
    ])

    # 3. Competency & Talent Module
    create_doctype("PMS Competency", "dot Permformance Management System", [
        {"fieldname": "competency_name", "fieldtype": "Data", "label": "Competency Name", "reqd": 1, "in_list_view": 1},
        {"fieldname": "category", "fieldtype": "Select", "options": "Technical\nSoft Skill\nLeadership", "label": "Category", "in_list_view": 1},
        {"fieldname": "description", "fieldtype": "Text", "label": "Description"}
    ])
    
    create_doctype("PMS Skill Gap Assessment", "dot Permformance Management System", [
        {"fieldname": "employee", "fieldtype": "Link", "options": "User", "label": "Employee", "reqd": 1, "in_list_view": 1},
        {"fieldname": "competency", "fieldtype": "Link", "options": "PMS Competency", "label": "Competency", "reqd": 1, "in_list_view": 1},
        {"fieldname": "current_level", "fieldtype": "Int", "label": "Current Level (1-5)", "reqd": 1},
        {"fieldname": "required_level", "fieldtype": "Int", "label": "Required Level (1-5)", "reqd": 1},
        {"fieldname": "gap", "fieldtype": "Int", "label": "Gap", "read_only": 1, "in_list_view": 1}
    ])

    # 4. Appraisal Module
    create_doctype("PMS Appraisal Cycle", "dot Permformance Management System", [
        {"fieldname": "cycle_name", "fieldtype": "Data", "label": "Cycle Name", "reqd": 1, "in_list_view": 1},
        {"fieldname": "start_date", "fieldtype": "Date", "label": "Start Date", "reqd": 1, "in_list_view": 1},
        {"fieldname": "end_date", "fieldtype": "Date", "label": "End Date", "reqd": 1, "in_list_view": 1},
        {"fieldname": "status", "fieldtype": "Select", "options": "Draft\nActive\nCompleted", "label": "Status", "default": "Draft", "in_list_view": 1}
    ])

    create_doctype("PMS Appraisal", "dot Permformance Management System", [
        {"fieldname": "employee", "fieldtype": "Link", "options": "User", "label": "Employee", "reqd": 1, "in_list_view": 1},
        {"fieldname": "cycle", "fieldtype": "Link", "options": "PMS Appraisal Cycle", "label": "Appraisal Cycle", "reqd": 1, "in_list_view": 1},
        {"fieldname": "manager", "fieldtype": "Link", "options": "User", "label": "Manager", "reqd": 1, "in_list_view": 1},
        {"fieldname": "performance_score", "fieldtype": "Float", "label": "Performance Score (X-axis)", "description": "Calculated from OKRs and Feedback"},
        {"fieldname": "potential_score", "fieldtype": "Float", "label": "Potential Score (Y-axis)", "description": "Manager's rating for the 9-box grid"},
        {"fieldname": "final_rating", "fieldtype": "Select", "options": "1 - Needs Improvement\n2 - Meets Expectations\n3 - Exceeds Expectations", "label": "Final Rating"},
        {"fieldname": "status", "fieldtype": "Select", "options": "Draft\nManager Review\nHR Review\nFinalized", "label": "Status", "default": "Draft", "in_list_view": 1}
    ], is_submittable=1)

    frappe.db.commit()
    print("Doctype Creation Complete.")
