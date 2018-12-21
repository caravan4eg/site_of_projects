from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime
from .models import Book


# Create your views here.
def current_time(request):
	now = datetime.datetime.now()
	return render(request, 'book_app/current_time.html', context={'current_time': now})


def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	'''
	Если ошибка, если поставить False, то покажет без ошибки что здесь
	'''
	assert True
	# html = "<html><body><h1>Через %s часов будет %s часов !</h1></body></html>" % (offset, dt)
	# return HttpResponse(html)
	return render(request, 'book_app/hours_ahead.html', context={'hours_ahead': dt, 'offset': offset})


def order(request):
	now = datetime.datetime.now()
	c = {
		'company': 'Silveran',
		'ordered_warranty': True,
		'persone_name': 'NIK Ivanov',
		'ship_date': now,
		'item_list': ['BMW', 'White House', 'TV set Samsung']
	}
	return render(request, 'book_app/order.html', context=c)


def book_list(request):
	books = Book.objects.order_by('name')
	return render(request, 'book_app/book_list.html', {'books': books})


def display_meta(request):
	values_meta = sorted(request.META.items())
	path = request.path
	cook = request.COOKIES
	c = {'values_meta': values_meta,
	     'path': path,
	     'cook': cook}
	# html = []
	# for key, value in values:
	# 	html.append('<tr><td>{0}</td><td>{1}</tr></td>'.format(key, value))
	# report = '<table>%s</table>' % '\n'.join(html)
	# print(report)
	return render(request, 'book_app/display_meta.html', context=c)


def search_form(request):
	return render(request, 'book_app/search_form.html')


def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Введите поисковый запрос')
		elif len(q) > 20:
			errors.append('Введите поисковый запрос менее 20 символов')  # если запрос слишком длинный
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'book_app/search_results.html',
			              {'books': books, 'query': q})
	return render(request, 'book_app/search_form.html', {'errors': errors})
