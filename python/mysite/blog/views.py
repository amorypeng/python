from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import time
from calendar import month_name
from .models import Blog, Category

# Create your views here.
def index(request):
	categories = Category.objects.all().order_by('title')
	post_list = Blog.objects.all()[::-1]
	print(post_list)
	paginator = Paginator(post_list, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(pageinator.num_pages)
		
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
		'posts': Blog.objects.filter(category=category),
	})
			

def view_archives(request):
	posts = Blog.objects.all().order_by('posted')[::-1]
	first = posts[0].posted
		
	return render_to_response('blog/view_archives.html', {
		'posts': posts,
	})