from django.urls import path
from django.conf.urls import url
from . views import *

app_name = 'book_app'


urlpatterns = [
    path('', current_time, name='current_time'),
    url(r'^plus/(\d{1,2})/$', hours_ahead, name='hours_ahead'),
    path('order/', order, name='order'),
    path('display/', display_meta, name='display_meta'),


	# path('contact/', views.contact, name='contact'),
]