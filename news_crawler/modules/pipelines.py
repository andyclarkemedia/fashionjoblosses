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
from news_crawler.modules.items import ScoreItem, SentenceItem, ClubScoreItem, ClubSentenceItem


# Accessing top level
import sys
sys.path.append("..")
from main.models import Player, Club