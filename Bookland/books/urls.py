from django.urls import path, include

from Bookland.books.views import add_book, book_details, book_edit, book_delete, category, buy_book, completed_order

urlpatterns = (
    path('add/', add_book, name='book add'),
    path('book/<int:book_pk>/', include([
        path('', book_details, name='book details'),
        path('edit/', book_edit, name='book edit'),
        path('delete/', book_delete, name='book delete'),
        path('buy/', buy_book, name='book buy'),
    ])),
    path('completed_order/', completed_order, name='completed order'),
)