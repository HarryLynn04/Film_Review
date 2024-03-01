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

def genres(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Genres.html', context=context_dict)

def thriller(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Thriller.html', context=context_dict) 

def animated(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Animated.html', context=context_dict)  

def comedy(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Comedy.html', context=context_dict)   

def horror(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Horror.html', context=context_dict)     

def drama(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Drama.html', context=context_dict)                                         

def documentary(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Documentary.html', context=context_dict)                                                                                                 