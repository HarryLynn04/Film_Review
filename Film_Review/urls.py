from django.urls import path
from Film_Review import views

app_name = 'ReviewFlix'

urlpatterns = [
    path('', views.home, name='Home'),
    path('faq/', views.faq, name='FAQ'),
    path('register/', views.register, name='Register'),
    path('watchlist/', views.watchlist, name='Watchlist'),
    path('addAMovie/', views.addAMovie, name='AddAMovie'),
    path('genres/', views.genres, name='Genres'),
    path('thriller/', views.thriller, name='Thriller'),
    path('animated/', views.animated, name='Animated'),
    path('comedy/', views.comedy, name='Comedy'),
    path('horror/', views.horror, name='Horror'),
    path('drama/', views.drama, name='Drama'),
    path('documentary/', views.documentary, name='Documentary'),
    path('register/', views.register, name='Register'),
    path('login/', views.user_login, name='Login'),
    path('film/<int:film_id>/', views.individual_film, name='Film'),
    path('film/<int:film_id>/review/', views.review_for_film, name='FilmReview'),


]
