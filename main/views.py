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
from .models import JobLossMention, Country, Date
from .serializers import CountrySerializer, JobLossMentionSerializer, DateSerializer



#===================
# The JobLossMention API view - Filter by publication_name // Search by date, country, publication_name
#===================
class JobLossMentionListCreate(generics.ListCreateAPIView):
	queryset = JobLossMention.objects.all()

	# Declare serializer_class
	serializer_class = JobLossMentionSerializer


	# Allow search functionality
	search_fields = ['date_text', 'country', 'publication_name']
	filter_backends = (filters.SearchFilter,)

	# Setting the filter options
	def get_queryset(self):
		""" Optionally restricts the returned job loss mention by filtering against a `publication_name` query parameter in the URL. """

		# Initially set the returned objects to be all sentences
		queryset = JobLossMention.objects.all()

		# Access the request params
		publication_name = self.request.query_params.get('publication_name', None)

		# If a player name is specified ---> Set the filter
		if publication_name is not None:
			queryset = queryset.filter(publication_name=publication_name)

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


#===================
# The Date API view - Filter by date // Search by date
#===================
class DateListCreate(generics.ListCreateAPIView):
	queryset = Date.objects.all()

	# Declare serializer_class
	serializer_class = DateSerializer


	# Allow search functionality
	search_fields = ['date']
	filter_backends = (filters.SearchFilter,)

	# Setting the filter options
	def get_queryset(self):
		""" Optionally restricts the returned job loss mention by filtering against a `country` query parameter in the URL. """

		# Initially set the returned objects to be all sentences
		queryset = Date.objects.all()

		# Access the request params
		date = self.request.query_params.get('date', None)

		# If a player name is specified ---> Set the filter
		if date is not None:
			queryset = queryset.filter(date=date)

		# Return the appropriate queryset
		return queryset

