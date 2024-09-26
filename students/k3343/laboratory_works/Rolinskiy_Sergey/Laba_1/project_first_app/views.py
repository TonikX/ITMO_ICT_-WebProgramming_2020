from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from project_first_app.models import *
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def review(request,ho_id):
    post = Hotel.objects.get(pk=ho_id)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    try:
        hotell=Hotel.objects.get(pk=ho_id)
    except Hotel.DoesNotExist:
        raise Http404("Hotel does not exist")
    return render(request,'review.html',
                  {"hotel":hotell,'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})

def main(request):
    context = {}
    context["dataset"] = Hotel.objects.all()
    return render(request, "main.html", context)

def log_in(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def createowner(request):
    context = {}
    form = RegistrationForm(
        request.POST or None)
    if form.is_valid():
        form.save()
        new_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        new_user.username = username
        new_user.set_password(password)
        new_user.last_name = last_name
        new_user.email = email
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect('/main')
    context['form'] = form
    return render(request, "reg.html", context)

'''def post_detail(request, year, month, day, post):
    post = get_object_or_404(Hotel, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # Список активных комментариев к этой записи
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # Комментарий был опубликован
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создайте объект Comment, но пока не сохраняйте в базу данных
            new_comment = comment_form.save(commit=False)
            # Назначить текущий пост комментарию
            new_comment.post = post
            # Сохранить комментарий в базе данных
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'review.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})'''