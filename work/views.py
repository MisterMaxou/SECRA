#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from main.models import Version, Work
from main.forms import WorkForm, VersionForm
from django.contrib.auth.decorators import login_required

@login_required
def drop(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        version_form = VersionForm(request.POST)  # Nous reprenons les données
        work_form = WorkForm(request.POST)  # Nous reprenons les données
        if version_form.is_valid():
            work = work_form.save(commit=False)
            work.user = request.user
            work.save()

            version = version_form.save(commit=False)
            version.user = request.user
            version.work = work
            version.save()
        else:
            return HttpResponse(version_form.errors['text'])
        return redirect('/')

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        work_form = WorkForm()  # Nous créons un formulaire vide
        version_form = VersionForm()  # Nous créons un formulaire vide
        return render(request, 'work/drop.html', locals())


@login_required
def edit(request, link):
    user = request.user
    instance = Work.objects.get(link=link)
    if not request.user == instance.user:
        return redirect('/')
    form = WorkForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return render(request, 'work/edit.html', {'form':form, 'edit':True, 'link':link}) # redirect('/account/')
    return render(request, 'work/edit.html', {'form':form, 'edit':False,'link':link})


# def consult(request, link):
#     work = Work.objects.filter(link=link)[0]
#     # user_has_rights = request.user.is_staff() | work.user == request.user
#     versions = list(Version.objects.filter(work=work))
#     length = len(versions)
#     versions = enumerate(versions)
#     return render(request, 'work/consult.html', {'work':work, 'versions':versions, 'length':length})


def render_versions(request, link):
    work = Work.objects.filter(link=link)[0]
    # user_has_rights = request.user.is_staff() | work.user == request.user
    versions = list(Version.objects.filter(work=work))
    length = len(versions)
    participated = versions[-1].user != work.user
    versions = enumerate(versions)
    return render(request, 'work/render_versions.html', {'work':work, 'versions':versions, 'length':length, 'participated':participated})


def consult(request, link):
    view_of_versions = render_versions(request, link)
    return render(request, 'work/consult.html', {'view_of_versions':view_of_versions})


