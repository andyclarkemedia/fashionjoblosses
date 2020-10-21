# =========================
# Register models with the 'main' app
# =========================


# =============
# IMPORTS 
# =============

from django.contrib import admin

# Local imports 
from main.models import Country, Date, JobLossMention


# ===============
# Customising appearance of admin site
# ===============

# Change Site Header
admin.site.site_header = "Vogue Business - Fashion Job Losses Tracker"


# ===============
# Customise Appearance of Models
# ===============

# ==========
# Country
# ==========


class CountryDisplay(admin.ModelAdmin):

	list_display = ('country', )

	list_filter = ('country', )


# ==========
# Date
# ==========


class DateDisplay(admin.ModelAdmin):

	list_display = ('date', )

	list_filter = ('date', )



# ==========
# JobLossMention
# ==========


class JobLossMentionDisplay(admin.ModelAdmin):

	list_display = ('publication_name', 'extracted_text', 'numbers_mentioned')

	list_filter = ('country', 'date_text')





# ================
# Register your models here
# ================
admin.site.register(Country, CountryDisplay)
admin.site.register(Date, DateDisplay)
admin.site.register(JobLossMention, JobLossMentionDisplay)



