from movie import Movie
from fresh_tomatoes import open_movies_page

toy_story_3 = Movie('Toy Story 3', 'https://www.youtube.com/watch?v=JcpWXaA2qeg', 'http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster1.jpg')

movies = [toy_story_3]

open_movies_page(movies)
