#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from account.models import ExtendedUser
from account.forms import AutoUserForm, UserCreationFormWithMail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def manage(request):
    if not request.user.is_authenticated():
        return redirect('/')
    user = request.user
    instance = ExtendedUser.objects.get(user=user)
    form = AutoUserForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return render(request, 'account/manage_account.html', {'form':form, 'edit':True}) # redirect('/account/')
    return render(request, 'account/manage_account.html', {'form':form, 'edit':False})


# def log_with_pseudo(request, username):
#     if isRegistered(username):
#         return redirect('pseudodejaexistant')
#     else:
#         user = User()
#         user.username = username
#         # user.email = 'badmail@bllllllllllllllll.com'
#         # user.first_name = 'illustre'
#         # user.last_name = 'inconnu'

#         user.set_password(username)
#         user.save()
#         extended_user = ExtendedUser(user=user)
#         extended_user.save()
#         user = authenticate(username=username, password=username)
#         login(request, user)

#     return redirect('my board')

def register(request, post):
    form = UserCreationFormWithMail(request.POST)  # Nous reprenons les données
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = form.save(commit=True)
        extended_user = ExtendedUser(user=user)
        extended_user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return form, request
    return form, request




def empty_register_form():
    return UserCreationFormWithMail()

