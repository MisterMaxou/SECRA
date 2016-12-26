#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render


def aboutus(request):
    return render(request, 'aboutus/aboutus.html')