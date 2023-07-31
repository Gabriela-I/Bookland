from django.shortcuts import render, redirect, get_object_or_404

from Bookland.books.forms import BookAddForm, BuyBookForm
from Bookland.books.models import Book


def category(request, cats):
    books = Book.objects.filter(category=cats)
    context = {
        'cats': cats,
        'books': books,
    }
    return render(request, 'categories.html', context)


def add_book(request):
    if request.method == 'GET':
        form = BookAddForm()
    else:
        form = BookAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('details user', pk=book.user.pk)

    context = {
        'form': form,
    }
    return render(request, 'books/add-book.html', context)


def book_details(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()
    context = {
        'book': book,
    }
    return render(request, 'books/book-details.html', context)


def book_edit(request, book_pk):
    ...


def book_delete(request, book_pk):
    ...


def buy_book(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()

    if request.method == 'POST':
        form = BuyBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            book.delete()
            return redirect('completed order')
    else:
        form = BuyBookForm(instance=book)

    context = {
        'form': form,
        'book_pk': book_pk,
        'book': book,
    }

    return render(request, 'books/buy_book.html', context)


def completed_order(request):
    return render(request, 'books/completed_order.html')