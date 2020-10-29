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

	# range(1,1201)
	for n in range(1, 41):
		urls.append("https://uk.reuters.com/news/archive/businessNews?view=page&page="+ str(n))

	return urls



# ================
# WOMANS WEAR DAILY
# ================


def wwd_url_list_creator():

	urls = []

	# range(1,226)
	for n in range(1,7):
		urls.append("https://wwd.com/business-news/page/"+ str(n) + '/')

	return urls


# ================
# MARK UP
# ================


def markup_url_list_creator():

	urls = []

	# range(1,81)
	for n in range(1,4):
		urls.append("https://www.mark-up.it/category/news/page/"+ str(n) + '/')

	return urls



# ================
# TextilZeitung
# ================


def tz_url_list_creator():

	urls = []

	# range(1,26)
	for n in range(1,3):
		urls.append("https://www.textilzeitung.at/business/?currPage="+ str(n))

	return urls



# ================
# Fashion Network - France
# ================


def fn_url_list_creator():

	urls = []

	# range(1,286)
	for n in range(1,9): 
		urls.append("https://be.fashionnetwork.com/news/s?page="+ str(n))

	return urls


# ================
# Fashion Network - Italy
# ================


def fn_italy_url_list_creator():

	urls = []

	# range(1,150)
	for n in range(1,6): 
		urls.append("https://it.fashionnetwork.com/news/s?page="+ str(n))

	return urls


# ================
# Fashion Network - USA
# ================


def fn_us_url_list_creator():

	urls = []

	# range(1,200)
	for n in range(1,7): 
		urls.append("https://us.fashionnetwork.com/news/s?page="+ str(n))

	return urls


# ================
# Fashion Network - UK
# ================


def fn_uk_url_list_creator():

	urls = []

	# range(1,250)
	for n in range(1,10): 
		urls.append("https://uk.fashionnetwork.com/news/s?page="+ str(n))

	return urls



# ================
# Retail Detail - Netherlands
# ================


def rdbl_url_list_creator():

	urls = []

	# range(1,20)
	for n in range(1,4): 
		urls.append("https://www.retaildetail.be/fr/mode?page="+ str(n))

	return urls



# ================
# DM&T 
# ================


def dansk_url_list_creator():

	urls = []

	# range(1,21)
	for n in range(1,3): 
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
	for n in range(1,4): 
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
	for n in range(1,10): 
		urls.append("https://www.fibre2fashion.com/news/allnews.aspx?SortBy=latest&page="+ str(n))

	return urls



# ================
# Fibre 2 Fashion - Articles
# ================


def fibrefashion_articles_url_list_creator():

	urls = []

	# range(1,16)
	for n in range(1,3): 
		urls.append("https://www.fibre2fashion.com/industry-article/search?category=articles&page="+ str(n))

	return urls



# ================
# Nikkei Asia
# ================


def nikkei_url_list_creator():

	urls = []

	# range(1,61)
	for n in range(1,3): 
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

	for n in range(1,2): 
		urls.append("https://vnexpress.net/tag/det-may-736343-p"+ str(n))

	return urls



# ================
# ShareBiz - Bangladesh
# ================


def sharebiz_url_list_creator():

	urls = []

	# range(1, 55)
	for n in range(1,3): 
		urls.append("https://sharebiz.net/category/today-news/industrial-trade/trade-news/page/"+ str(n) +'/')

	return urls




# ================
# Textil Wirtschaft
# ================


def txtwr_url_list_creator():

	urls = []

	# range(1, 200)
	for n in range(1,7): 
		urls.append("https://www.textilwirtschaft.de/nachrichten/?currPage="+ str(n))

	return urls




# ================
# Textil Wirtschaft - Biz
# ================


def txtwr_biz_url_list_creator():

	urls = []

	# range(1, 190)
	for n in range(1,7): 
		urls.append("https://www.textilwirtschaft.de/business/?currPage="+ str(n))

	return urls


# ================
# Textil Wirtschaft - Fashion
# ================


def txtwr_fashion_url_list_creator():

	urls = []

	# range(1, 200)
	for n in range(1,3): 
		urls.append("https://www.textilwirtschaft.de/fashion/?currPage="+ str(n))

	return urls



# ================
# Le Nouvelle Economiste - News
# ================


