from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Film(models.Model):
    GENRES = [
        ('animated', 'Animated'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('documentary', 'Documentary'),
        ('horror', 'Horror'),
        ('thriller', 'Thriller'),
    ]
    Title = models.CharField(max_length=100)
    Genre = models.CharField(max_length=20, choices=GENRES)
    Description = models.CharField(max_length=1000)
    ReleaseDate = models.DateField()
    Director = models.CharField(max_length=50)
    Cast = models.CharField(max_length=100)
    image = models.ImageField(upload_to='film_images/', null=True, blank=True)
    
    def __str__(self):
        return self.Title
    
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30,blank=True)
    lastName = models.CharField(max_length=150,blank=True)
    email = models.EmailField()
    isProducer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    
class Review(models.Model):
    RATINGS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    Rating = models.IntegerField(choices=RATINGS)
    Likes = models.IntegerField()
    DatePublished = models.DateField()
    Description = models.CharField(max_length=1000)
    Film = models.ForeignKey(Film, on_delete=models.CASCADE)
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    