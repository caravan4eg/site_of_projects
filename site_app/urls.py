from django.urls import path
from . views import *

app_name = 'site_app'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('search-form/', search_form, name='search_from'),

    ]
