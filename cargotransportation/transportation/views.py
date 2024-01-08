from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .models import *

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
    }
    return render(request, "transportations/services.html", context=data)

def company(request):
    data = {
        'title': 'О компании',
        'menu_items': menu_items,
    }
    return render(request, "transportations/company.html", context=data)

def service(request, name):
    card_items = get_object_or_404(Cards_orders, slug=name)
    data = {
        'title': card_items.title,
        'card_items': card_items,
        'menu_items': menu_items,
        'type_transporations_item': type_transporations_item,
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