# =========================
# This file contains API URL patters that will be used to make and send requests
# =========================

# =============
# IMPORTS 
# =============
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# Local Imports 
from . import views



# Define the url patterns here

urlpatterns = [
    path('api/countries/', views.CountryListCreate.as_view()),
    # path('api/dates/', views.DateListCreate.as_view()),
    path('api/joblossmentions/', views.JobLossMentionListCreate.as_view()),
]