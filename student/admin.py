from django.contrib import admin
from django.utils.html import format_html
from .models import candidate

class candidateAdmin(admin.ModelAdmin):
    list_display = ['admno','name','fname','dob','std','section','image_tag']
    search_fields = ('name','fname')
    ordering =  ('section',)
    list_per_page = 10


    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.photo.url))  #only helpful when media and other information is set in settings.py file
# Register your models here.
admin.site.register(candidate,candidateAdmin)
