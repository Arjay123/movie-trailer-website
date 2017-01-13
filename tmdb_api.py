import requests

#get api key
apifile = open('api_key.txt', 'r')
api_key = apifile.read()
api_key_query_str = "api_key=d993f52dbb1f8d190a966790f7590b3b"

api_base = "https://api.themoviedb.org"
search_base = api_base + "/3/search/movie?" + api_key_query_str + "&query="
movie_base = api_base + "/3/movie/"

poster_base = "https://image.tmdb.org/t/p/original"


#search for movie by querying api w/ title, returns id if found, None if not
def search_movie(query):
	query_url = search_base + query
	data = requests.get(query_url)

	#check status code
	if(data.status_code == 200 and len(data.json()['results']) > 0):
		id = data.json()['results'][0]['id']
		return id


#get movie info using id, returns dictionary w/ all movie information
def get_movie_by_id(id):
	query_url = movie_base + str(id) + "?" + api_key_query_str
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
	query_url = movie_base + str(id) + "/images?" + api_key_query_str
	data = requests.get(query_url)

	if data.status_code == 200 and len(data.json()['posters']) > 0:
		return poster_base + data.json()['posters'][0]['file_path']


print(get_movie_by_id(161)['poster'])
