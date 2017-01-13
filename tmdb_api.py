import requests

#get api key
apifile = open('api_key.txt', 'r')
api_key = apifile.read()
api_key_query_str = "api_key=d993f52dbb1f8d190a966790f7590b3b"
api_base = "https://api.themoviedb.org"
search_base = api_base + "/3/search/movie?api_key=d993f52dbb1f8d190a966790f7590b3b&query="
poster_base = "https://image.tmdb.org/t/p/original/"
movie_base = "https://api.themoviedb.org/3/movie/"

#search for movie by querying api w/ title, returns id if found, None if not
def search_movie(query):
	query_url = search_base + query
	data = requests.get(query_url)

	#check status code
	if(data.status_code == 200 and len(data.json()['results']) > 0):
		id = data.json()['results'][0]['id']
		return id

	return None

#get movie info using id, returns dictionary w/ all movie information
def get_movie_by_id(id):
	query_url = movie_base + str(id) + "?" + api_key_query_str
	data = requests.get(query_url)

	results = {}

	if(data.status_code == 200):
		json = data.json()

		#get title
		results['title'] = json['title']

		#get image
		#get trailer

	return results

def get_image_by_id(id):
	query_url = movie_base + str(id) + "/images?" + api_key_query_str
	data = requests.get(query_url)



get_movie_by_id(161)
