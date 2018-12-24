from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.

def index(request):
	"""View function for home page of site."""

	# Generate counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	# Available books (status = 'a')
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()

	# The 'all()' is implied by default.
	num_authors = Author.objects.count()
	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	# Added by me - study case
	num_books_darktower = Book.objects.filter(title__icontains='dark').count()
	num_genres_fiction = Genre.objects.filter(name__contains='fiction').count()

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		# Added by me - study case
		'num_books_darktower': num_books_darktower,
		'num_genres_fiction': num_genres_fiction,
		'num_visits': num_visits,
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'catalog/index.html', context=context)


class BookListView(generic.ListView):
	"""
	That's it! The generic view will query the database to get all records
	for the specified model (Book) then render a template located
	at /catalog/templates/catalog/book_list.html (which we will create below).
	Within the template you can access the list of books with the template
	variable named object_list OR book_list (i.e. generically "the_model_name_list").
	"""
	model = Book
	# context_object_name = 'my_book_list'  # your own name for the list as a template variable by default it is book_list
	# queryset = Book.objects.filter(title__icontains='dark')[:3]  # Get 5 books containing the title war
	# template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
	model = Book
	'''
	With this addition, as soon as you have more than 
	10 records the view will start paginating the data it sends to 
	the template. The different pages are accessed using 
	GET parameters — to access page 2 you would use the 
	URL: /catalog/books/?page=2
	'''
	paginate_by = 2


class AuthorListView(generic.ListView):
	model = Author


class AuthorDetailView(generic.DetailView):
	model = Author
	paginate_by = 2
