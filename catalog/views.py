from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
# to restrict access to info about loan book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
	"""Generic class-based view listing books on loan to current user."""
	model = BookInstance
	template_name = 'catalog/bookinstance_list_borrowed_user.html'
	paginate_by = 10

	def get_queryset(self):
		'''
		In order to restrict our query to just the BookInstance
		objects for the current user, we re-implement get_queryset()
		as shown below. Note that "o" is the stored code for "on loan"
		and we order by the due_back date so that the oldest
		items are displayed first.
		'''
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksByLibrariansListView(PermissionRequiredMixin, generic.ListView):
	"""Generic class-based view listing books on loan to librarians
	who has catalog.can_mark_returned permission."""
	permission_required = 'catalog.can_mark_returned'
	model = BookInstance
	template_name = 'catalog/bookinstance_list_borrowed_lib.html'
	paginate_by = 10
# в таком виде плказывает всем все отданные книги
	def get_queryset(self):
		return BookInstance.objects.filter(status__exact='o').order_by('due_back')