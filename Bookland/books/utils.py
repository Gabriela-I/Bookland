from django.urls import reverse

from Bookland.books.models import MyList


def has_user_marked_book(book_pk, user):
    return MyList.objects.filter(book_id=book_pk, user=user).first()


def get_comment_url(book_pk,):
    return reverse('book details', kwargs={'book_pk': book_pk}) + f'#comment-here'