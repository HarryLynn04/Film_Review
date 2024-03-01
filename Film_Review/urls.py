from django.urls import path
from Film_Review import views

app_name = 'ReviewFlix'

urlpatterns = [
    path('', views.home, name='Home'),
]
