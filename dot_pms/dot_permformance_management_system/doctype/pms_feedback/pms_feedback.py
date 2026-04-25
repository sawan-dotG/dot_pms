import frappe
from frappe.model.document import Document

class PMSFeedback(Document):
	def before_insert(self):
		self.analyze_sentiment()

	def analyze_sentiment(self):
		# Mock AI Sentiment Analysis based on keyword matching for the MVP
		text = self.content.lower() if self.content else ""
		
		positive_words = ["great", "awesome", "excellent", "good", "amazing", "thanks", "kudos", "appreciate"]
		constructive_words = ["improve", "better", "could", "next time", "suggest", "try", "issue", "problem"]
		
		pos_count = sum(1 for word in positive_words if word in text)
		con_count = sum(1 for word in constructive_words if word in text)
		
		if pos_count > con_count:
			self.sentiment = "Positive"
		elif con_count > pos_count:
			self.sentiment = "Constructive"
		else:
			self.sentiment = "Neutral"
