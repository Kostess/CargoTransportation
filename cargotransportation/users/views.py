from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm
from transportation.models import Menu, Cargos, Clients

import datetime

menu = Menu.objects.all()
dt = datetime.datetime.now()


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация',
                     'menu_items': menu,
                     'dt': dt
                     }


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация',
                     'menu_items': menu,
                     'dt': dt
                     }
    success_url = reverse_lazy('users:login_user')

@login_required
def profile(request):
    cargo_info = Cargos.objects.filter(status="Не выполнен")
    data = {
        'title': 'Профиль пользователя',
        'menu_items': menu,
        'cargo_info': cargo_info,
        'dt': dt
    }
    return render(request, 'users/profile.html', context=data)

