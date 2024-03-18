import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Film_Reviews_Project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from Film_Review.models import UserProfile

def populate_user_profiles():
    users_data = [
        {
            'username': 'john_doe',
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'password123',
            'is_producer': False
        },
        {
            'username': 'jane_smith',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'password': 'password123',
            'is_producer': True
        },
        
        {
            'username': 'jim_brown',
            'first_name': 'Jim',
            'last_name': 'Brown',
            'password': 'password123',
            'is_producer': False
        },
        
        {
            'username': 'jane_doe',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'password': 'password123',
            'is_producer': False
        }
        
 
    ]

    for user_data in users_data:
        # Create user
        user = User.objects.create_user(
            username=user_data['username'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            password=user_data['password']
        )

        # Create user profile
        UserProfile.objects.create(
            user=user,
            firstName=user_data['first_name'],
            lastName=user_data['last_name'],
            isProducer=user_data['is_producer']
        )

        print(f'Created UserProfile for user: {user.username}')

if __name__ == '__main__':
    print('Starting UserProfile population script...')
    populate_user_profiles()
    print('UserProfile population script complete.')
