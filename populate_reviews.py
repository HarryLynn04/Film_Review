
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Film_Reviews_Project.settings')
import django
django.setup()

import random
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from Film_Review.models import Film, Review, UserProfile




def populate_reviews():
    # Get all films from the database
    films = Film.objects.all()

    # Get all users from the database
    users = User.objects.all()

   

    for film in films:
        # Generate a random number of reviews for each film (between 1 and 5)
        num_reviews = random.randint(1, 5)
        
        for _ in range(num_reviews):
            # Choose a random user for the review
            user = random.choice(users)
            
            # Generate a random rating for the review
            rating = random.randint(1, 5)
            thumbsUp = random.randint(0, 10)
            
            # Generate a random date within the defined range for the review
            review_date = timezone.now()
            
            # Generate a random description for the review
            description = f"This film is {generate_review_sentiment(rating)}."
            
            # Create the review object
            review = Review.objects.create(
                Rating=rating,
                DatePublished=review_date,
                Description=description,
                likes = thumbsUp,
                Film=film,
                Username=user
            )



def generate_review_sentiment(rating):
    # Generate review sentiments based on rating
    if rating == 1:
        return "terrible"
    elif rating == 2:
        return "not good"
    elif rating == 3:
        return "average"
    elif rating == 4:
        return "good"
    elif rating == 5:
        return "excellent"

if __name__ == '__main__':
    print('Starting Reviews population script...')
    populate_reviews()
    print('Reviews population script complete.')
