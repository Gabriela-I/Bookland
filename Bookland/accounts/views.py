from django.contrib.auth import get_user_model, views, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import resolve_url, render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic
from Bookland.accounts.forms import RegisterUserForm, UserEditForm
from Bookland.books.models import Book, Purchase
from django.core.paginator import Paginator

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
        next_url = self.request.POST.get('next', None)
        if next_url:
            try:
                resolve_url(next_url)
            except:
                next_url = None

        if not next_url:
            next_url = self.success_url

        return next_url


class LogoutUserView(LoginRequiredMixin, views.LogoutView):
    next_page = reverse_lazy('login user')


class ProfileDetailsView(generic.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    profile_image = static('images/profile_image.jpg')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        requests = Purchase.objects.filter(seller=self.request.user)
        number_of_items_per_page = 3
        user_books = Book.objects.filter(user=self.request.user).order_by('-id')
        book_paginator = Paginator(user_books, number_of_items_per_page)
        page_number = self.request.GET.get('page')
        books = book_paginator.get_page(page_number)
        page_range = book_paginator.page_range
        context['page_range'] = page_range
        context['profile_image'] = self.get_profile_image()
        context['books'] = books
        context['books_count'] = self.request.user.book_set.count()
        context['request'] = requests

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


def seller_dashboard(request):
    purchase_requests = Purchase.objects.filter(seller=request.user)

    context = {
        'purchase_requests': purchase_requests,
    }
    return render(request, 'accounts/seller_dashboard.html', context)


def accept_request(request, request_pk):
    req = Purchase.objects.get(pk=request_pk)
    book = Book.objects.get(pk=req.book.pk)
    book.delete()
    req.delete()

    return redirect('seller dashboard')


def reject_request(request, request_pk):
    req = Purchase.objects.get(pk=request_pk)
    req.delete()
    return redirect('seller dashboard')

