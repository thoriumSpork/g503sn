from django.contrib import admin

# Register your models here.
from .models import SerialNumbers

class SerialNumbersAdmin(admin.ModelAdmin):
    list_display = ('xserialnumber','xlastname')
    sortable_by = ('xserialnumber')
    list_filter = ('xmodel','xlastname')

admin.site.register(SerialNumbers,SerialNumbersAdmin)