from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Bookland.common.urls')),
    path('accounts/', include('Bookland.accounts.urls')),
    path('books/', include('Bookland.books.urls')),
    path('authors/', include('Bookland.authors.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)