from django.contrib import admin
from django.utils.html import format_html
from .models import candidate

class candidateAdmin(admin.ModelAdmin):
    list_display = ['admno','name','fname','dob','std','section','image_tag']
    search_fields = ('name','fname')
    ordering =  ('section',)
    list_per_page = 15


    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.photo.url))
# Register your models here.
admin.site.register(candidate,candidateAdmin)
