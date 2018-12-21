from django.urls import path
from . views import *

app_name = 'site_app'

urlpatterns = [
    path('', home, name='home'),
    ]
