from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from Bookland.books.forms import BookAddForm, BuyBookForm, BookEditForm, BookDeleteForm, BookCommentForm, PurchaseForm
from Bookland.books.models import Book, BookComment, Purchase
from Bookland.books.utils import has_user_marked_book, get_comment_url
from Bookland.books.models import MyList
from django.contrib import messages

@login_required
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
    has_marked = False
    comments = book.bookcomment_set.all()
    if request.user.is_authenticated:
        has_marked = has_user_marked_book(book_pk, request.user)
    context = {
        'book': book,
        'has_marked': has_marked,
        'comments': comments,
    }
    return render(request, 'books/book-details.html', context)


@login_required
def book_edit(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()
    if request.user != book.user:
        return redirect('book details', book_pk=book.pk)

    if request.method == 'POST':
        form = BookEditForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book details', book_pk=book.pk)
    else:
        form = BookEditForm(instance=book)

    context = {
        'form': form,
        'book_pk': book.pk,
    }

    return render(request, 'books/book-edit.html', context)


@login_required
def book_delete(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()
    if request.user != book.user:
        return redirect('book details', book_pk=book.pk)

    if request.method == 'POST':
        form = BookDeleteForm(request.POST, instance=book)
        book.delete()
        return redirect('book details', book_pk=book.pk)
    else:
        form = BookDeleteForm(instance=book)

    context = {
        'form': form,
        'book_pk': book.pk,
    }

    return render(request, 'books/book-delete.html', context)




@login_required
def buy_book(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()

    if request.method == 'POST':
        form = BuyBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('finish purchase', book_pk=book_pk)
    else:
        form = BuyBookForm(instance=book)

    context = {
        'form': form,
        'book_pk': book_pk,
        'book': book,
    }

    return render(request, 'books/buy_book.html', context)

@login_required
def finish_purchase(request, book_pk):
    book = Book.objects.get(pk=book_pk)

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.buyer = request.user
            purchase.seller = book.user
            purchase.book = book
            purchase.save()
            return redirect('completed order')
    else:
        form = PurchaseForm()

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'books/finish_purchase.html', context)





def completed_order(request):
    return render(request, 'books/completed_order.html')


@login_required
def my_list(request, book_pk):
    book = Book.objects.get(pk=book_pk)

    bookmark = MyList(
        book=book,
        user=request.user,
    )
    bookmark.save()

    return redirect('book details', book_pk=book_pk)


def my_list_details(request):
    user = request.user
    my_list_entries = MyList.objects.filter(user=user)
    book_ids = my_list_entries.values_list('book_id', flat=True)
    books = Book.objects.filter(pk__in=book_ids)

    book_paginator = Paginator(books, 8)
    page = request.GET.get('page')
    books_paginated = book_paginator.get_page(page)
    page_range = book_paginator.page_range

    context = {
        'books': books_paginated,
        'page_range': page_range,
    }

    return render(request, 'books/my_list_details.html', context)


def remove_from_my_list(request, book_pk):
    my_list_entry = MyList.objects.get(book_id=book_pk, user=request.user)
    my_list_entry.delete()

    return redirect('book details', book_pk=book_pk)


@login_required
def book_comment(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()

    if request.method == 'POST':
        form = BookCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.user = request.user
            comment.save()

            comment_id = comment.id
            return redirect(get_comment_url(book_pk))
    else:
        form = BookCommentForm()

    comments = BookComment.objects.filter(book=book)
    context = {
        'book': book,
        'form': form,
        'comments': comments,
    }
    return render(request, 'books/book-details.html', context)


