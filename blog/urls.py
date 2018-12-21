from . views import *
from django.urls import path

app_name = 'blog'


urlpatterns = [
	path('', post_list, name='post_list'),
	path('post/(<pk>\d+)/', post_detail, name='post_detail'),
	path('post/new/', post_new, name='post_new'),
	]

