from django.contrib import admin

from Bookland.books.models import Book, BookComment, Purchase


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    ordering = ('-upload_date',)
    list_filter = ('category', 'author',)
    list_display = ('title', 'author', 'category', 'price')
    date_hierarchy = 'upload_date'


@admin.register(BookComment)
class BookCommentAdmin(admin.ModelAdmin):
    ...


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    ...