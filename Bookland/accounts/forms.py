from django.contrib.auth import forms, get_user_model
from django import forms as model_forms

from Bookland.accounts.models import BooklandUser

UserModel = get_user_model()

GENDER = [
    ('', '------'),
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]


class RegisterUserForm(forms.UserCreationForm):
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2',)


class UserEditForm(model_forms.ModelForm):
    gender = model_forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = UserModel
        fields = (
        'username', 'first_name', 'last_name', 'profile_picture', 'gender', 'phone_number', 'address', 'email')
        labels = {'username': 'Username:',
                  'first_name': 'First Name:',
                  'last_name': 'Last Name:',
                  'email': 'Email:',
                  'profile_picture': 'Image:',
                  'address': 'Address:',
                  'phone_number': 'Phone number:',
                  'gender': 'Gender:',
                  }
