from media import Movie
from fresh_tomatoes import open_movies_page
from tmdb_api import search_movie, get_movie_by_id


def remove_movie(movies, index):
    if index < len(movies):
        movies.pop(index)
    else:
        print("Not a valid option")

#create new movie entry using user inputs if parameters are None
def create_movie(title=None, trailer=None, poster=None, overview=None):
    print()

    if title is None:
        title = input("Please enter a title: ")
    if trailer is None:
        trailer = input("Please enter the trailer url: ")
    if poster is None:
        poster = input("Please enter the poster image url: ")
    if overview is None:
        overview = input("Please enter a quick overview of the movie: ")

    movie = Movie(title, trailer, poster, overview)
    return movie

# search tmdb for movie by title with user's input
def create_movie_from_tmdb():
    title = input("Please enter the title of the movie to search for: ")

    movie_id = search_movie(title)

    if movie_id is None:
        print("Could not find a movie with that title!")
        return

    movie = get_movie_by_id(movie_id)
    print("Found movie: %s" % movie['title'])
    if input("Add movie to list? (y/n): ") == 'y':
        movies.append(create_movie(movie['title'], 
                                   movie['trailer'],
                                   movie['poster'],
                                   movie['overview']))

# init default movies
toy_story_3 = Movie('Toy Story 3',
                    'https://www.youtube.com/watch?v=JcpWXaA2qeg',
                    'http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster1.jpg',
                    "Woody, Buzz, and the rest of Andy's toys haven't been "
                    "played with in years. With Andy about to go to college, "
                    "the gang find themselves accidentally left at a nefarious "
                    "day care center. The toys must band together to escape "
                    "and return home to Andy.")

saving_private_ryan = Movie('Saving Private Ryan',
                            'https://www.youtube.com/watch?v=zwhP5b4tD6g',
                            'http://static.metacritic.com/images/products/movies/0/99efe57b9095e0f9be760550fbd98325.jpg',
                            "As U.S. troops storm the beaches of Normandy, "
                            "three brothers lie dead on the battlefield, with "
                            "a fourth trapped behind enemy lines. Ranger "
                            "captain John Miller and seven men are tasked with "
                            "penetrating German-held territory and bringing "
                            "the boy home.")

interstellar = Movie('Interstellar',
                     'https://www.youtube.com/watch?v=0vxOhd4qlnA',
                     'https://resizing.flixster.com/NF5iYPJi334dv-LDZiFt2cEwOJ4=/206x305/v1.bTsxMTE5MDg2MDtqOzE3Mjc0OzEyMDA7ODAwOzEyMDA',
                     "Interstellar chronicles the adventures of a group of "
                     "explorers who make use of a newly discovered wormhole to "
                     "surpass the limitations on human space travel and "
                     "conquer the vast distances involved in an interstellar "
                     "voyage.")

oceans_eleven = Movie('Ocean\'s Eleven',
                      'https://www.youtube.com/watch?v=u7VTkceSsEw',
                      'https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmYzVkMmUtOGRhMi00MTNmLThlMmUtZTljYjlkMjNkMjJkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                      "Less than 24 hours into his parole, charismatic thief "
                      "Danny Ocean is already rolling out his next plan: In "
                      "one night , Danny's hand-picked crew of specialists "
                      "will attempt to steal more than $150 million from "
                      "three Las Vegas casinos . But to score the cash, Danny "
                      "risks his chances of reconciling with ex-wife, Tess.")

movies = [toy_story_3, saving_private_ryan, interstellar, oceans_eleven]
option = None

# allow user to edit list before generating web page
while(option != 'g'):

    # prompt user input
    option = input("\nChoose an option\n"
                   "a - Add movie to list\n"
                   "d - Delete movie from list\n"
                   "g - Generate web page\n"
                   "s - Search movie database for movie\n"
                   "v - View current movie list\n")
    option = option.lower()

    # add movie
    if option == 'a':
        movies.append(create_movie())

    # delete movie
    elif option == 'd':
        
        # print movie choices w/ indices for selection i.e.
        for index in range(len(movies)):
            print('%s: %s' % (str(index), movies[index].title))
        
        # remove movie if valid user input
        try:
            deleteChoice = int(input("\nPlease choose a movie to delete: "))
            remove_movie(movies, deleteChoice)
        except ValueError:
            print("Not a valid option")

    # add movie from api
    elif option == 's':
        create_movie_from_tmdb()

    # print current movies in list
    elif option == 'v':
        movie_title_list = [mov.title for mov in movies]
        print("\nCurrent movies to be processed: " + str(movie_title_list))


open_movies_page(movies)
