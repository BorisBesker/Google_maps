from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .forms import UserForm


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
                    return JsonResponse({"message": "Login successful"})
                else:
                    return JsonResponse({"message": "Account disabled"})
            else:
                return JsonResponse({"message": "Invalid credentials"})

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
