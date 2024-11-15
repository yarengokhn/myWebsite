from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from user.forms import LoginForm, RegisterForm


# Create your views here.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Oturum Açma Başarılı')
                return HttpResponseRedirect('/user/login')
            else:
                messages.error(request, 'Oturum Açma Başarısız')
                return HttpResponseRedirect('/user/login')

    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username').lower()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Kayıt Başarılı')
                return HttpResponseRedirect('/user/register')
            else:
                messages.error(request, 'Kayıt Başarısız')
                return HttpResponseRedirect('/user/register')
    form = RegisterForm
    context = {'form': form}
    return render(request, 'register.html', context)