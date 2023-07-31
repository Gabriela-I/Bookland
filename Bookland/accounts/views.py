from django.contrib.auth import get_user_model, views, login
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic

from Bookland.accounts.forms import RegisterUserForm, UserEditForm
from Bookland.accounts.models import BooklandUser
from Bookland.books.models import Category

UserModel = get_user_model()


class LoginUserView(views.LoginView):
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')


class RegisterUserView(generic.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LogoutUserView(LoginRequiredMixin, views.LogoutView):
    next_page = reverse_lazy('login user')


class ProfileDetailsView(generic.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    profile_image = static('images/default-person-image.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['profile_image'] = self.get_profile_image()
        context['books'] = self.request.user.book_set.all()
        context['cat_menu'] = cat_menu

        return context


class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.object.pk})


class ProfileDeleteView(generic.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('login user')


