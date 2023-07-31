from django.urls import path, include

from Bookland.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, ProfileDetailsView, \
    ProfileDeleteView, ProfileEditView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login user'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('delete/', ProfileDeleteView.as_view(), name='delete user'),
        path('edit/', ProfileEditView.as_view(), name='edit user'),
        path('', ProfileDetailsView.as_view(), name='details user'),
    ])),

)
