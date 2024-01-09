from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm
from transportation.models import Menu

menu = Menu.objects.all()


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация',
                     'menu_items': menu,
                     }


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация',
                     'menu_items': menu,
                     }
    success_url = reverse_lazy('users:login_user')

@login_required
def profile(request):
    data = {
        'title': 'Профиль пользователя',
        'menu_items': menu,
    }
    return render(request, 'users/profile.html', context=data)

# class ProfileUser(LoginRequiredMixin):
#     model = get_user_model()
#     template_name = 'users/profile.html'
#     extra_context = {'title': 'Профиль пользователя',
#                      'menu_items': menu,
#                      }
