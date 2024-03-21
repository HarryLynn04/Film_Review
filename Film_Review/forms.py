from django import forms
from django.contrib.auth.models import User
from Film_Review.models import Review, UserProfile, Film


#Form for user authentication
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password',)
        help_texts = {
            'username': None,
            'password': None,
        }
        
#Form for user profile information
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'isProducer',)
        
#Form for submitting film reviews      
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Rating', 'Description']  
        widgets = {
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Leave your review'}),
            'Rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
        labels = {
            'Rating': 'Your Rating (1-5)',
            'Description': 'Your Review',
        }
        
#Form for adding new films to the database
class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['Title', 'Genre', 'Description', 'ReleaseDate', 'Director', 'Cast', 'image']
