from django.contrib import admin
from .models import Todo
# Register your models here.

class displayTodo(admin.ModelAdmin):
    list_display = ('title', 'title','completed', 'user')  # Add the fields you want to display in the list view


admin.site.register(Todo, displayTodo)
