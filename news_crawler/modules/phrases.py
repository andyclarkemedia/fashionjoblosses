# =========================
# Split article text into phrases
# =========================


# Parameters: 
	# - list of <p> elements in article
	# - string - publication_name
	# - string - language
	# - string - country
	# - string - article url


# Function will return a dictionary for each phrase of text in an article
# Function will tokenize the sentences 


# =============
#  IMPORTS 
# =============

from nltk.tokenize import sent_tokenize
from datetime import datetime

nltk.download('punkt')

# =============
#  Split into phrases
# =============

def phraseify(article_p_list, publication_name, language, country, article_url, headline, publication_date):

	# Declare the article_phrase_dictionary_list
	article_phrase_dictionary_list = []

	# Iterate through the <p> elements in article_p_list
	for p_element in article_p_list:

		# Tokenize the sentences
		for item in sent_tokenize(p_element):

			# Initialise a datetime object
			now = datetime.now()

			# Create a string from the datetime object
			datetime_string = now.strftime("%d/%m/%Y %H:%M:%S")

			# Split date and time
			date = datetime_string.split(" ")[0]

			# Create the individual phrase dictionary
			phrase_dictionary = {
				"publication_name": publication_name,
				"article_headline": str(headline)[1:-1],
				"publication_date": str(publication_date)[1:-1],
				"url": article_url,
				"language": language,
				"country": country,
				"date": date,
				"phrase": item,
			}

			# Append the dataframe list with the dictionary
			article_phrase_dictionary_list.append(phrase_dictionary)

				


	# Return a list of dictionaries
	return article_phrase_dictionary_list
