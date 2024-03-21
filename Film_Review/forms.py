from django import forms
from django.contrib.auth.models import User
from Film_Review.models import Review, UserProfile, Film


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password',)
        help_texts = {
            'username': None,
            'password': None,
        }
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'isProducer',)

        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Rating', 'Description']  
        widgets = {
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Leave your comment about the film'}),
            'Rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
        labels = {
            'Rating': 'Your Rating',
            'Description': 'Your Review',
        }
        

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['Title', 'Genre', 'Description', 'ReleaseDate', 'Director', 'Cast', 'image']
