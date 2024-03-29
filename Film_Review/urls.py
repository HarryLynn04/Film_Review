from django.urls import path
from Film_Review import views

app_name = 'ReviewFlix'

urlpatterns = [
    path('', views.home, name='Home'),
    path('faq/', views.faq, name='FAQ'),
    path('register/', views.register, name='Register'),
    path('watchlist/', views.watchlist, name='Watchlist'),
    path('add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('check_watchlist/', views.check_watchlist, name='check_watchlist'),
    path('addAMovie/', views.addAMovie, name='AddAMovie'),
    path('genres/', views.genres, name='Genres'),
    path('thriller/', views.thriller, name='Thriller'),
    path('animated/', views.animated, name='Animated'),
    path('comedy/', views.comedy, name='Comedy'),
    path('horror/', views.horror, name='Horror'),
    path('drama/', views.drama, name='Drama'),
    path('documentary/', views.documentary, name='Documentary'),
    path('login/', views.user_login, name='Login'),
    path('logout/', views.user_logout, name='Logout'),
    path('film/<int:film_id>/', views.individual_film, name='Film'),
    path('film/<int:film_id>/review/', views.review_for_film, name='FilmReview'),
    path('like_review/', views.like_review, name='like_review'),
    path('check_like_status/', views.check_like_status, name='check_like_status'),
]
