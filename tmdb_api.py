import requests

#get api key
apifile = open('api_key.txt', 'r')
API_KEY = apifile.read()
API_KEY_QUERY_STR = "api_key=" + API_KEY

API_BASE = "https://api.themoviedb.org"
SEARCH_BASE = API_BASE + "/3/search/movie?" + API_KEY_QUERY_STR + "&query="
MOVIE_BASE = API_BASE + "/3/movie/"

POSTER_BASE = "https://image.tmdb.org/t/p/original"


#search for movie by querying api w/ title, returns id if found, None if not
def search_movie(query):
	query_url = SEARCH_BASE + query
	data = requests.get(query_url)

	#check status code
	if(data.status_code == 200 and len(data.json()['results']) > 0):
		id = data.json()['results'][0]['id']
		return id


#get movie info using id, returns dictionary w/ all movie information
def get_movie_by_id(id):
	query_url = MOVIE_BASE + str(id) + "?" + API_KEY_QUERY_STR
	data = requests.get(query_url)

	results = {}

	if data.status_code == 200:
		json = data.json()

		#get title
		results['title'] = json['title']

		#get image
		results['poster'] = get_image_by_id(id)

		#get trailer

	return results


#get movie poster by id, returns url of image if found
def get_image_by_id(id):
	query_url = MOVIE_BASE + str(id) + "/images?" + API_KEY_QUERY_STR
	data = requests.get(query_url)

	if data.status_code == 200 and len(data.json()['posters']) > 0:
		return POSTER_BASE + data.json()['posters'][0]['file_path']


print(get_movie_by_id(161)['poster'])
