from django.urls import path
from Bookland.common.views import IndexView, category

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('category/<str:cats>/', category, name='category'),
)
