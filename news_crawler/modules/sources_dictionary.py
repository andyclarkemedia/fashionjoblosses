# =========================
# Sources dictionary with all the landing urls for sites
# -----
# - These urls will be visited and new article urls scraped from them
# =========================

# Note: This file will be updated frequently with more source urls

# ================
# IMPORTS 
# ================

from ..modules.url_helpers import reuters_url_list_creator, wwd_url_list_creator, markup_url_list_creator, tz_url_list_creator, fn_url_list_creator, rdbl_url_list_creator, dansk_url_list_creator, modaes_url_list_creator, fmitaly_url_list_creator, juststyle_url_list_creator, fibrefashion_allnews_url_list_creator, fibrefashion_articles_url_list_creator, nikkei_url_list_creator, vnexpress_url_list_creator, sharebiz_url_list_creator, txtwr_url_list_creator, txtwr_biz_url_list_creator, txtwr_fashion_url_list_creator, lne_url_list_creator, fu_biz_france_url_list_creator, fu_fashion_france_url_list_creator, fu_retail_france_url_list_creator, fu_biz_spain_url_list_creator, fu_fashion_spain_url_list_creator, fu_retail_spain_url_list_creator, fu_biz_netherlands_url_list_creator, fu_fashion_netherlands_url_list_creator, fu_retail_netherlands_url_list_creator, fu_biz_uk_url_list_creator, fu_fashion_uk_url_list_creator, fu_retail_uk_url_list_creator, fu_biz_germany_url_list_creator, fu_fashion_germany_url_list_creator, fu_retail_germany_url_list_creator, fn_italy_url_list_creator, dtxtrm_fashion_url_list_creator, dtxtrm_news_url_list_creator, fn_us_url_list_creator, fn_uk_url_list_creator



# ================
# Sources Dictionary
# ================


