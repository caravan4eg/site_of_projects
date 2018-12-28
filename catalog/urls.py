from django.urls import path
from . views import *
# from django.contrib.auth import urls

app_name = 'catalog'


urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('userbooks/', LoanedBooksByLibrariansListView.as_view(), name='user-borrowed'),
    path('book/<uuid:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),

    path('book/create/', BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
    ]
