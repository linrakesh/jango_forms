from django.contrib import admin
from .models import candidate

class candidateAdmin(admin.ModelAdmin):
    list_display =('admno','name','fname','dob','std','section')
    list_filter = ('std','section')
    search_fields = ('name','fname')
    ordering =  ('section',)
    list_per_page = 3

# Register your models here.
admin.site.register(candidate,candidateAdmin)