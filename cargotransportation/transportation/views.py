from django.shortcuts import render

def index(request):
    return render(request, "transportations/index.html")

def services(request):
    return render(request, "transportations/services.html")

def company(request):
    return render(request, "transportations/company.html")