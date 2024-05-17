from django.contrib import admin
from .models import *
# Register your models here.

from django.contrib import admin
from .models import Language

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language',)


class what_you_will_learn_TabularInline(admin.TabularInline):
    model = what_you_will_learn

class Requirements_TabularInline(admin.TabularInline):
    model = Requirements

class Video_TabularInline(admin.TabularInline):
    model = Video

class course_admin(admin.ModelAdmin):
    inlines = (what_you_will_learn_TabularInline,Requirements_TabularInline,Video_TabularInline)


admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course,course_admin)
admin.site.register(Level)
admin.site.register(what_you_will_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)