from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from account.models import ExtendedUser
from main.models import Work, Version
from main.forms import WorkForm
from django.contrib.auth.models import User
from account.forms import LoginForm, UserCreationFormWithMail
from account.views import empty_register_form, register
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import json, hashlib

import time
# Create your views here.


def login_view(request):
    username = request.POST['username_for_log']
    password = request.POST['password_for_log']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(my_board)
    else:
        invalid_auth = True
        return homepage(request, invalid_auth=True)

def logout_view(request):
    logout(request)
    return redirect('homepage')

def homepage(request, invalid_auth=False):
    if request.user.is_authenticated(): # or 'pseudo' in request.session.keys():
        return my_board(request)
    if invalid_auth:
        form = UserCreationFormWithMail()
        return render(request, 'main/presentation.html', {'form':form, 'invalid_auth':invalid_auth})
    else:
        if request.method == 'POST':  # S'il s'agit d'une requête POST
            form = UserCreationFormWithMail(request.POST)
            # if form.is_valid():
            #     return HttpResponse(form)
            # else:
            #     return HttpResponse('formulaire invalide')
            form, request = register(request, post=True)
            if request.user.is_authenticated():
                return my_board(request)
            return render(request, 'main/presentation.html', {'form':form})
        else: # Si ce n'est pas du POST, c'est probablement une requête GET
            form = empty_register_form()  # Nous créons un formulaire vide
            return render(request, 'main/presentation.html', {'form':form})





@login_required
def my_board(request):
    works = Work.objects.filter(user=request.user)
    contributions = Version.objects.filter(user=request.user)
    contributed_works = Work.objects.filter(version__in=contributions)
    contributed_works = contributed_works.exclude(user=request.user)
    return render(request, 'main/my_board.html', {'works':works, 'contributed_works':contributed_works})

def co_user_1(request):
    user = authenticate(username='max', password='131141520513')
    if user is not None:
        login(request, user)
    return my_board(request)


def co_user_2(request):
    user = authenticate(username='clem', password='131141520513')
    if user is not None:
        login(request, user)
    return my_board(request)


def not_found_error(request):
   return render(request, 'main/not_found_error.html')

# def delete(request, link):
#     work = Work.objects.filter(link=link)[0]
#     user_has_rights = request.user.is_staff() or work.user == request.user
#     if user_has_rights:
#         work.delete()
#     return user_has_rights



