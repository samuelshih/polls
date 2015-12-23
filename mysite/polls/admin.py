from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# This allows choice objects to be edited on the Question admin page
class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3 # provide enough fields for 3 choices

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 								{'fields': ['question_text']}),
		('Date information', 	{'fields': ['pub_date']}),
	]
	inlines = [ChoiceInLine]
	# list_display admin option, tuple of filed names to display as columns
	# on the change list page for this objects
	# if this is not present, Django displays the __str()__ of feach object
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)