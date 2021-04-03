from unicodedata import category

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from home.models import Setting, ContactFormMessage, ContactFormu
from content.models import Content, Category, Images


def index(request):
    setting = Setting.objects.get()
    sliderdata = Content.objects.all()[:4]
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata':sliderdata}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get()
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)



def referanslar(request):
    setting = Setting.objects.get()
    context = {'setting': setting, 'page': 'referanslar'}
    return render(request, 'referanslar.html', context)



def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajiniz basariyla gonderildi.")
            return HttpResponseRedirect('/iletisim')
    setting = Setting.objects.get()
    form = ContactFormu()
    context = {'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context)

def category_contents(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    contents = Content.objects.filter(category_id=id)
    context = {'contents' : contents,
               'category': category,
               'categorydata' : categorydata
               }
    return render(request, 'content-list.html', context)

def content_detail(request,id,slug):
    category = Category.objects.all()
    content = Content.objects.get(pk=id)
    images = Images.objects.filter(content_id=id)
    context = {'content': content,
               'category': category,
               'images' : images
              }
    return render(request, 'content_detail.html', context)
