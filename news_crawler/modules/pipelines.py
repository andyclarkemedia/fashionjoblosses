# ===================================================================
# Pipelines which process the result of the spider - ProcessItemPipeline stores items in the Database
# ===================================================================

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# ==============
# IMPORTS 
# ==============

# General Imports
import datetime


# Module Imports
from news_crawler.modules.items import JobLossMentionItem


# Accessing top level
import sys
sys.path.append("..")
from main.models import JobLossMention, Country




# ================
# ProcessItemPipeline ---> Process scraping result ... then -----> Store Items in DB (when spider has finished crawling)
# ================


class ProcessItemPipeline:

	# List attribute to store scraping results
	results_list = []

	def close_spider(self, spider):


		# ==========
		# Declare current date
		# ==========

		current_date = datetime.datetime.now().date()


    	# ==========
		# Loop through the results_dictionary and add the results to the DB
		# ==========
		
		for item in self.results_list:

			# Specify the current country & date
			current_country = item['country']

			country_model_reference = Country.objects.get(country=current_country)

			# Enter the item into the Database
			joblossmention_item = JobLossMentionItem()

			# Link to the country table
			joblossmention_item['country'] = country_model_reference

			# Add other fields
			joblossmention_item['publication_name'] = item['publication_name']
			joblossmention_item['date'] = current_date
			joblossmention_item['country_name'] = item['country']
			joblossmention_item['language'] = item['language']
			joblossmention_item['extracted_text'] = item['phrase']
			joblossmention_item['entities_mentioned'] = item['entities_mentioned']
			joblossmention_item['numbers_mentioned'] = item['numbers_mentioned']
			joblossmention_item['article_headline'] = item['article_headline']
			joblossmention_item['article_url'] = item['url']
			

			# Save the item
			joblossmention_item.save()


	def process_item(self, item, spider):


		# Add an entry in self.results_dictionary for each phrase where a keyword was matched
		self.results_list.append(item)

