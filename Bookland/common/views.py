from django.shortcuts import render
from django.views.generic import TemplateView

from Bookland.books.models import Category, Book


# def index(request):
#     return render(request, 'common/index.html')

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


def category(request, cats):
    books = Book.objects.filter(category=cats)
    context = {
        'cats': cats,
        'books': books,
    }
    return render(request, 'categories.html', context)
