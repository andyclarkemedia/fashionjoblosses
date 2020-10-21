# =========================
# Sources dictionary with all the landing urls for sites
# -----
# - These urls will be visited and new article urls scraped from them
# =========================

# Note: This file will be updated frequently with more source urls

# ================
# IMPORTS 
# ================

from ..modules.url_helpers import reuters_url_list_creator



# ================
# Sources Dictionary
# ================


sources_dictionary_pause = {


	"Drapers - Home": {
		"country": "United Kingdom",
		"language": "English",
		"landing_urls": ["https://www.drapersonline.com/"],
		"landing_characteristics": '//div[contains(@id, "main-content")]//a/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//span[contains(@class, 'tie-date')]",
		"article_url_prefix": "",
		"fashionb2b": True
	},
	"Drapers - Redundancies": {
		"country": "United Kingdom",
		"language": "English",
		"landing_urls": ["https://www.drapersonline.com/tag/redundancies", "https://www.drapersonline.com/tag/redundancies/page/2", "https://www.drapersonline.com/tag/redundancies/page/3", "https://www.drapersonline.com/tag/redundancies/page/4", "https://www.drapersonline.com/tag/redundancies/page/5", "https://www.drapersonline.com/tag/redundancies/page/6"],
		"landing_characteristics": '//div[contains(@id, "main-content")]//a/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//span[contains(@class, 'tie-date')]",
		"article_url_prefix": "",
		"fashionb2b": True
	},
	"Retail Detail - Home": {
		"country": "Europe",
		"language": "English",
		"landing_urls": ["https://www.retaildetail.eu/en"],
		"landing_characteristics": '//a[contains(@href, "https")]/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//div[contains(@class, 'date')]",
		"article_url_prefix": "",
		"fashionb2b": True
	},
	"Retail Detail - Fashion": {
		"country": "Europe",
		"language": "English",
		"landing_urls": ["https://www.retaildetail.eu/en/fashion", "https://www.retaildetail.eu/en/fashion?page=1", "https://www.retaildetail.eu/en/fashion?page=2", "https://www.retaildetail.eu/en/fashion?page=3", "https://www.retaildetail.eu/en/fashion?page=4", "https://www.retaildetail.eu/en/fashion?page=5", "https://www.retaildetail.eu/en/fashion?page=6", "https://www.retaildetail.eu/en/fashion?page=7", "https://www.retaildetail.eu/en/fashion?page=8", "https://www.retaildetail.eu/en/fashion?page=9", "https://www.retaildetail.eu/en/fashion?page=10", "https://www.retaildetail.eu/en/fashion?page=11"],
		"landing_characteristics": '//a[contains(@href, "https")]/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//div[contains(@class, 'date')]",
		"article_url_prefix": "",
		"fashionb2b": True
	},
	"Reuters - Business News": {
		"country": "Global",
		"language": "English",
		"landing_urls": reuters_url_list_creator(),
		"landing_characteristics": '//a[contains(@href, "article")]/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//meta[contains(@property, 'og:article:published_time')]/@content",
		"fashionb2b": False,
		"article_url_prefix": "https://uk.reuters.com"
	}


}


sources_dictionary_not_working = {
	
}


sources_dictionary = {

	"Reuters - Business News": {
		"country": "Global",
		"language": "English",
		"landing_urls": reuters_url_list_creator(),
		"landing_characteristics": '//a[contains(@href, "article")]/@href',
		"article_characteristics": "//p",
		"headline_characteristics": "//h1",
		"published_date_characteristics": "//meta[contains(@property, 'og:article:published_time')]/@content",
		"fashionb2b": False,
		"article_url_prefix": "https://uk.reuters.com"
	}

}