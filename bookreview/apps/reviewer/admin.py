from django.contrib import admin

# Register your models here.
from .models import User, Author, Book, Review

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)