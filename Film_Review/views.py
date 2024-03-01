from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Home.html', context=context_dict)

# Create your views here.
