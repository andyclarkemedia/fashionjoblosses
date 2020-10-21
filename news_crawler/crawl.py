# ================
# File contains a function to run the scraper
# ================

# ================
# IMPORTS
# ================


import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import time


# # Local imports
from .spiders.fashionjobsspider import FashionJobsSpider
from . import settings

# Initialisation imports - NEW
# from .populateplayerstable import populate_players_model
# from .populateclubstable import populate_clubs_model


# ================
# The function that will initialise the scraping process
# ================

def crawl():

	# Populate the countries model - Ran only on DB setup
	# populate_clubs_model()

	# Start a timer
	start = time.time()

	# Initialise the Crawler Process applying the settings declared in news_crawler/settings.py
	crawler_settings = Settings()
	crawler_settings.setmodule(settings)
	process = CrawlerProcess(settings=crawler_settings)
	# Direct the process to the FashionJobsSpider
	process.crawl(FashionJobsSpider)
	# Start the spider
	process.start()

	# Finish the timer
	end = time.time()
	#Print time taken
	print("Time Taken:", end - start, "(seconds)")
