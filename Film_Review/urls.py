from django.urls import path
from Film_Review import views

app_name = 'ReviewFlix'

urlpatterns = [
    path('', views.home, name='Home'),
    path('faq/', views.faq, name='FAQ'),
    path('login/', views.login, name='Login'),
    path('register/', views.register, name='Register'),
    path('watchlist/', views.watchlist, name='Watchlist'),
    path('addAMovie/', views.addAMovie, name='AddAMovie'),
    
]
