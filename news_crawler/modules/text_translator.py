# =========================
# A Helper function to translate text in non-English languages using 'googletrans' package
# =========================


# ================
# IMPORTS 
# ================
from googletrans import Translator



# ================
# REUTERS
# ================


def translate_text(full_text, language):

	if language == "English":
		return full_text

	translation_list = []

	translator = Translator()

	for phrase in full_text:

		translation = translator.translate(phrase, dest='en')

		translation_list.append(translation.text)


	return translation_list




