from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse, JsonResponse
from Film_Review.forms import ReviewForm, UserForm, UserProfileForm, FilmForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Film_Review.models import Film, Like, Review, Watchlist
from django.db.models import Avg
from django.contrib import messages




def home(request):
    top_films = Film.objects.annotate(avg_rating=Avg("review__Rating")).order_by("-avg_rating")[:5]
    context_dict= {"top_films": top_films}
    return render(request, 'ReviewFlix/Home.html', context=context_dict)

# Create your views here.
def faq(request):
    context_dict= {}
    return render(request, 'ReviewFlix/FAQ.html', context=context_dict)

@login_required
def watchlist(request):
    watchlist_entries = Watchlist.objects.filter(Username=request.user)
    context_dict= {'watchlist_entries': watchlist_entries}
    return render(request, 'ReviewFlix/Watchlist.html', context=context_dict)


def addAMovie(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('ReviewFlix:Home')) 
    else:
        form = FilmForm()
    return render(request, 'ReviewFlix/AddAMovie.html', {'form': form})


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
            profile.isProducer = profile_form.cleaned_data.get('isProducer', False)
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

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('ReviewFlix:Home'))   
    
def individual_film(request, film_id):
    film = Film.objects.get(id=film_id)
    sort = request.GET.get('sort', '-DatePublished')
    reviews = Review.objects.filter(Film=film).order_by(sort)
    average_rating = reviews.aggregate(Avg('Rating'))['Rating__avg']
    
    context_dict = {'film': film, "reviews": reviews, "average_rating": average_rating}
    return render(request, 'ReviewFlix/Film.html', context=context_dict)   


# @login_required
# def review_for_film(request, film_id):
#     film = Film.objects.get(id=film_id)
#     context_dict = {'film': film}
#     return render(request, 'ReviewFlix/Review.html', context=context_dict) 


@login_required
def review_for_film(request, film_id):
    film = Film.objects.get(id=film_id)
    

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.Film = film
            review.Username = request.user
            review.likes = 0  
            review.DatePublished = timezone.now().date()
            review.save()
            return redirect('ReviewFlix:Film', film_id=film_id) 
    else:
        form = ReviewForm()

    context = {
        'film': film,
        'form': form
    }
    return render(request, 'ReviewFlix/Review.html', context)


@login_required
def add_to_watchlist(request):
    if request.method == 'POST':
        film_id = request.POST.get('film_id')
        user = request.user
        film = Film.objects.get(id=film_id)

        Watchlist.objects.get_or_create(Username=user, Film=film)
        return redirect('ReviewFlix:Film', film_id=film_id)
    else:
        return redirect('ReviewFlix:Home')
    

@login_required
def remove_from_watchlist(request):
    if request.method == 'POST':
        film_id = request.POST.get('film_id')
        user = request.user
        try:
            watchlist_entry = Watchlist.objects.get(Username=user, Film_id=film_id)
            watchlist_entry.delete()
            messages.success(request, "Movie removed from watchlist.")
        except Watchlist.DoesNotExist:
            messages.error(request, "Movie not found in watchlist.")
    return redirect('ReviewFlix:Watchlist')


@login_required
def check_watchlist(request):
    film_id = request.GET.get('film_id')
    user = request.user
    in_watchlist = Watchlist.objects.filter(Username=user, Film_id=film_id).exists()
    return JsonResponse({'in_watchlist': in_watchlist})

def like_review(request):
    if request.method == 'POST' and request.is_ajax():
        review_id = request.POST.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        user = request.user

        if Like.objects.filter(user=user, review=review).exists():
            return JsonResponse({'status': 'error', 'message': 'You have already liked this review.'})
        review.likes += 1
        review.save()

        Like.objects.create(user=user, review=review)

        return JsonResponse({'status': 'success', 'new_likes': review.likes})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})