def lne_url_list_creator():

	urls = []

	# range(1, 30)
	for n in range(1,3): 
		urls.append("https://www.lenouveleconomiste.fr/les-analyses/page/"+ str(n) + '/')

	return urls



# ================
# Fashion United France - Business
# ================


def fu_biz_france_url_list_creator():

	urls = []

	# range(1, 59)
	for n in range(1,4): 
		urls.append("https://fashionunited.fr/actualite/business/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United France - Fashion
# ================


def fu_fashion_france_url_list_creator():

	urls = []

	# range(1, 76)
	for n in range(1,4): 
		urls.append("https://fashionunited.fr/actualite/mode/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United France - Retail
# ================


def fu_retail_france_url_list_creator():

	urls = []

	# range(1, 25)
	for n in range(1,3): 
		urls.append("https://fashionunited.fr/actualite/retail/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United Spain - Business
# ================


def fu_biz_spain_url_list_creator():

	urls = []

	# range(1, 42)
	for n in range(1,4): 
		urls.append("https://fashionunited.es/noticias/empresas/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United Spain - Fashion
# ================


def fu_fashion_spain_url_list_creator():

	urls = []

	# range(1, 50)
	for n in range(1,3): 
		urls.append("https://fashionunited.es/noticias/moda/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United Spain - Retail
# ================


def fu_retail_spain_url_list_creator():

	urls = []

	# range(1, 29)
	for n in range(1,2): 
		urls.append("https://fashionunited.es/noticias/retail/Page-"+ str(n) + '/')

	return urls




# ================
# Fashion United Netherlands - Business
# ================


def fu_biz_netherlands_url_list_creator():

	urls = []

	# range(1, 80)
	for n in range(1,5): 
		urls.append("https://fashionunited.nl/nieuws/business/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United Netherlands - Fashion
# ================


def fu_fashion_netherlands_url_list_creator():

	urls = []

	# range(1, 60)
	for n in range(1,3): 
		urls.append("https://fashionunited.nl/nieuws/mode/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United Netherlands - Retail
# ================


def fu_retail_netherlands_url_list_creator():

	urls = []

	# range(1, 30)
	for n in range(1,2): 
		urls.append("https://fashionunited.nl/nieuws/retail/Page-"+ str(n) + '/')

	return urls




# ================
# Fashion United UK - Business
# ================


def fu_biz_uk_url_list_creator():

	urls = []

	# range(1, 120)
	for n in range(1,6): 
		urls.append("https://fashionunited.uk/news/business/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United UK - Fashion
# ================


def fu_fashion_uk_url_list_creator():

	urls = []

	# range(1, 140)
	for n in range(1,5): 
		urls.append("https://fashionunited.uk/news/fashion/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United UK - Retail
# ================


def fu_retail_uk_url_list_creator():

	urls = []

	# range(1, 70)
	for n in range(1,4): 
		urls.append("https://fashionunited.uk/news/retail/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United Germany - Business
# ================


def fu_biz_germany_url_list_creator():

	urls = []

	# range(1, 35)
	for n in range(1,5): 
		urls.append("https://fashionunited.de/nachrichten/business/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United Germany - Fashion
# ================


def fu_fashion_germany_url_list_creator():

	urls = []

	# range(1, 65)
	for n in range(1,5): 
		urls.append("https://fashionunited.de/nachrichten/mode/Page-"+ str(n) + '/')

	return urls



# ================
# Fashion United Germany - Retail
# ================


def fu_retail_germany_url_list_creator():

	urls = []

	# range(1, 25)
	for n in range(1,3): 
		urls.append("https://fashionunited.de/nachrichten/einzelhandel/Page-"+ str(n) + '/')

	return urls



# ================
# Dialog Textil - Fashion
# ================


def dtxtrm_fashion_url_list_creator():

	urls = []

	# range(1, 7)
	for n in range(1,2): 
		urls.append("https://dialogtextil.ro/category/moda/page/"+ str(n) + '/')

	return urls



# ================
# Dialog Textil - News
# ================


def dtxtrm_news_url_list_creator():

	urls = []

	# range(1, 18)
	for n in range(1,2): 
		urls.append("https://dialogtextil.ro/category/stiri/page/"+ str(n) + '/')

	return urls








