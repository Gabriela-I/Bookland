from django.urls import path

from Bookland.authors.views import author_books, author_list

urlpatterns = (
    path('<str:author_name>/', author_books, name='author books'),
    path('author_list/', author_list, name='author list'),
)