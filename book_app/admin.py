from django.contrib import admin
from .models import *

# Register your models here.
'''
Для изменения отображения полей по умолчанию в административной панели
Теперь будет не один столбик имен как было при 
admin.site.register(Author), а три + Поиск
'''


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')


'''
Тут добавляем больше колонок для книг фильтр и порядок сортировки
'''


class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_filter = ('publication_date',)
	# list_filter = ('publisher')
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	filter_horizontal = ('authors',)
	raw_id_fields = ('publisher',)


class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'city', 'website')
	list_filter = ('city',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
