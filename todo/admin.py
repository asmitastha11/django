from django.contrib import admin
from .models import Todolist
# Register your models here.
@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ['title','description','is_completed']
    list_editable = ['is_completed']
    list_per_page = 5
    search_fields = ['title']
    list_filter = ['is_completed']
# admin.site.register(Todolist,TodolistAdmin)
    
