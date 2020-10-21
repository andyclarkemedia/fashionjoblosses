# =======================
# REST serializer config - convert the Django models into a JSON for data access
# =======================

# ============
# IMPORTS 
# ============

from rest_framework import serializers
from .models import JobLossMention, Country






# The Serializer for Job Loss Mentions
class JobLossMentionSerializer(serializers.ModelSerializer):

	# Meta information to setup the serializer
	class Meta:
		model = JobLossMention
		fields = ['id', 'publication_name', 'extracted_text', 'language', 'entities_mentioned', 'numbers_mentioned', 'article_headline', 'article_url', 'country_name', 'date']



# The Serializer for Country
class CountrySerializer(serializers.ModelSerializer):

	# Link to the score serializer
	job_losses = JobLossMentionSerializer(many=True, read_only=True)

	# Meta information to setup the serializer
	class Meta:
		model = Country
		fields = ('id', 'country', 'job_losses')


# # The Serializer for Date
# class DateSerializer(serializers.ModelSerializer):

# 	# Link to the score serializer
# 	countries = CountrySerializer(many=True, read_only=True)
	
# 	# Meta information to setup the serializer
# 	class Meta:
# 		model = Date
# 		fields = ('id', 'date', 'countries')