from django.contrib import admin
from .models import Choice, Question
from .models import Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


