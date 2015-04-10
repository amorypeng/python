from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Blog, Category

# Create your views here.
def index(request):
	categories = Category.objects.all().order_by('title')
	posts = Blog.objects.all()[:5:-1]
	context = {'categories': categories, 'posts':posts, }
	return render_to_response('blog/index.html', context)

	
def view_post(request, slug):
	post = get_object_or_404(Blog, slug=slug)
	try:
		previous_post = Blog.get_previous_by_posted(post)
	except ObjectDoesNotExist:
		previous_post = None
	try:
		next_post = Blog.get_next_by_posted(post)
	except ObjectDoesNotExist:
		next_post = None
	context = {
		'post':post, 
		'previous_post':previous_post,
		'next_post':next_post,
	}
	return render_to_response('blog/view_post.html', context)
	
def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('blog/view_category.html', {
		'category': category,
		'posts': Blog.objects.filter(category=category)[:5],
	})
			
		