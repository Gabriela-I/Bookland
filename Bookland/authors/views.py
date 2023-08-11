from django.core.paginator import Paginator
from django.shortcuts import render

from Bookland.authors.models import Author
from Bookland.books.models import Book


def author_books(request, author_name):
    book_paginator = Paginator(Book.objects.filter(author=author_name), 8)
    page = request.GET.get('page')
    books = book_paginator.get_page(page)
    page_range = book_paginator.page_range
    context = {
        'books': books,
        'author_name': author_name,
        'page_range': page_range,
    }
    return render(request, 'author/author_books.html', context)


def author_list(request):
    all_books = Book.objects.all()
    authors = all_books.values_list('author', flat=True).distinct().order_by('author')
    print(authors)
    return render(request, 'author/author_list.html', {'authors': authors})
# user = request.user
#     my_list_entries = MyList.objects.filter(user=user)
#     book_ids = my_list_entries.values_list('book_id', flat=True)
#     books = Book.objects.filter(pk__in=book_ids)
