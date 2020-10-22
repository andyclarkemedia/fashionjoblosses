# =========================
# Helper functions to support the sources dictionary in finding the correct landing URLs to visit.
# =========================


# ================
# IMPORTS 
# ================
import datetime



# ================
# REUTERS
# ================


def reuters_url_list_creator():

	urls = []

	for n in range(1, 1201):
		urls.append("https://uk.reuters.com/news/archive/businessNews?view=page&page="+ str(n))

	return urls



# ================
# WOMANS WEAR DAILY
# ================


def wwd_url_list_creator():

	urls = []

	for n in range(1,226):
		urls.append("https://wwd.com/business-news/page/"+ str(n) + '/')

	return urls


# ================
# MARK UP
# ================


def markup_url_list_creator():

	urls = []

	for n in range(1,81):
		urls.append("https://www.mark-up.it/category/news/page/"+ str(n) + '/')

	return urls



# ================
# TextilZeitung
# ================


def tz_url_list_creator():

	urls = []

	for n in range(1,26):
		urls.append("https://www.textilzeitung.at/business/?currPage="+ str(n))

	return urls



# ================
# Fashion Network
# ================


def fn_url_list_creator():

	urls = []

	# range(1,286)
	for n in range(1,286): 
		urls.append("https://be.fashionnetwork.com/news/s?page="+ str(n))

	return urls



# ================
# Retail Detail - Netherlands
# ================


def rdbl_url_list_creator():

	urls = []

	for n in range(1,20): 
		urls.append("https://www.retaildetail.be/fr/mode?page="+ str(n))

	return urls



# ================
# DM&T 
# ================


def dansk_url_list_creator():

	urls = []

	# range(1,21)
	for n in range(1,5): 
		urls.append("https://www.dmogt.dk/branchenyt?page="+ str(n))

	return urls




# ================
# Modaes 
# ================


def modaes_url_list_creator():

	urls = []

	# range(1,101)
	for n in range(1,5): 
		urls.append("https://www.modaes.es/empresa.html?page="+ str(n))

	return urls





# ================
# Fashion Magazine - Italy 
# ================


def fmitaly_url_list_creator():

	urls = []

	# range(1,65)
	for n in range(1,5): 
		urls.append("https://www.fashionmagazine.it/business/?currPage="+ str(n))

	return urls


# ================
# Just Style 
# ================


def juststyle_url_list_creator():

	urls = []

	# range(1,60)
	for n in range(1,3): 
		urls.append("https://www.just-style.com/search.aspx?q=&p="+ str(n) + "&ob=0&fqd=0&fq[0]=content_type:")

	return urls





# ================
# Fibre 2 Fashion - All News
# ================


def fibrefashion_allnews_url_list_creator():

	urls = []

	# range(1,310)
	for n in range(1,3): 
		urls.append("https://www.fibre2fashion.com/news/allnews.aspx?SortBy=latest&page="+ str(n))

	return urls



# ================
# Fibre 2 Fashion - Articles
# ================


def fibrefashion_articles_url_list_creator():

	urls = []

	# range(1,16)
	for n in range(1,16): 
		urls.append("https://www.fibre2fashion.com/industry-article/search?category=articles&page="+ str(n))

	return urls



# ================
# Nikkei Asia
# ================


def nikkei_url_list_creator():

	urls = []

	# range(1,61)
	for n in range(1,11): 
		urls.append("https://asia.nikkei.com/Business/Retail?page="+ str(n))

	return urls



# ================
# Wall Street Journal
# ================


# def wsj_retail_url_list_creator():

# 	urls = []

# 	# range(1,61)
# 	for n in range(1,11): 
# 		urls.append("https://www.wsj.com/news/business/retail-industry"+ str(n))

# 	return urls



# ================
# VN Express
# ================


def vnexpress_url_list_creator():

	urls = []

	# range(1,61)
	for n in range(1,2): 
		urls.append("https://vnexpress.net/tag/det-may-736343-p"+ str(n))

	return urls
