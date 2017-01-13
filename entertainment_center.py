from media import Movie
from fresh_tomatoes import open_movies_page

def remove_movie(movies, index):
	if index < len(movies):
		movies.pop(index)
	else:
		print("Not a valid option")

def create_movie():
	print()

	title = input("Please enter a title: ")
	trailer = input("Please enter the trailer url: ")
	poster = input("Please enter the poster image url: ")

	movie = Movie(title, trailer, poster)
	return movie

#init movies
toy_story_3 = Movie('Toy Story 3', 
	'https://www.youtube.com/watch?v=JcpWXaA2qeg', 
	'http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster1.jpg',
	"Woody, Buzz, and the rest of Andy's toys haven't been played with in years. "
	"With Andy about to go to college, the gang find themselves accidentally left at a nefarious day care center. "
	"The toys must band together to escape and return home to Andy.")

saving_private_ryan = Movie('Saving Private Ryan', 
	'https://www.youtube.com/watch?v=zwhP5b4tD6g', 
	'http://static.metacritic.com/images/products/movies/0/99efe57b9095e0f9be760550fbd98325.jpg',
	"As U.S. troops storm the beaches of Normandy, three brothers lie dead on the battlefield, "
	"with a fourth trapped behind enemy lines. Ranger captain John Miller and seven men are tasked with"
	" penetrating German-held territory and bringing the boy home.")

interstellar = Movie('Interstellar', 
	'https://www.youtube.com/watch?v=0vxOhd4qlnA', 
	'https://resizing.flixster.com/NF5iYPJi334dv-LDZiFt2cEwOJ4=/206x305/v1.bTsxMTE5MDg2MDtqOzE3Mjc0OzEyMDA7ODAwOzEyMDA',
	"Interstellar chronicles the adventures of a group of explorers who make use of a newly discovered wormhole to"
	"surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.")

oceans_eleven = Movie('Ocean\'s Eleven', 
	'https://www.youtube.com/watch?v=u7VTkceSsEw', 
	'https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmYzVkMmUtOGRhMi00MTNmLThlMmUtZTljYjlkMjNkMjJkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
	"Less than 24 hours into his parole, charismatic thief Danny Ocean is already rolling out his next plan: In one night"
	", Danny's hand-picked crew of specialists will attempt to steal more than $150 million from three Las Vegas casinos"
	". But to score the cash, Danny risks his chances of reconciling with ex-wife, Tess.")

movies = [toy_story_3, saving_private_ryan, interstellar, oceans_eleven]

option = None

#allow user to edit list before generating web page
while(option != 'g'):
	movie_title_list = [mov.title for mov in movies]
	print()
	print("Current movies to be processed: " + str(movie_title_list))
	option = input("Choose an option: a - Add movie to list, d - Delete movie from list, g - Generate web page: ")
	option = option.lower()

	#delete movie
	if option == 'd':
		print()

		#print movie choices w/ index for selection
		for index in range(len(movies)):
			print(str(index + 1) + ": " + movies[index].title)

		#make sure user enters an int value
		try:
			deleteChoice = int(input("Please choose a movie to delete: "))
			remove_movie(movies, deleteChoice - 1)
		except ValueError:
			print("Not a valid option")

	#add movie		
	elif option == 'a':
		movies.append(create_movie())


open_movies_page(movies)
