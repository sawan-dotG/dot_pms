# dotG Performance Management System - User Guide

This guide provides a step-by-step walkthrough on how to run a complete performance cycle using the dotG system. Since the Vue SPA acts primarily as the employee/manager frontend UI, all administrative setup and data entry for this simulation will happen in the standard **Frappe Desk**.

---

## Phase 1: Setup & Goal Alignment (Start of Quarter)

### 1. Initialize the Appraisal Cycle
* Go to Frappe Desk and create a new **PMS Appraisal Cycle**.
* Name it (e.g., `Q2 2026 Performance Cycle`), set the start and end dates, and leave the status as `Draft`.

### 2. Set the Company OKRs
* Create a **PMS Objective**. For example: 
  * **Title:** "Expand into EU Market"
  * **Owner:** CEO
* Create a **PMS Key Result** linked to that Objective. 
  * **Title:** "Close 50 Enterprise Deals in EU"
  * **Target Value:** 50

### 3. Define Competencies
* Create a few **PMS Competency** records. (e.g., **Name:** "Frappe Development", **Category:** Technical).
* Create a **PMS Skill Gap Assessment** for an employee, setting their current level (e.g., 3) against the required level (e.g., 5).

---

## Phase 2: The "Ops Flow" (Continuous Dialogue during the Quarter)

This is where dotG shines compared to traditional static HR tools by capturing continuous performance signals.

### 1. Logging OKR Progress
An employee makes progress on their goal. They create a **PMS Check-in**.
* **Select the Key Result:** "Close 50 Enterprise Deals"
* **New Value:** 10
> **How it works:** When submitted, the backend automation kicks in. It calculates that the Key Result is now 20% complete (10/50) and automatically updates the parent Objective's total progress.

### 2. Continuous Feedback
A manager or peer creates a **PMS Feedback** entry for an employee.
* **Type:** "Constructive"
* **Content:** "Great effort, but please try to improve documentation next time."
> **How it works:** Upon saving, our AI Sentiment hook intercepts the text, detects the words "improve" and "next time," and automatically tags the sentiment as `Constructive`.

### 3. Running a 1-on-1
* A manager schedules a **PMS 1-on-1** record with an employee.
* In the child table **PMS 1-on-1 Agenda**, they add talking points.
* During the meeting, if an Action Item isn't finished, they check the `Carried Over` box so it appears in next week's sync.
> *(Behind the scenes, our scheduled Nudge Engine will automatically flag managers who go 14+ days without creating one of these meeting records).*

---

## Phase 3: Appraisal & Analytics (End of Quarter)

### 1. Trigger the Appraisals
* HR goes back to the **PMS Appraisal Cycle** (`Q2 2026 Performance Cycle`) and changes the status from `Draft` to `Active`.
> **How it works:** This immediately triggers a custom automation hook. The system fetches all active employees and automatically creates draft **PMS Appraisal** documents for each of them.

### 2. Manager Review & The 9-Box Grid
* Managers open their direct reports' newly generated **PMS Appraisal** documents.
* Because of continuous tracking, managers don't have to guess how the employee did—they can base the **Performance Score (X-axis)** directly off the OKR progress and Feedback history.
* The manager inputs a **Potential Score (Y-axis)** and selects a **Final Rating** (e.g., "Exceeds Expectations").

### 3. HR Calibration
* HR uses **Frappe Insights** to pull the SQL queries provided in the system documentation.
* They look at the **Bell Curve Report** to ensure Managers aren't inflating ratings.
* The CEO looks at the **9-Box Grid Report** to instantly see who their high-potential, high-performance future leaders are.

You can simulate all of these steps right now by navigating to the newly created modules in your Frappe Desk instance!
