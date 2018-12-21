from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'book_app'


urlpatterns = [
    path('', views.current_time, name='current_time'),
    url(r'^plus/(\d{1,2})/$', views.hours_ahead, name='hours_ahead'),
    path('order/', views.order, name='order'),
    path('display/', views.display_meta, name='display_meta'),
    path('search-form/', views.search_form, name='search_from'),
    path('search/', views.search, name='search'),
	# path('contact/', views.contact, name='contact'),
]