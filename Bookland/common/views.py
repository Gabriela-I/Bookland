from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from Bookland.books.models import Book



class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        last_3_books = Book.objects.order_by('-upload_date')[:3]
        cat_menu = [
            'Romance', 'Fantasy', 'Criminal',
            'Historical novel', 'Thriller', 'Science fiction',
            'Poetry', 'Health',
            'Psychology', 'Esoteric', 'Home, Family, Hobby',
            'Children\'s literature', 'Other',
        ]

        context = super().get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        context['last_3_books'] = last_3_books
        return context


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        book_paginator = Paginator(Book.objects.filter(title__contains=searched), 8)
        page = request.GET.get('page')
        books = book_paginator.get_page(page)
        page_range = book_paginator.page_range
        if len(books) == 0:
            pattern = searched
            searched = None
            context = {
                'searched': searched,
                'pattern': pattern,
            }
            return render(request, 'common/search.html', context)
        else:
            context = {
                'books': books,
                'searched': searched,
                'page_range': page_range,
            }
            return render(request, 'common/search.html', context)
    else:
        return render(request, 'common/search.html')


def category(request, cats):
    book_paginator = Paginator(Book.objects.filter(category=cats), 8)
    page = request.GET.get('page')
    books = book_paginator.get_page(page)
    page_range = book_paginator.page_range
    context = {
        'cats': cats,
        'books': books,
        'page_range': page_range,
    }
    return render(request, 'common/categories.html', context)

