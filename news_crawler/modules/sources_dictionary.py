# =========================
# Sources dictionary with all the landing urls for sites
# -----
# - These urls will be visited and new article urls scraped from them
# =========================

# Note: This file will be updated frequently with more source urls

# ================
# IMPORTS 
# ================

sources_dictionary = {


	"Drapers": {
		"country": "United Kingdom",
		"language": "English",
		""
		"landing_urls": ["https://www.drapersonline.com/"],
		"landing_characteristics": '//div[contains(@id, "main-content")]//a[contains(@href, "match-report")]/@href',
		"article_characteristics": "//p/text()",
		"article_url_prefix": ""
	},

}


sources_dictionary_not_working = {
	
}


sources_dictionary_test = {

}