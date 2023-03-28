from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ['title', 'date_created', 'date_updated']


admin.site.register(Post, PostAdmin)
admin.site.register(Portal)
