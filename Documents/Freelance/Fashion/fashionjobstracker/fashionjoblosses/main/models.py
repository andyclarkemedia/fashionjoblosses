# =========================
# Django DB Models used to store results of scraping process
# =========================


# =============
# IMPORTS 
# =============

from django.db import models



# =============
# Date Model - stores list of dates that crawler has run
#
# Fields: 	'date'
# =============


class Date(models.Model):

	# Declare the fields
	date = models.DateField()

	# Declare how the entry should appear on display
	def __str__(self):
		return "{}".format(self.date)

	# Specify the ordering of the data
	class Meta:
		ordering = ['date']




# =============
# Countries Model - stores list of countries
#
# Fields: 	'country'
# =============


class Country(models.Model):

	# Link to the Date Table 
	date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name="countries")

	# Declare the fields
	country = models.CharField(max_length=150)
	

	# Declare how the entry should appear on display
	def __str__(self):
		return "{}".format(self.country)

	# Specify the ordering of the data
	class Meta:
		ordering = ['country']




# =============
# Job Loss Mention Model - stores information on job loss as found in text of article
#
# Fields: 	'date', 'publication_name', 'country', 'language', 'extracted_text', 'entities_mentioned', 'numbers_mentioned' 'article_headline', 'article_url'
# =============


class JobLossMention(models.Model):

	# Link to the Country Table
	country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="job_losses")

	# Declare the fields
	publication_name = models.CharField(max_length=150)
	country_name = models.CharField(max_length=150)
	date_text = models.DateField()
	language = models.CharField(max_length=30)
	extracted_text = models.TextField()
	entities_mentioned = models.TextField()
	numbers_mentioned = models.TextField()
	article_headline = models.TextField()
	article_url = models.TextField()
	

	# Declare how the entry should appear on display
	def __str__(self):
		return "{} - {} {}".format(self.publication_name, self.extracted_text, self.numbers_mentioned)

	# Specify the ordering of the data
	class Meta:
		ordering = ['publication_name', 'extracted_text', 'numbers_mentioned']




# =======================================
# Visited URL Model - stores urls that have been visited by crawler
# =======================================

class VisitedURL(models.Model):

	# Declare the fields 
	url = models.URLField(max_length=300)
	date_visited = models.DateField()

	# Declare how the entry should appear on display
	def __str__(self):
		return "{}: {}".format(self.date_visited, self.url)

	# Specify the ordering of the data
	class Meta:
		ordering = ['date_visited', 'url']

