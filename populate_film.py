import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Film_Reviews_Project.settings')

import django
django.setup()
from Film_Review.models import Film

def populate():
    films_data = [
        {
            'Title': 'The Lion King',
            'Genre': 'animated',
            'Description': 'A young lion prince flees his kingdom only to learn the true meaning of responsibility and bravery.',
            'ReleaseDate': '1994-10-07',
            'Director': 'Roger Allers, Rob Minkoff',
            'Cast': 'Matthew Broderick, Jeremy Irons, James Earl Jones'
        },
        {
            'Title': 'Pulp Fiction',
            'Genre': 'thriller',
            'Description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
            'ReleaseDate': '1994-10-21',
            'Director': 'Quentin Tarantino',
            'Cast': 'John Travolta, Uma Thurman, Samuel L. Jackson'
        },
        {
            'Title': 'The Shawshank Redemption',
            'Genre': 'drama',
            'Description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
            'ReleaseDate': '1995-02-17',
            'Director': 'Frank Darabont',
            'Cast': 'Tim Robbins, Morgan Freeman, Bob Gunton'
        }
        

    ]
    for film in films_data:
        Film.objects.get_or_create(**film)

if __name__ == '__main__':
    print('Starting Film population script...')
    populate()
    print('Film population script complete.')

        
