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
toy_story_3 = Movie('Toy Story 3', 'https://www.youtube.com/watch?v=JcpWXaA2qeg', 'http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster1.jpg')
saving_private_ryan = Movie('Saving Private Ryan', 'https://www.youtube.com/watch?v=zwhP5b4tD6g', 'http://static.metacritic.com/images/products/movies/0/99efe57b9095e0f9be760550fbd98325.jpg')
interstellar = Movie('Interstellar', 'https://www.youtube.com/watch?v=0vxOhd4qlnA', 'https://resizing.flixster.com/NF5iYPJi334dv-LDZiFt2cEwOJ4=/206x305/v1.bTsxMTE5MDg2MDtqOzE3Mjc0OzEyMDA7ODAwOzEyMDA')
oceans_eleven = Movie('Ocean\'s Eleven', 'https://www.youtube.com/watch?v=u7VTkceSsEw', 'https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmYzVkMmUtOGRhMi00MTNmLThlMmUtZTljYjlkMjNkMjJkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg')

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
