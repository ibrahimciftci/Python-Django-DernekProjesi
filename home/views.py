
from django.shortcuts import render


def index(request):
    text = "Bilgisayar Mühendisliği"
    context = {'text' : text}
    return render(request, 'index.html', context)

