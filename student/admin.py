from django.contrib import admin
from .models import candidate

class candidateAdmin(admin.ModelAdmin):
    list_display =('admno','name','fname','dob','std','section')
    list_filter = ('std','section')

# Register your models here.
admin.site.register(candidate,candidateAdmin)