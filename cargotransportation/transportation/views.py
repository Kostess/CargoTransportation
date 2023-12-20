from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    menu_items = Menu.objects.all()
    card_three = Cards_orders.objects.all()[:3]
    data = {
        'title': 'Главная',
        'menu_items': menu_items,
        'card_three': card_three,
    }
    return render(request, "transportations/index.html", context=data)

def services(request):
    card_items = Cards_orders.objects.all()
    data = {
        'title': 'Услуги',
        'card_items': card_items,
    }
    return render(request, "transportations/services.html", context=data)

def company(request):
    return render(request, "transportations/company.html")

def service(request, name):
    card_items = get_object_or_404(Cards_orders, slug=name)
    data = {
        'title': card_items.title,
        'card_items': card_items,
    }
    return render(request, "transportations/service.html", context=data)

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