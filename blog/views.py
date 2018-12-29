from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})


# def post_new(request):
# 	form = PostForm()
# 	return render(request, 'blog/post_edit.html', {'form': form})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})


# class based views instead  def post_new(request):
class PostCreate(CreateView):
	model = Post
	fields = '__all__'
	success_url = reverse_lazy('blog:post_list')


class PostUpdate(PermissionRequiredMixin, UpdateView):
	model = Post
	fields = '__all__'
	success_url = reverse_lazy('blog:post_list')
	permission_required = 'catalog.can_mark_returned'


class PostDelete(PermissionRequiredMixin, DeleteView):
	model = Post
	fields = '__all__'
	success_url = reverse_lazy('blog:post_list')
	permission_required = 'catalog.can_mark_returned'
