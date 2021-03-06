from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(
		r'^view/(?P<slug>[\w-]+)/$', 
		views.view_post, 
		name='view_blog_post'),
	url(
		r'^category/(?P<slug>[\w-]+)/$', 
		views.view_category, 
		name='view_blog_category'),
	url(
		r'^archives/',
		views.view_archives,
		name='view_archives'),
	]
	