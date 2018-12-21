from django.db import models


# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __str__(self):
		return self.name

	'''
	Так можно задать по какому полю будет сортироваться по умолчанию при выводе
	'''

	class Meta:
		ordering = ['name']


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField('e-mail', blank=True)  # e-mail - прямо указывает как будет показана метка поля в форме
	# blank=True делает поле необязательным

	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

	'''
	For Для числовых полей чтобы поле было пустым, те не обязательным для заполнения 
	проставляют оба параметра null=True, blank=True,
	для текстовых полей только blank=True
	см в моделе Book
	'''


class Book(models.Model):
	title = models.CharField(max_length=100)
	publication_date = models.DateField(null=True, blank=True)  # тк числовое поле
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, )

	def __str__(self):
		return self.title
