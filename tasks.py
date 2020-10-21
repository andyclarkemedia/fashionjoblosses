# ================
# File contains tasks to be scheduled on Heroku Server
# ================

#

# SCHEDULED TASKS:
# ---------------
# This file is scheduled to run daily on the Heroku server
# It will first check the day of the week and ONLY RUN it's tasks on a MONDAY


# TASK 1: Call the spider to crawl - store the results in the database
# TASK 2: Check for VisitedURLs older than 100 days and delete them from the database

# =============
#  IMPORTS 
# =============

import datetime

# Local imports 
from news_crawler import crawl
from main.models import VisitedURL



# =======================================
# CHECK DAY OF THE WEEK (MONDAY = 0)
# =======================================

if datetime.datetime.today().weekday():

	# =============
	#  TASK 1 - crawl
	# =============
	crawl.crawl()


	# # =============
	# #  TASK 2 - Delete old URLs
	# # =============

	# today = datetime.datetime.now().date()
	# date_threshold = today - datetime.timedelta(days=100)
	# VisitedURL.objects.filter(date_visited__lte=date_threshold).delete()