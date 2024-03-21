from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Film, Review, Like, Watchlist
from django.urls import reverse

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.film = Film.objects.create(
            Title='Test Film',
            Genre='comedy',
            Description='This is a test film description.',
            ReleaseDate=timezone.now(),
            Director='Test Director',
            Cast='Test Cast',
        )
        self.review = Review.objects.create(
            Rating=4,
            DatePublished=timezone.now(),
            likes=0,
            Description='This is a test review description.',
            Film=self.film,
            Username=self.user
        )
    
#Checks if a film instance is created with the correct attributes
    def test_film_creation(self):
        self.assertEqual(self.film.Title, 'Test Film')
        self.assertEqual(self.film.Genre, 'comedy')
        self.assertEqual(self.film.Description, 'This is a test film description.')
        self.assertTrue(self.film.ReleaseDate <= timezone.now())
        self.assertEqual(self.film.Director, 'Test Director')
        self.assertEqual(self.film.Cast, 'Test Cast')

#Checks if a review instance is created with the correct attributes
    def test_review_creation(self):
        self.assertEqual(self.review.Rating, 4)
        self.assertTrue(self.review.DatePublished <= timezone.now())
        self.assertEqual(self.review.likes, 0)
        self.assertEqual(self.review.Description, 'This is a test review description.')
        self.assertEqual(self.review.Film, self.film)
        self.assertEqual(self.review.Username, self.user)

#Checks if a like instance is created and associated with the correct review and user
    def test_like_creation(self):
        user2 = User.objects.create_user(username='test_user2', password='test_password')
        like = Like.objects.create(review=self.review, user=user2)
        self.assertEqual(like.review, self.review)
        self.assertEqual(like.user, user2)

#Checks if a watchlist instance is created and associated with the correct user and film
    def test_watchlist_creation(self):
        user2 = User.objects.create_user(username='test_user2', password='test_password')
        watchlist = Watchlist.objects.create(Username=user2, Film=self.film)
        self.assertEqual(watchlist.Username, user2)
        self.assertEqual(watchlist.Film, self.film)

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password')
        self.film = Film.objects.create(
            Title='Test Film',
            Genre='comedy',
            Description='This is a test film description.',
            ReleaseDate=timezone.now(),
            Director='Test Director',
            Cast='Test Cast'
        )

#Checks if the home page is rendered successfully
    def test_home_view(self):
        response = self.client.get(reverse('ReviewFlix:Home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Home.html')

#Checks if the watchlist page is rendered successfully
    def test_watchlist_view(self):
        response = self.client.get(reverse('ReviewFlix:Watchlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Watchlist.html')

#Checks if the add a movie page is rendered successfully
    def test_add_a_movie_view(self):
        response = self.client.get(reverse('ReviewFlix:AddAMovie'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/AddAMovie.html')

#Checks if the individual film page is rendered successfully
    def test_individual_film_view(self):
        response = self.client.get(reverse('ReviewFlix:Film', args=[self.film.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Film.html')

#Checks if the FAQ page is rendered successfully
    def test_faq_view(self):
        response = self.client.get(reverse('ReviewFlix:FAQ'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/FAQ.html')

#Checks if the genres page is rendered successfully
    def test_genres_view(self):
        response = self.client.get(reverse('ReviewFlix:Genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Genres.html')

#Checks if the thriller genre page is rendered successfully
    def test_thriller_view(self):
        response = self.client.get(reverse('ReviewFlix:Thriller'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Thriller.html')

#Checks if the animated genre page is rendered successfully
    def test_animated_view(self):
        response = self.client.get(reverse('ReviewFlix:Animated'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Animated.html')

#Checks if the comedy genre page is rendered successfully
    def test_comedy_view(self):
        response = self.client.get(reverse('ReviewFlix:Comedy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Comedy.html')

#Checks if the horror genre page is rendered successfully
    def test_horror_view(self):
        response = self.client.get(reverse('ReviewFlix:Horror'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Horror.html')

#Checks if the drama genre page is rendered successfully
    def test_drama_view(self):
        response = self.client.get(reverse('ReviewFlix:Drama'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Drama.html')

#Checks if the documentary genre page is rendered successfully
    def test_documentary_view(self):
        response = self.client.get(reverse('ReviewFlix:Documentary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Documentary.html')

#Checks if the register page is rendered successfully
    def test_register_view(self):
        response = self.client.get(reverse('ReviewFlix:Register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Register.html')

#Checks if the login page is rendered successfully
    def test_login_view(self):
        response = self.client.get(reverse('ReviewFlix:Login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Login.html')

#Checks if the logout action redirects successfully
    def test_logout_view(self):
        response = self.client.get(reverse('ReviewFlix:Logout'))
        self.assertEqual(response.status_code, 302)  

#Checks if the review page for a film is rendered successfully (GET request)
    def test_review_for_film_view_get(self):
        response = self.client.get(reverse('ReviewFlix:FilmReview', args=[self.film.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Review.html')

#Checks if a review is successfully submitted for a film (POST request)
    def test_review_for_film_view_post(self):
        data = {
            'Rating': 4,
            'Description': 'This is a test review description.'
        }
        response = self.client.post(reverse('ReviewFlix:FilmReview', args=[self.film.id]), data=data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Review.objects.count(), 1)  

#Checks if a film is successfully added to the user's watchlist
    def test_add_to_watchlist_view(self):
        response = self.client.post(reverse('ReviewFlix:add_to_watchlist'), {'film_id': self.film.id})
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Watchlist.objects.filter(Username=self.user, Film=self.film).exists())

#Checks if a film is successfully removed from the user's watchlist
    def test_remove_from_watchlist_view(self):
        Watchlist.objects.create(Username=self.user, Film=self.film)
        response = self.client.post(reverse('ReviewFlix:remove_from_watchlist'), {'film_id': self.film.id})
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Watchlist.objects.filter(Username=self.user, Film=self.film).exists())
