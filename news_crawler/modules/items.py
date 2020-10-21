# =======================
# Link scrapy process to the Django Models; 'Date', 'Country', 'JobLossMention'
# =======================

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem


# Accessing top level
import sys
sys.path.append("..")
from main.models import Country, JobLossMention, VisitedURL



# JobLossMention - convert the django model into a scrapy django item
class JobLossMentionItem(DjangoItem):
	django_model = JobLossMention

# # Date - convert the django model into a scrapy django item
# class DateItem(DjangoItem):
# 	django_model = Date

# Country - convert the django model into a scrapy django item
class CountryItem(DjangoItem):
	django_model = Country

# VisitedURL - convert the django model into a scrapy django item
class VisitedURLItem(DjangoItem):
	django_model = VisitedURL
