from . views import *
from django.urls import path

app_name = 'blog'


urlpatterns = [
	path('', post_list, name='post_list'),
	path('post/<int:pk>/', post_detail, name='post_detail'),
	path('post/new/', post_new, name='post_new'),
	path('post/create/', PostCreate.as_view(), name='post_create'),
	path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
	path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

	]

