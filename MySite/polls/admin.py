from django.contrib import admin
from polls.models import Choice, Question


class ChoiceInline(admin.TabularInline):  # StackedInline for line by line
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ('Question Details', {'fields': ['Description']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