sources_dictionary = {


	# "Drapers - Home": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": ["https://www.drapersonline.com/"],
	# 	"landing_characteristics": '//div[contains(@id, "main-content")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'tie-date')]",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Drapers - Redundancies": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": ["https://www.drapersonline.com/tag/redundancies", "https://www.drapersonline.com/tag/redundancies/page/2", "https://www.drapersonline.com/tag/redundancies/page/3", "https://www.drapersonline.com/tag/redundancies/page/4", "https://www.drapersonline.com/tag/redundancies/page/5", "https://www.drapersonline.com/tag/redundancies/page/6"],
	# 	"landing_characteristics": '//div[contains(@id, "main-content")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'tie-date')]",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Retail Detail - Home": {
	# 	"country": "Europe",
	# 	"language": "English",
	# 	"landing_urls": ["https://www.retaildetail.eu/en"],
	# 	"landing_characteristics": '//a[contains(@href, "https")]/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//div[contains(@class, 'date')]",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Retail Detail - Fashion": {
	# 	"country": "Europe",
	# 	"language": "English",
	# 	"landing_urls": ["https://www.retaildetail.eu/en/fashion", "https://www.retaildetail.eu/en/fashion?page=1", "https://www.retaildetail.eu/en/fashion?page=2", "https://www.retaildetail.eu/en/fashion?page=3", "https://www.retaildetail.eu/en/fashion?page=4", "https://www.retaildetail.eu/en/fashion?page=5", "https://www.retaildetail.eu/en/fashion?page=6", "https://www.retaildetail.eu/en/fashion?page=7", "https://www.retaildetail.eu/en/fashion?page=8", "https://www.retaildetail.eu/en/fashion?page=9", "https://www.retaildetail.eu/en/fashion?page=10", "https://www.retaildetail.eu/en/fashion?page=11"],
	# 	"landing_characteristics": '//a[contains(@href, "https")]/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//div[contains(@class, 'date')]",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Reuters - Business News": {
	# 	"country": "Global",
	# 	"language": "English",
	# 	"landing_urls": reuters_url_list_creator(),
	# 	"landing_characteristics": '//a[contains(@href, "article")]/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//meta[contains(@property, 'og:article:published_time')]/@content",
	# 	"fashionb2b": False,
	# 	"article_url_prefix": "https://uk.reuters.com"
	# },
	# "Womans Wear Daily - Business": {
	# 	"country": "Global",
	# 	"language": "English",
	# 	"landing_urls": wwd_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "archive__post")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//div[contains(@id, 'author-container')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": ""
	# },
	# "Mark Up - News": {
	# 	"country": "Italy",
	# 	"language": "Italian",
	# 	"landing_urls": markup_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "td-module-thumb")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//time[contains(@class, 'entry-date')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": ""
	# },
	# "TextilZeitung - Business": {
	# 	"country": "Austria",
	# 	"language": "German",
	# 	"landing_urls": tz_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'PublishDate_date')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": "https://www.textilzeitung.at"
	# },
	# "Fashion Network Belgium - Business News": {
	# 	"country": "Belgium",
	# 	"language": "French",
	# 	"landing_urls": fn_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'time-ago__text')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": ""
	# },
	"Retail Detail Belgium - Fashion": {
		"country": "Belgium",
		"language": "French",
		"landing_urls": rdbl_url_list_creator(),
		"landing_characteristics": '//a[contains(@href, "https")]/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//div[contains(@class, 'date')]",
		"article_url_prefix": "",
		"fashionb2b": True
	},
	"Dansk Mode & Textil": {
		"country": "Denmark",
		"language": "Danish",
		"landing_urls": dansk_url_list_creator(),
		"landing_characteristics": '//div[contains(@class, "column-block")]//a/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//span[contains(@class, 'article__detail')]",
		"article_url_prefix": "https://www.dmogt.dk",
		"fashionb2b": True
	},
	"Modaes": {
		"country": "Spain",
		"language": "Spanish",
		"landing_urls": modaes_url_list_creator(),
		"landing_characteristics": '//div[contains(@class, "title")]//a/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1[contains(@class, 'title')]",
		"published_date_characteristics": "//div[contains(@class, 'news_block_title')]",
		"article_url_prefix": "https://www.modaes.es/",
		"fashionb2b": True
	},
	# "Fashion Magazine Italy - Business": {
	# 	"country": "Italy",
	# 	"language": "Italian",
	# 	"landing_urls": fmitaly_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'PublishDate_date')]",
	# 	"article_url_prefix": "https://www.fashionmagazine.it",
	# 	"fashionb2b": True
	# },
	# "Business of Fashion **": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": ['https://www.businessoffashion.com/articles'],
	# 	"landing_characteristics": '//a[contains(@tracker, "Article")]/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1[contains(@class, 'article-title')]",
	# 	"published_date_characteristics": "//div[contains(@class, 'text-uppercase sans-serif small-font horizontal-borders margin-vertical-xs-3')]",
	# 	"article_url_prefix": "https://www.businessoffashion.com/",
	# 	"fashionb2b": True
	# },
	# "Just Style": {
	# 	"country": "Global",
	# 	"language": "English",
	# 	"landing_urls": juststyle_url_list_creator(),
	# 	"landing_characteristics": '//p[contains(@class, "linktitle")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1[contains(@class, 'articleTitle')]",
	# 	"published_date_characteristics": "//p[contains(@class, 'date')]",
	# 	"article_url_prefix": "https://www.just-style.com",
	# 	"fashionb2b": True
	# },
	# "Fibre 2 Fashion - All News": {
	# 	"country": "Global",
	# 	"language": "English",
	# 	"landing_urls": fibrefashion_allnews_url_list_creator(),
	# 	"landing_characteristics": '//a[contains(@class, "blue-heading")]/@href',
	# 	"article_characteristics": "//span[contains(@class, 'news-details-txt')]",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//div[contains(@class, 'news-date')]",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Fibre 2 Fashion - Articles": {
	# 	"country": "Global",
	# 	"language": "English",
	# 	"landing_urls": fibrefashion_articles_url_list_creator(),
	# 	"landing_characteristics": '//a[contains(@class, "blue-heading")]/@href',
	# 	"article_characteristics": "//div[contains(@class, 'article-text')]",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//div[contains(@class, 'published-on')]",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Nikkei Asia - Business/Retail": {
	# 	"country": "Asia",
	# 	"language": "English",
	# 	"landing_urls": nikkei_url_list_creator(),
	# 	"landing_characteristics": '//a[contains(@data-trackable, "headline")]/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//time[contains(@class, 'timestamp__time')]",
	# 	"article_url_prefix": "https://asia.nikkei.com/",
	# 	"fashionb2b": False
	# },
	# "VN Express": {
	# 	"country": "Vietnam",
	# 	"language": "Vietnamese",
	# 	"landing_urls": vnexpress_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'date')]",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Indian Economic Times - Textile Industry": {
	# 	"country": "India",
	# 	"language": "English",
	# 	"landing_urls": ['https://economictimes.indiatimes.com/topic/Indian-textile-industry'],
	# 	"landing_characteristics": '//div[contains(@class, "topicstry")]//a/@href',
	# 	"article_characteristics": "//div[contains(@class, 'artText')]",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://economictimes.indiatimes.com/",
	# 	"fashionb2b": True
	# },
	# "BBC - Retailing": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": ['https://www.bbc.co.uk/news/topics/ce1qrvlegjyt/retailing'],
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://www.bbc.co.uk",
	# 	"fashionb2b": False
	# },
	# "BBC - Business": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": ['https://www.bbc.co.uk/news/business'],
	# 	"landing_characteristics": '//a[contains(@href, "news")]/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://www.bbc.co.uk",
	# 	"fashionb2b": False
	# },
	# "Journal du Textile - Home": {
	# 	"country": "France",
	# 	"language": "French",
	# 	"landing_urls": ['https://www.journaldutextile.com/'],
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//article",
	# 	"headline_characteristics": "//h2",
	# 	"published_date_characteristics": "//button//font",
	# 	"article_url_prefix": "https://www.journaldutextile.com/",
	# 	"fashionb2b": True
	# },
	# "Journal du Textile - This Week": {
	# 	"country": "France",
	# 	"language": "French",
	# 	"landing_urls": ['https://www.journaldutextile.com/sommaire-de-la-semaine'],
	# 	"landing_characteristics": '//li//a/@href',
	# 	"article_characteristics": "//article",
	# 	"headline_characteristics": "//h2",
	# 	"published_date_characteristics": "//button[contains(@class, 'btn')]//font",
	# 	"article_url_prefix": "https://www.journaldutextile.com/",
	# 	"fashionb2b": True
	# },
	# "Textil Wirtschaft - News": {
	# 	"country": "Germany",
	# 	"language": "German",
	# 	"landing_urls": txtwr_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//div[contains(@class, 'PageArticle')]",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'PublishDate_date')]",
	# 	"article_url_prefix": "https://www.textilwirtschaft.de",
	# 	"fashionb2b": True
	# },
	# "Textil Wirtschaft - Business": {
	# 	"country": "Germany",
	# 	"language": "German",
	# 	"landing_urls": txtwr_biz_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//div[contains(@class, 'PageArticle')]",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'PublishDate_date')]",
	# 	"article_url_prefix": "https://www.textilwirtschaft.de",
	# 	"fashionb2b": True
	# },
	# "Textil Wirtschaft - Fashion": {
	# 	"country": "Germany",
	# 	"language": "German",
	# 	"landing_urls": txtwr_fashion_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//div[contains(@class, 'PageArticle')]",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'PublishDate_date')]",
	# 	"article_url_prefix": "https://www.textilwirtschaft.de",
	# 	"fashionb2b": True
	# },
	# "Le Nouvel Economiste - News": {
	# 	"country": "France",
	# 	"language": "French",
	# 	"landing_urls": lne_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": False
	# },
	# "Il Sole 24 - Fashion Business": {
	# 	"country": "Italy",
	# 	"language": "Italian",
	# 	"landing_urls": ['https://www.ilsole24ore.com/archivi/moda/storie-impresa/1', 'https://www.ilsole24ore.com/archivi/moda/storie-impresa/2', 'https://www.ilsole24ore.com/sez/moda/storie-impresa'],
	# 	"landing_characteristics": '//li[contains(@class, "list-lined-item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//p[contains(@class, 'ainfo-block')]",
	# 	"article_url_prefix": "https://www.ilsole24ore.com/",
	# 	"fashionb2b": True
	# },
	# "Il Sole 24 - Fashion Economics": {
	# 	"country": "Italy",
	# 	"language": "Italian",
	# 	"landing_urls": ['https://www.ilsole24ore.com/archivi/moda/economia-e-finanza/1', 'https://www.ilsole24ore.com/archivi/moda/economia-e-finanza/2', 'https://www.ilsole24ore.com/sez/moda/economia-e-finanza'],
	# 	"landing_characteristics": '//li[contains(@class, "list-lined-item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//p[contains(@class, 'ainfo-block')]",
	# 	"article_url_prefix": "https://www.ilsole24ore.com/",
	# 	"fashionb2b": True
	# },
	# "Il Sole 24 - Luxury Fashion News": {
	# 	"country": "Italy",
	# 	"language": "Italian",
	# 	"landing_urls": ['https://www.ilsole24ore.com/sez/moda/luxury'],
	# 	"landing_characteristics": '//li[contains(@class, "list-lined-item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//p[contains(@class, 'ainfo-block')]",
	# 	"article_url_prefix": "https://www.ilsole24ore.com/",
	# 	"fashionb2b": True
	# },
	# "Il Sole 24 - Fashion Archives": {
	# 	"country": "Italy",
	# 	"language": "Italian",
	# 	"landing_urls": ['https://www.ilsole24ore.com/archivi/moda/1', 'https://www.ilsole24ore.com/archivi/moda/2', 'https://www.ilsole24ore.com/archivi/moda/3', 'https://www.ilsole24ore.com/archivi/moda/4', 'https://www.ilsole24ore.com/archivi/moda/5', 'https://www.ilsole24ore.com/archivi/moda/6', 'https://www.ilsole24ore.com/archivi/moda/7', 'https://www.ilsole24ore.com/archivi/moda/8'],
	# 	"landing_characteristics": '//li[contains(@class, "list-lined-item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//p[contains(@class, 'ainfo-block')]",
	# 	"article_url_prefix": "https://www.ilsole24ore.com/",
	# 	"fashionb2b": True
	# },
	# "Fashion United Business - Spain": {
	# 	"country": "Spain",
	# 	"language": "Spanish",
	# 	"landing_urls": fu_biz_spain_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.es/",
	# 	"fashionb2b": True
	# },
	# "Fashion United Fashion - Spain": {
	# 	"country": "Spain",
	# 	"language": "Spanish",
	# 	"landing_urls": fu_fashion_spain_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.es/",
	# 	"fashionb2b": True
	# },
	# "Fashion United Retail - Spain": {
	# 	"country": "Spain",
	# 	"language": "Spanish",
	# 	"landing_urls": fu_retail_spain_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.es/",
	# 	"fashionb2b": True
	# },
	# "Fashion United Business - France": {
	# 	"country": "France",
	# 	"language": "French",
	# 	"landing_urls": fu_biz_france_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.fr/",
	# 	"fashionb2b": True
	# },
	# "Fashion United Fashion - France": {
	# 	"country": "France",
	# 	"language": "French",
	# 	"landing_urls": fu_fashion_france_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.fr/",
	# 	"fashionb2b": True
	# },
	# "Fashion United Retail - France": {
	# 	"country": "France",
	# 	"language": "French",
	# 	"landing_urls": fu_retail_france_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.fr/",
	# 	"fashionb2b": True
	# },
	# "Fashion United Business - Netherlands": {
	# 	"country": "Netherlands",
	# 	"language": "Dutch",
	# 	"landing_urls": fu_biz_netherlands_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Fashion United Fashion - Netherlands": {
	# 	"country": "Netherlands",
	# 	"language": "Dutch",
	# 	"landing_urls": fu_fashion_netherlands_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Fashion United Retail - Netherlands": {
	# 	"country": "Netherlands",
	# 	"language": "Dutch",
	# 	"landing_urls": fu_retail_netherlands_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": True
	# },
	# "Fashion United Business - United Kingdom": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": fu_biz_uk_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.uk",
	# 	"fashionb2b": True
	# },
	# "Fashion United Fashion - United Kingdom": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": fu_fashion_uk_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.uk",
	# 	"fashionb2b": True
	# },
	# "Fashion United Retail - United Kingdom": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": fu_retail_uk_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.uk",
	# 	"fashionb2b": True
	# },
	# "Fashion United Business - Germany": {
	# 	"country": "Germany",
	# 	"language": "German",
	# 	"landing_urls": fu_biz_germany_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.de",
	# 	"fashionb2b": True
	# },
	# "Fashion United Fashion - Germany": {
	# 	"country": "Germany",
	# 	"language": "German",
	# 	"landing_urls": fu_fashion_germany_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.de",
	# 	"fashionb2b": True
	# },
	# "Fashion United Retail - Germany": {
	# 	"country": "Germany",
	# 	"language": "German",
	# 	"landing_urls": fu_retail_germany_url_list_creator(),
	# 	"landing_characteristics": '//div[contains(@class, "item")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//div[contains(@class, 'page-header')]//h1",
	# 	"published_date_characteristics": "//time",
	# 	"article_url_prefix": "https://fashionunited.de",
	# 	"fashionb2b": True
	# },
	# "Fashion Network Italy - Business News": {
	# 	"country": "Italy",
	# 	"language": "Italian",
	# 	"landing_urls": fn_italy_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'time-ago__text')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": ""
	# },
	# "Dialog Textil - Fashion": {
	# 	"country": "Romania",
	# 	"language": "Romanian",
	# 	"landing_urls": dtxtrm_fashion_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//a[contains(@class, 'post-date')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": ""
	# },
	# "Dialog Textil - News": {
	# 	"country": "Romania",
	# 	"language": "Romanian",
	# 	"landing_urls": dtxtrm_news_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//a[contains(@class, 'post-date')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": ""
	# },
	# "Retail Asia - Fashion": {
	# 	"country": "Asia",
	# 	"language": "English",
	# 	"landing_urls": ['https://retailasia.net/fashion'],
	# 	"landing_characteristics": '//div[contains(@class, "views-row")]//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//div[contains(@class, 'article-published')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": "https://retailasia.net/"
	# },
	# "Fashion Network US - Business News": {
	# 	"country": "United States",
	# 	"language": "English",
	# 	"landing_urls": fn_us_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'time-ago__text')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": ""
	# },
	# "Fashion Network UK - Business News": {
	# 	"country": "United Kingdom",
	# 	"language": "English",
	# 	"landing_urls": fn_uk_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1",
	# 	"published_date_characteristics": "//span[contains(@class, 'time-ago__text')]",
	# 	"fashionb2b": True,
	# 	"article_url_prefix": ""
	# }
	


}


