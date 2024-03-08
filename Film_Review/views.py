from django.shortcuts import render
from django.http import HttpResponse
from Film_Review.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from Film_Review.models import Film



def home(request):
    context_dict= {}
    return render(request, 'ReviewFlix/Home.html', context=context_dict)

# Create your views here.
def faq(request):
    context_dict= {}
    return render(request, 'ReviewFlix/FAQ.html', context=context_dict)

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
    films = Film.objects.filter(Genre='thriller')
    context_dict= {'films': films}
    return render(request, 'ReviewFlix/Thriller.html', context=context_dict) 

def animated(request):
    films = Film.objects.filter(Genre='animated')
    context_dict= {'films': films}
    return render(request, 'ReviewFlix/Animated.html', context=context_dict)  

def comedy(request):
    films = Film.objects.filter(Genre='comedy')
    context_dict= {'films': films}
    return render(request, 'ReviewFlix/Comedy.html', context=context_dict)   

def horror(request):
    films = Film.objects.filter(Genre='horror')
    context_dict= {'films': films}
    return render(request, 'ReviewFlix/Horror.html', context=context_dict)     

def drama(request):
    films = Film.objects.filter(Genre='drama')
    context_dict= {'films': films}
    return render(request, 'ReviewFlix/Drama.html', context=context_dict)                                         

def documentary(request):
    films = Film.objects.filter(Genre='documentary')
    context_dict= {'films': films}
    return render(request, 'ReviewFlix/Documentary.html', context=context_dict)  

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.firstName = profile_form.cleaned_data['firstName']
            profile.lastName = profile_form.cleaned_data['lastName']
            profile.isProducer = user_form.cleaned_data.get('isProducer', False)
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'ReviewFlix/Register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form, 
                           'registered': registered}) 

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('ReviewFlix:Home'))
            else:
                return HttpResponse("Your ReviewFlix account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'ReviewFlix/Login.html')     
    
def individual_film(request, film_id):
    film = Film.objects.get(id=film_id)
    context_dict = {'film': film}
    return render(request, 'ReviewFlix/Film.html', context=context_dict)                                                                                        