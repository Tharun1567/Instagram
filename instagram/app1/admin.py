from django.contrib import admin
from app1.models import Author,Book

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)