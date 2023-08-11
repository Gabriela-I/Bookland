from django.urls import path, include

from Bookland.books.views import add_book, book_details, book_edit, book_delete, buy_book, completed_order, my_list, \
    my_list_details, remove_from_my_list, book_comment, finish_purchase

urlpatterns = (
    path('add/', add_book, name='book add'),
    path('book/<int:book_pk>/', include([
        path('', book_details, name='book details'),
        path('edit/', book_edit, name='book edit'),
        path('delete/', book_delete, name='book delete'),
        path('buy/', buy_book, name='book buy'),
        path('finish_purchase/', finish_purchase, name='finish purchase'),
        path('bookmark/', my_list, name='bookmark'),
        path('remove/', remove_from_my_list, name='remove from my list'),
        path('comment/', book_comment, name='book comment'),

    ])),
    path('my_list/', my_list_details, name='my list details'),
    path('completed_order/', completed_order, name='completed order'),
)

