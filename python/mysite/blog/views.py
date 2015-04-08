from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from .models import Blog, Category

# Create your views here.
def index(request):
	categories = Category.objects.all()
	posts = Blog.objects.all()[:5]
	context = {'categories': categories, 'posts':posts, }
	return render_to_response('blog/index.html', context)

	
def view_post(request, slug):
	return render_to_response('blog/view_post.html', {
		'post': get_object_or_404(Blog, slug=slug)
	})
	
def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('blog/view_category.html', {
		'category': category,
		'posts': Blog.objects.filter(category=category)[:5],
	})
			
		