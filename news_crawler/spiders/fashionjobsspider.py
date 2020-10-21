# =========================
# Scrapy spider class used to scrape news articles from sources list
# =========================

# Steps:

	# 1. The spider will loop through the landing urls stored in the sources dictionary
	# 2. It will extract the article urls that match the specific landing_characteristics described in the sources dictionary
	# 3. It will then return a list of article dictionaries with the new article urls available from the corresponding source url - if that article url has not already been accessed
	# 4. Next each new article url is crawled
	# 5. The text is gathered from each article - according to specific article_characteristics described in the sources dictionary
	# 6. The text is then processed -- (cleaned, stopwords removed, teams identified, lemmatized and split into phrases)
	# 7. The output is a dataframe for each article with the structure outlined below
	# 8. Before returning, the dataframes are concatenated


# Output ---->  (Django Model Entry) JobLossMention 


# =============
#  IMPORTS 
# =============

# General Imports
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import logging
import datetime


# Settings 
from .. import settings


# Module Imports
from ..modules import sources_dictionary as sources_dictionary
from ..modules import clean_text as clean_text
from ..modules import phrases as phrases
from ..modules import identify_match as identify_match
from ..modules.items import VisitedURLItem as VisitedURLItem



import sys
sys.path.append("..")
from main.models import VisitedURL


# ================
# Function to check if url exists in DB Model VisitedURLs - Prevents URL from being visisted twice
# ================

def filter(parsed_response):

	# Declare new list of unaccessed_urls
	unaccessed_urls = []

	# Iterate through the individual urls in parsed_response
	for item in parsed_response:

		# Check if url is entry in DB ----> VisitedURL model 
		if VisitedURL.objects.filter(url=item).exists():
			continue
		# If item is not in previously_accessed_articles ----> append the item to previously_accessed_articles & add it to unaccessed_url list
		else:
			unaccessed_urls.append(item)
			# Enter Url into DB
			new_url_item = VisitedURLItem()
			new_url_item['url'] = item
			new_url_item['date_visited'] = datetime.datetime.now().date()
			
			# Save the new_url_item
			new_url_item.save()


	return unaccessed_urls



# ================
# The Spider 
# ================

class FashionJobsSpider(scrapy.Spider):


	def __init__(self):
		self.name="FashionJobsSpider"



	# Function will be called automatically when spider crawls
	def start_requests(self):

		# Iterate through the sources_dictionary
		for key, value in sources_dictionary.sources_dictionary.items():

			# Iterate through the landing urls for each source
			for item in value['landing_urls']:

				# Make the request and pass the response to be parsed
				source_request = scrapy.Request(url=item, callback=self.parse_source)

				# Add the source name to the parse keywords parameter
				source_request.cb_kwargs['key'] = key

				# Process the response
				yield source_request


	# Callback function to return a dictionary of the new article urls for each source listed in the sources dictionary	
	def parse_source(self, response, key):

		parse_source_result = {

			"source": key,
			"country": sources_dictionary.sources_dictionary[key]["country"],
			"language": sources_dictionary.sources_dictionary[key]["language"],
			"article_urls": filter(list(dict.fromkeys(response.xpath(sources_dictionary.sources_dictionary[key]["landing_characteristics"]).extract()))),
			"characteristics": sources_dictionary.sources_dictionary[key]["article_characteristics"],
			"headline_characteristics": sources_dictionary.sources_dictionary[key]["headline_characteristics"],
			"published_date_characteristics": sources_dictionary.sources_dictionary[key]["published_date_characteristics"],
			"fashionb2b": sources_dictionary.sources_dictionary[key]["fashionb2b"],
			"prefix": sources_dictionary.sources_dictionary[key]["article_url_prefix"],
			
		}

		# Iterate through the article_urls in parse_source_result
		for url in parse_source_result['article_urls']:

			# Prefix url - where required
			url_prefix = str(parse_source_result['prefix'] + url)

			# Make the request and pass the response to the callback function ----> self.parse_article
			article_request = scrapy.Request(url=url_prefix, callback=self.parse_article)

			# Add the source name to the parse keywords parameter
			article_request.cb_kwargs['publication_name'] = parse_source_result['source']

			# Add the article characteristics to the parse keywords parameter
			article_request.cb_kwargs['characteristics'] = parse_source_result['characteristics']

			# Add the headline characteristics to the parse keywords parameter
			article_request.cb_kwargs['headline_characteristics'] = parse_source_result['headline_characteristics']

			# Add the published_date_characteristics to the parse keywords parameter
			article_request.cb_kwargs['published_date_characteristics'] = parse_source_result['published_date_characteristics']

			# Add the country to the parse keywords parameter
			article_request.cb_kwargs['country'] = parse_source_result['country']

			# Add the language to the parse keywords parameter
			article_request.cb_kwargs['language'] = parse_source_result['language']

			# Add the article url to the parse keywords parameter
			article_request.cb_kwargs['url'] = url_prefix

			# Add the fashionb2b boolean to the parse keywords parameter
			article_request.cb_kwargs['fashionb2b'] = parse_source_result['fashionb2b']

			# Process the response
			yield article_request

	

	# Callback function to parse the text in the article urls returned from parse_source
	# Function will return a list of dataframes after having processed and cleaned the text
	def parse_article(self, response, publication_name, characteristics, headline_characteristics, published_date_characteristics, country, language, url, fashionb2b):

		# Clean the response object
		full_text = clean_text.clean_text(response.xpath(characteristics).extract())

		# Check if article is fashion related - (for non fashionb2b publications)
		is_fashion_article = True

		if fashionb2b == False:
			if "fashion" in " ".join(full_text) or "Fashion" in " ".join(full_text):
				pass
			elif "clothing" in " ".join(full_text) or "Clothing" in " ".join(full_text):
				pass
			elif "Huawei" in " ".join(full_text):
				pass
			else:
				is_fashion_article = False
		


		# Extract the headline
		headline = clean_text.clean_text(response.xpath(headline_characteristics).extract())

		# Extract the publication date
		publication_date = clean_text.clean_text(response.xpath(published_date_characteristics).extract())

		# Split the article into phrases and return a new list of dictionaries for each article
		item_list = phrases.phraseify(full_text, publication_name, language, country, url, headline, publication_date)

		# Loop through each phrase 
		for item in item_list:
			
			# Call the module to identify the key phrases within each article phrase
			target_dictionary = identify_match.identify_keywords_entities_numbers(item)

			# Only return the item (pass it through to the pipeline) if there is a key phrase match
			if len(target_dictionary['keywords']) != 0 and len(target_dictionary['phrase']) > 15 and is_fashion_article == True:
				yield target_dictionary
			else:
				pass
			

