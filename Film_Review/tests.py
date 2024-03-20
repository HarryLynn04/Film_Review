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
    
    def test_film_creation(self):
        self.assertEqual(self.film.Title, 'Test Film')
        self.assertEqual(self.film.Genre, 'comedy')
        self.assertEqual(self.film.Description, 'This is a test film description.')
        self.assertTrue(self.film.ReleaseDate <= timezone.now())
        self.assertEqual(self.film.Director, 'Test Director')
        self.assertEqual(self.film.Cast, 'Test Cast')
    
    def test_review_creation(self):
        self.assertEqual(self.review.Rating, 4)
        self.assertTrue(self.review.DatePublished <= timezone.now())
        self.assertEqual(self.review.likes, 0)
        self.assertEqual(self.review.Description, 'This is a test review description.')
        self.assertEqual(self.review.Film, self.film)
        self.assertEqual(self.review.Username, self.user)

    def test_like_creation(self):
        user2 = User.objects.create_user(username='test_user2', password='test_password')
        like = Like.objects.create(review=self.review, user=user2)
        self.assertEqual(like.review, self.review)
        self.assertEqual(like.user, user2)

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
    
    def test_home_view(self):
        response = self.client.get(reverse('ReviewFlix:Home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Home.html')

    def test_watchlist_view(self):
        response = self.client.get(reverse('ReviewFlix:Watchlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Watchlist.html')

    def test_add_a_movie_view(self):
        response = self.client.get(reverse('ReviewFlix:AddAMovie'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/AddAMovie.html')

    def test_individual_film_view(self):
        response = self.client.get(reverse('ReviewFlix:Film', args=[self.film.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Film.html')

    def test_faq_view(self):
        response = self.client.get(reverse('ReviewFlix:FAQ'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/FAQ.html')

    def test_genres_view(self):
        response = self.client.get(reverse('ReviewFlix:Genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Genres.html')

    def test_thriller_view(self):
        response = self.client.get(reverse('ReviewFlix:Thriller'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Thriller.html')

    def test_animated_view(self):
        response = self.client.get(reverse('ReviewFlix:Animated'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Animated.html')

    def test_comedy_view(self):
        response = self.client.get(reverse('ReviewFlix:Comedy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Comedy.html')

    def test_horror_view(self):
        response = self.client.get(reverse('ReviewFlix:Horror'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Horror.html')

    def test_drama_view(self):
        response = self.client.get(reverse('ReviewFlix:Drama'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Drama.html')

    def test_documentary_view(self):
        response = self.client.get(reverse('ReviewFlix:Documentary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Documentary.html')

    def test_register_view(self):
        response = self.client.get(reverse('ReviewFlix:Register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Register.html')

    def test_login_view(self):
        response = self.client.get(reverse('ReviewFlix:Login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('ReviewFlix:Logout'))
        self.assertEqual(response.status_code, 302)  

    def test_review_for_film_view_get(self):
        response = self.client.get(reverse('ReviewFlix:FilmReview', args=[self.film.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReviewFlix/Review.html')

    def test_review_for_film_view_post(self):
        data = {
            'Rating': 4,
            'Description': 'This is a test review description.'
        }
        response = self.client.post(reverse('ReviewFlix:FilmReview', args=[self.film.id]), data=data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Review.objects.count(), 1)  

    def test_add_to_watchlist_view(self):
        response = self.client.post(reverse('ReviewFlix:add_to_watchlist'), {'film_id': self.film.id})
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Watchlist.objects.filter(Username=self.user, Film=self.film).exists())

    def test_remove_from_watchlist_view(self):
        Watchlist.objects.create(Username=self.user, Film=self.film)
        response = self.client.post(reverse('ReviewFlix:remove_from_watchlist'), {'film_id': self.film.id})
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Watchlist.objects.filter(Username=self.user, Film=self.film).exists())
