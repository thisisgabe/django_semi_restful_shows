from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(req):
    return redirect('/shows')

def show(req, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(req, 'shows/display_show.html', context=context)

def shows(req):
    context = {
        'shows': Show.objects.all()
    }
    return render(req, 'shows/index.html', context=context)

def add_show(req):
    return render(req, 'shows/add_show.html')


def edit_show(req, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(req, 'shows/edit_show.html', context=context)

def update(req, id):
    if not req.POST:
        return HttpResponse('lol, nope')
    new_show = Show.objects.get(id=id)
    new_show.title = req.POST['inputTitle']
    new_show.network = req.POST['inputNetwork']
    new_show.release_date = req.POST['inputReleaseDate']
    new_show.description = req.POST['inputDescription']
    new_show.save()
    return redirect('/shows')

def create(req):
    if not req.POST:
        return HttpResponse('lol, nope')
    new_show = Show.objects.create(
        title=req.POST['inputTitle'], network=req.POST['inputNetwork'], 
        release_date=req.POST['inputReleaseDate'], description=req.POST['inputDescription'])
    return redirect('/shows')

def destroy(req, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')