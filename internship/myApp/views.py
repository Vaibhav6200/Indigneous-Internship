from django.shortcuts import render
from .models import Asgard


def index(request):
    obj = Asgard.objects.all()[0]
    return render(request, 'index.html', {'asgard': obj})