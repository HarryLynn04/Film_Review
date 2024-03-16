import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Film_Reviews_Project.settings')
import django
django.setup()


from django.contrib.auth.models import User
from Film_Review.models import UserProfile

def create_users():
    users_data = [
        {'username': 'john_doe', 'first_name': 'John', 'last_name': 'Doe', 'is_producer': False},
        {'username': 'jane_smith', 'first_name': 'Jane', 'last_name': 'Smith', 'is_producer': True},
        {'username': 'bob_johnson', 'first_name': 'Bob', 'last_name': 'Johnson', 'is_producer': False},
        {'username': 'sarah_jones', 'first_name': 'Sarah', 'last_name': 'Jones', 'is_producer': True},
        {'username': 'mike_brown', 'first_name': 'Mike', 'last_name': 'Brown', 'is_producer': False},
        
    ]
    
    for data in users_data:
        user = User.objects.create_user(
            username=data['username'],
            password='password123',  
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        
        # Create UserProfile
        UserProfile.objects.create(
            user=user,
            firstName=data['first_name'],
            lastName=data['last_name'],
            isProducer=data['is_producer']
        )
        
        print(f"User '{data['username']}' created.")

if __name__ == "__main__":
    create_users()
