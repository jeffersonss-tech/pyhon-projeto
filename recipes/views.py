from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'jefferson',
    })


def sobre(request):
    return render(request, 'me_apague/temp.html')


def contato(request):
    return HttpResponse('contato')
