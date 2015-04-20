from django.db import models
from django.db.models import permalink
# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['title']
		
class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	author = models.CharField(max_length=100, default='yolo')
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ManyToManyField(Category)
	def __str__(self):
		return self.title
	
	

