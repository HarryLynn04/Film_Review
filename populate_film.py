import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Film_Reviews_Project.settings')

import django
django.setup()
from Film_Review.models import Film

def populate():
    films_data = [
        # Animated
        {
            'Title': 'The Lion King',
            'Genre': 'animated',
            'Description': 'A young lion prince flees his kingdom only to learn the true meaning of responsibility and bravery.',
            'ReleaseDate': '1994-10-07',
            'Director': 'Roger Allers, Rob Minkoff',
            'Cast': 'Matthew Broderick, Jeremy Irons, James Earl Jones'
        },
        {
            'Title': 'Toy Story',
            'Genre': 'animated',
            'Description': 'A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy\'s room.',
            'ReleaseDate': '1995-11-22',
            'Director': 'John Lasseter',
            'Cast': 'Tom Hanks, Tim Allen, Don Rickles'
        },
        {
            'Title': 'Finding Nemo',
            'Genre': 'animated',
            'Description': 'After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.',
            'ReleaseDate': '2003-05-30',
            'Director': 'Andrew Stanton, Lee Unkrich',
            'Cast': 'Albert Brooks, Ellen DeGeneres, Alexander Gould'
        },
        {
            'Title': 'Frozen',
            'Genre': 'animated',
            'Description': 'When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister Anna teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.',
            'ReleaseDate': '2013-11-27',
            'Director': 'Chris Buck, Jennifer Lee',
            'Cast': 'Kristen Bell, Idina Menzel, Jonathan Groff'
        },
        {
            'Title': 'Shrek',
            'Genre': 'animated',
            'Description': 'A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.',
            'ReleaseDate': '2001-05-18',
            'Director': 'Andrew Adamson, Vicky Jenson',
            'Cast': 'Mike Myers, Eddie Murphy, Cameron Diaz'
        },
        # Comedy
        {
            'Title': 'Dumb and Dumber',
            'Genre': 'comedy',
            'Description': 'After a woman leaves a briefcase at the airport terminal, a dumb limo driver and his dumber friend set out on a hilarious cross-country road trip to Aspen to return it.',
            'ReleaseDate': '1994-12-16',
            'Director': 'Peter Farrelly',
            'Cast': 'Jim Carrey, Jeff Daniels, Lauren Holly'
        },
        {
            'Title': 'Superbad',
            'Genre': 'comedy',
            'Description': 'Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.',
            'ReleaseDate': '2007-08-17',
            'Director': 'Greg Mottola',
            'Cast': 'Michael Cera, Jonah Hill, Christopher Mintz-Plasse'
        },
            {
            'Title': 'Monty Python and the Holy Grail',
            'Genre': 'comedy',
            'Description': 'King Arthur and his knights embark on a low-budget search for the Grail, encountering many, very silly obstacles.',
            'ReleaseDate': '1975-05-25',
            'Director': 'Terry Gilliam, Terry Jones',
            'Cast': 'Graham Chapman, John Cleese, Eric Idle'
        },
        {
            'Title': 'Anchorman: The Legend of Ron Burgundy',
            'Genre': 'comedy',
            'Description': 'Ron Burgundy is San Diego\'s top-rated newsman in the male-dominated broadcasting of the 1970s, but that\'s all about to change for Ron and his cronies when an ambitious woman is hired as a new anchor.',
            'ReleaseDate': '2004-07-09',
            'Director': 'Adam McKay',
            'Cast': 'Will Ferrell, Christina Applegate, Steve Carell'
        },
        {
            'Title': 'The Grand Budapest Hotel',
            'Genre': 'comedy',
            'Description': 'A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel\'s glorious years under an exceptional concierge.',
            'ReleaseDate': '2014-03-28',
            'Director': 'Wes Anderson',
            'Cast': 'Ralph Fiennes, F. Murray Abraham, Mathieu Amalric'
        },
        # Drama
        {
            'Title': 'Forrest Gump',
            'Genre': 'drama',
            'Description': 'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.',
            'ReleaseDate': '1994-07-06',
            'Director': 'Robert Zemeckis',
            'Cast': 'Tom Hanks, Robin Wright, Gary Sinise'
        },
        {
            'Title': 'Good Will Hunting',
            'Genre': 'drama',
            'Description': 'Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.',
            'ReleaseDate': '1997-12-05',
            'Director': 'Gus Van Sant',
            'Cast': 'Robin Williams, Matt Damon, Ben Affleck'
        },
        {
            'Title': 'The Godfather',
            'Genre': 'drama',
            'Description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            'ReleaseDate': '1972-03-24',
            'Director': 'Francis Ford Coppola',
            'Cast': 'Marlon Brando, Al Pacino, James Caan'
        },
        {
            'Title': 'Schindler\'s List',
            'Genre': 'drama',
            'Description': 'In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.',
            'ReleaseDate': '1994-12-15',
            'Director': 'Steven Spielberg',
            'Cast': 'Liam Neeson, Ralph Fiennes, Ben Kingsley'
        },
        {
            'Title': 'The Shawshank Redemption',
            'Genre': 'drama',
            'Description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
            'ReleaseDate': '1995-02-17',
            'Director': 'Frank Darabont',
            'Cast': 'Tim Robbins, Morgan Freeman, Bob Gunton'
        },
        # Documentary
        {
            'Title': 'Blackfish',
            'Genre': 'documentary',
            'Description': 'A documentary following the controversial captivity of killer whales, and its dangers for both humans and whales.',
            'ReleaseDate': '2013-07-19',
            'Director': 'Gabriela Cowperthwaite',
            'Cast': 'Kim Ashdown, Ken Balcomb, Samantha Berg'
        },
        {
            'Title': 'Won\'t You Be My Neighbor?',
            'Genre': 'documentary',
            'Description': 'An exploration of the life, lessons, and legacy of iconic children\'s television host, Fred Rogers.',
            'ReleaseDate': '2018-06-29',
            'Director': 'Morgan Neville',
            'Cast': 'Fred Rogers, Joanne Rogers, John Rogers'
        },
        {
            'Title': 'March of the Penguins',
            'Genre': 'documentary',
            'Description': 'In the Antarctic, every March since the beginning of time, the quest begins to find the perfect mate and start a family.',
            'ReleaseDate': '2005-01-26',
            'Director': 'Luc Jacquet',
            'Cast': 'Morgan Freeman (Narrator)'
        },
        {
            'Title': 'Man on Wire',
            'Genre': 'documentary',
            'Description': 'A look at tightrope walker Philippe Petit\'s daring, but illegal, high-wire routine performed between New York City\'s World Trade Center\'s twin towers in 1974, what some consider, "the artistic crime of the century."',
            'ReleaseDate': '2008-08-29',
            'Director': 'James Marsh',
            'Cast': 'Philippe Petit, Jean François Heckel, Jean-Louis Blondeau'
        },
        {
            'Title': '20 Feet from Stardom',
            'Genre': 'documentary',
            'Description': 'Backup singers live in a world that lies just beyond the spotlight.',
            'ReleaseDate': '2013-07-05',
            'Director': 'Morgan Neville',
            'Cast': 'Darlene Love, Merry Clayton, Lisa Fischer'
        },
        # Horror
        {
            'Title': 'The Shining',
            'Genre': 'horror',
            'Description': 'A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.',
            'ReleaseDate': '1980-06-13',
            'Director': 'Stanley Kubrick',
            'Cast': 'Jack Nicholson, Shelley Duvall, Danny Lloyd'
        },
        {
            'Title': 'Psycho',
            'Genre': 'horror',
            'Description': 'A Phoenix secretary embezzles $40,000 from her employer\'s client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.',
            'ReleaseDate': '1960-09-08',
            'Director': 'Alfred Hitchcock',
            'Cast': 'Anthony Perkins, Janet Leigh, Vera Miles'
        },
        {
            'Title': 'The Exorcist',
            'Genre': 'horror',
            'Description': 'When a teenage girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her daughter.',
            'ReleaseDate': '1973-12-26',
            'Director': 'William Friedkin',
            'Cast': 'Ellen Burstyn, Max von Sydow, Linda Blair'
        },
        {
            'Title': 'Get Out',
            'Genre': 'horror',
            'Description': 'A young African-American visits his white girlfriend\'s parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.',
            'ReleaseDate': '2017-02-24',
            'Director': 'Jordan Peele',
            'Cast': 'Daniel Kaluuya, Allison Williams, Bradley Whitford'
        },
        {
            'Title': 'A Nightmare on Elm Street',
            'Genre': 'horror',
            'Description': 'The monstrous spirit of a slain child murderer seeks revenge by invading the dreams of teenagers whose parents were responsible for his untimely death.',
            'ReleaseDate': '1984-11-16',
            'Director': 'Wes Craven',
            'Cast': 'Heather Langenkamp, Johnny Depp, Robert Englund'
        },
        # Thriller
        {
            'Title': 'Pulp Fiction',
            'Genre': 'thriller',
            'Description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
            'ReleaseDate': '1994-10-21',
            'Director': 'Quentin Tarantino',
            'Cast': 'John Travolta, Uma Thurman, Samuel L. Jackson'
        },
        {
            'Title': 'Se7en',
            'Genre': 'thriller',
            'Description': 'Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.',
            'ReleaseDate': '1995-09-22',
            'Director': 'David Fincher',
            'Cast': 'Morgan Freeman, Brad Pitt, Kevin Spacey'
        },
        {
            'Title': 'The Silence of the Lambs',
            'Genre': 'thriller',
            'Description': 'A young FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims.',
            'ReleaseDate': '1991-02-14',
            'Director': 'Jonathan Demme',
            'Cast': 'Jodie Foster, Anthony Hopkins, Lawrence A. Bonney'
        },
        {
            'Title': 'Inception',
            'Genre': 'thriller',
            'Description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
            'ReleaseDate': '2010-07-16',
            'Director': 'Christopher Nolan',
            'Cast': 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page'
        },
        {
            'Title': 'The Departed',
            'Genre': 'thriller',
            'Description': 'An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.',
            'ReleaseDate': '2006-10-06',
            'Director': 'Martin Scorsese',
            'Cast': 'Leonardo DiCaprio, Matt Damon, Jack Nicholson'
        }
    ]
    for film in films_data:
        Film.objects.get_or_create(**film)
    
    shawshank_film = Film.objects.get(Title='The Shawshank Redemption')

    shawshank_film.image = 'film_images/shawshank.jpg'
    shawshank_film.save()
    

if __name__ == '__main__':
    print('Starting Film population script...')
    populate()
    print('Film population script complete.')
