from tkinter import Image

from django.contrib import admin
from blogs.models import *

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "author", "created_at", "updated_at","status","is_featured"]
    search_fields = ["title","category__category_name"]
    list_editable = ["is_featured"]
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name","created_at","updated_at"]
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog,BlogAdmin)