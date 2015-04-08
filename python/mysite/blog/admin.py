from django.contrib import admin
from .models import Blog, Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	exlude = ['posted']
	prepopulated_fields = {'slug': ('title',)}
	
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)