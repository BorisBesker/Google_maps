from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


def index(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/welcome/')

    return render(request, 'accounts/index.html')


def login_view(request):

    form = UserForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/welcome/')
                else:
                    return HttpResponse("Your account has been disabled")
            else:
                return HttpResponse("Ivalid credentialess")

    if request.user.is_authenticated():
        return HttpResponseRedirect('/welcome/')

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/')


@login_required
def welcome(request):

    return render(request, 'accounts/welcome.html')


def register(request):

    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

    if request.user.is_authenticated():
        return HttpResponseRedirect('/welcome/')

    return render(request, 'accounts/register.html', {'form': form})















