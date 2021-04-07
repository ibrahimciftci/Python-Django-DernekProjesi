import json
from unicodedata import category

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from home.models import Setting, ContactFormMessage, ContactFormu, UserProfile
from content.models import Content, Category, Images, Comment
from home.forms import SearchForm, SignUpForm


def index(request):
    setting = Setting.objects.get()
    sliderdata = Content.objects.all()[:4]
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata}
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


def category_contents(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    contents = Content.objects.filter(category_id=id)
    context = {'contents': contents,
               'category': category,
               'categorydata': categorydata
               }
    return render(request, 'content-list.html', context)


def content_detail(request, id, slug):
    category = Category.objects.all()
    content = Content.objects.get(pk=id)
    images = Images.objects.filter(content_id=id)
    comments = Comment.objects.filter(content_id=id, status='True')
    context = {'content': content,
               'category': category,
               'images': images,
               'comments': comments,
               }
    return render(request, 'content_detail.html', context)


def content_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                contents = Content.objects.filter(title__icontains=query, )
            else:
                contents = Content.objects.filter(title__icontains=query, category_id=catid)
            context = {'contents': contents,
                       'category': category,
                       }
            return render(request, 'contents_search.html', context)
    return HttpResponseRedirect('/')


def content_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        content = Content.objects.filter(title__icontains=q)
        results = []
        for rs in content:
            content_json = {}
            content_json = rs.title
            results.append(content_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Giriş Yapılamadı. Kullanıcı adı veya Parola hatalı!")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.jpg"
            data.save()
            messages.success(request, "Üye Kaydınız Başarıyla Gerçekleşmiştir.")
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'signup.html', context)