sources_dictionary_not_working = {

	"Wall Street Journal - All News Archives": {
		"country": "United States",
		"language": "English",
		"landing_urls": ['https://www.wsj.com/news/business/retail-industry'],
		"landing_characteristics": '//article//a/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//time[contains(@class, 'timestamp')]",
		"article_url_prefix": "",
		"fashionb2b": True
	},
	
}


sources_dictionary_test = {

	#False
	"BBC - Retailing": {
		"country": "United Kingdom",
		"language": "English",
		"landing_urls": ['https://www.bbc.co.uk/news/topics/ce1qrvlegjyt/retailing'],
		"landing_characteristics": '//article//a/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//time",
		"article_url_prefix": "https://www.bbc.co.uk",
		"fashionb2b": False
	},
	# "ShareBiz Trade News - Bangladesh": {
	# 	"country": "Bangladesh",
	# 	"language": "Bangladeshi",
	# 	"landing_urls": sharebiz_url_list_creator(),
	# 	"landing_characteristics": '//article//a/@href',
	# 	"article_characteristics": "//p",
	# 	"headline_characteristics": "//h1[contains(@class, 'title')]",
	# 	"published_date_characteristics": "//div[contains(@class, 'herald-date')]//font",
	# 	"article_url_prefix": "",
	# 	"fashionb2b": False
	# }

}