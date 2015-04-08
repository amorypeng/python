from django.contrib import admin

# Register your models here.
from .models import Question, Choice



class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	('ayy lmao', {'fields': ['question_text']}),
	('date info', {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]
	
admin.site.register(Question, QuestionAdmin)