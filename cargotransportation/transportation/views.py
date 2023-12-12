from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render

def index(request):
    return render(request, "transportations/index.html")

def services(request):
    return renders(request, "transportations/services.html")

def company(request):
    return render(request, "transportations/company.html")

def service(request):
    return render(request, "transportations/service.html")

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