#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from main.models import Work, Version
from main.forms import VersionForm
import random
from django.contrib.auth.decorators import login_required

@login_required
def contribute(request):
    return choose_text(request)


@login_required
def choose_text(request):
    non_author_works = Work.objects.exclude(user=request.user) # Tous les works pas de l'user, où il n'existe pas de version de l'user
    contributions = Version.objects.filter(user=request.user)
    contribuable_works = non_author_works.exclude(version__in=contributions)
    lack_of_works = max(3 - len(contribuable_works), 0)
    three_random_contribuable_works = random.sample(list(contribuable_works), 3) if lack_of_works == 0 else contribuable_works
    return render(request, 'contribute/choose_text.html', {'works':three_random_contribuable_works, 'lack_of_works':lack_of_works})

@login_required
def edit(request, link):
    work = Work.objects.filter(link=link)[0]
    versions = Version.objects.filter(work=work)

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        version_form = VersionForm(request.POST)  # Nous reprenons les données
        version = version_form.save(commit=False)
        version.user = request.user
        version.work = work
        work.save()
        version.save()
        return redirect('consult', link)
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        version_form = VersionForm()  # Nous créons un formulaire vide
        return render(request, 'contribute/edit.html', {'work':work, 'versions':versions, 'version_form':version_form})




