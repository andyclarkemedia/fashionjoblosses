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