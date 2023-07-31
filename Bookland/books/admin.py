from django.contrib import admin

from Bookland.books.models import Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...
