from django.shortcuts import render
from catalog.models import *
from blog.models import *

# Create your views here.


def home(request):
	return render(request, 'site_app/home.html')


def search_form(request):
	return render(request, 'site_app/search_form.html')


def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter your search request!')
		elif len(q) > 20:
			errors.append('Length of request should be less than 20 symbols!')
		else:
			books = Book.objects.filter(title__icontains=q)
			posts = Post.objects.filter(title__icontains=q)
			return render(request, 'site_app/search_results.html', context={'books': books, 'posts': posts, 'query': q})
	return render(request, 'site_app/search_form.html', {'errors': errors})