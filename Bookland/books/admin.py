from django.contrib import admin

from Bookland.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    ordering = ('-upload_date',)
    list_filter = ('category', 'author',)
    list_display = ('title', 'author', 'category', 'price')
    date_hierarchy = 'upload_date'
