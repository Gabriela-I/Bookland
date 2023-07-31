from django.contrib.auth import forms, get_user_model
from django import forms as model_forms

from Bookland.accounts.models import BooklandUser

UserModel = get_user_model()


class RegisterUserForm(forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2',)


class UserEditForm(model_forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'profile_picture', 'gender', 'phone_number', 'address', 'email')
        labels = {'username': 'Username:',
                  'first_name': 'First Name:',
                  'last_name': 'Last Name:',
                  'email': 'Email:',
                  'profile_picture': 'Image:',
                  'address': 'Address:',
                  'phone_number': 'Phone number:',
                  'gender': 'Gender:',
                  }
