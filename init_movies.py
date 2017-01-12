from movie import Movie
from fresh_tomatoes import open_movies_page

toy_story_3 = Movie('Toy Story 3', 'https://www.youtube.com/watch?v=JcpWXaA2qeg', 'http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster1.jpg')
saving_private_ryan = Movie('Saving Private Ryan', 'https://www.youtube.com/watch?v=zwhP5b4tD6g', 'http://static.metacritic.com/images/products/movies/0/99efe57b9095e0f9be760550fbd98325.jpg')
interstellar = Movie('Interstellar', 'https://www.youtube.com/watch?v=0vxOhd4qlnA', 'https://resizing.flixster.com/NF5iYPJi334dv-LDZiFt2cEwOJ4=/206x305/v1.bTsxMTE5MDg2MDtqOzE3Mjc0OzEyMDA7ODAwOzEyMDA')
oceans_eleven = Movie('Ocean\'s Eleven', 'https://www.youtube.com/watch?v=u7VTkceSsEw', 'https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmYzVkMmUtOGRhMi00MTNmLThlMmUtZTljYjlkMjNkMjJkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg')



movies = [toy_story_3, saving_private_ryan, interstellar, oceans_eleven]

open_movies_page(movies)
