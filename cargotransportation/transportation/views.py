from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.mail import send_mail

pages = [
    {'title': 'Услгуи', 'description': 'Весь список услуг, предоставляемый нашей компанией'},
    {'title': 'О компании', 'description': 'Вся необходимая информация про компанию ТрансГруз'},
]

menu_items = Menu.objects.all()
type_transporations_item = Type_transporation.objects.all()
def index(request):
    card_three = Cards_orders.objects.all()[:3]
    data = {
        'title': 'ТрансГруз',
        'menu_items': menu_items,
        'card_three': card_three,
        'type_transporations_item': type_transporations_item,
    }
    return render(request, "transportations/index.html", context=data)

def services(request):
    card_items = Cards_orders.objects.all()
    data = {
        'title': 'Услуги',
        'card_items': card_items,
        'menu_items': menu_items,
        'page_des': pages[0],
    }
    return render(request, "transportations/services.html", context=data)

def company(request):
    data = {
        'title': 'О компании',
        'menu_items': menu_items,
        'page_des': pages[1],
    }
    return render(request, "transportations/company.html", context=data)

#@login_required
def service(request, name):
    card_items = get_object_or_404(Cards_orders, slug=name)
    data = {
        'title': card_items.title,
        'card_items': card_items,
        'menu_items': menu_items,
        'type_transporations_item': type_transporations_item,
    }
    return render(request, "transportations/service.html", context=data)

def success(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        tel = request.POST.get('tel', '')

        data = f"Имя: {name}\nEmail: {email}\nТел: {tel}"

        send_mail('С вами хотят связаться', data, "Sender", ['qaz1234567890838@gmail.com'],
                      fail_silently=False)
    data = {
        'title': 'Отправлено',
        'menu_items': menu_items,
    }
    return render(request, 'transportations/success.html', context=data)

#404
def pageNotFound(request, exception):
    return render(request, "transportations/404.html")

#500
def errorServer(request):
    return render(request, "transportations/500.html")

#400
def accessDenied(request, exception):
    return HttpResponseBadRequest('<h1>Доступ запрещен</h1>')

#403
def unableToProcessRequest(request, exception):
    return HttpResponseForbidden('<h1>Невозможно обработать запрос</h1>')