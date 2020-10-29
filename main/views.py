# =========================
# API config and filter options
# =========================



# =============
# IMPORTS 
# =============
from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

# Local imports 
from .models import JobLossMention, Country
from .serializers import CountrySerializer, JobLossMentionSerializer



#===================
# The JobLossMention API view - Filter by publication_name // Search by date, country, publication_name
#===================
class JobLossMentionListCreate(generics.ListCreateAPIView):
	queryset = JobLossMention.objects.all()

	# Declare serializer_class
	serializer_class = JobLossMentionSerializer


	# Allow search functionality
	search_fields = ['date_accessed', 'country', 'publication_name', 'publication_date']
	filter_backends = (filters.SearchFilter,)

	# Setting the filter options
	def get_queryset(self):
		""" Optionally restricts the returned job loss mention by filtering against a `date_accessed` query parameter in the URL. """

		# Initially set the returned objects to be all sentences
		queryset = JobLossMention.objects.all()

		# Access the request params
		date_accessed = self.request.query_params.get('date_accessed', None)

		# If a player name is specified ---> Set the filter
		if date_accessed is not None:
			queryset = queryset.filter(date_accessed=date_accessed)

		# Return the appropriate queryset
		return queryset


#===================
# The Country API view - Filter by country // Search by country
#===================
class CountryListCreate(generics.ListCreateAPIView):
	queryset = Country.objects.all()

	# Declare serializer_class
	serializer_class = CountrySerializer


	# Allow search functionality
	search_fields = ['country']
	filter_backends = (filters.SearchFilter,)

	# Setting the filter options
	def get_queryset(self):
		""" Optionally restricts the returned job loss mention by filtering against a `country` query parameter in the URL. """

		# Initially set the returned objects to be all sentences
		queryset = Country.objects.all()

		# Access the request params
		country = self.request.query_params.get('country', None)

		# If a player name is specified ---> Set the filter
		if country is not None:
			queryset = queryset.filter(country=country)

		# Return the appropriate queryset
		return queryset


# #===================
# # The Date API view - Filter by date // Search by date
# #===================
# class DateListCreate(generics.ListCreateAPIView):
# 	queryset = Date.objects.all()

# 	# Declare serializer_class
# 	serializer_class = DateSerializer


# 	# Allow search functionality
# 	search_fields = ['date']
# 	filter_backends = (filters.SearchFilter,)

# 	# Setting the filter options
# 	def get_queryset(self):
# 		""" Optionally restricts the returned job loss mention by filtering against a `country` query parameter in the URL. """

# 		# Initially set the returned objects to be all sentences
# 		queryset = Date.objects.all()

# 		# Access the request params
# 		date = self.request.query_params.get('date', None)

# 		# If a player name is specified ---> Set the filter
# 		if date is not None:
# 			queryset = queryset.filter(date=date)

# 		# Return the appropriate queryset
# 		return queryset

