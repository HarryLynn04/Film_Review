from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Home.html', context=context_dict)

# Create your views here.
def faq(request):
    context_dict= {}
    return render(request, 'ReviewFlix/FAQ.html', context=context_dict)

def login(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Login.html', context=context_dict)

def register(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Register.html', context=context_dict)

def watchlist(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Watchlist.html', context=context_dict)

def addAMovie(request):
    context_dict= {}
    return render(request, 'ReviewFlix/AddAMovie.html', context=context_dict)   