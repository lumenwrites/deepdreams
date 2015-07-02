from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    return render(request, 'home.html',{
    })
