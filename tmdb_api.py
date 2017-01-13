import requests

#get api key
apifile = open('api_key.txt', 'r')
api_key = apifile.read()

api_base = "https://api.themoviedb.org"
search_base = api_base + "/3/search/movie?api_key=d993f52dbb1f8d190a966790f7590b3b&query="

#search for movie by querying api w/ title, returns id if found, None if not
def search_movie(query):
	query_url = search_base + query
	data = requests.get(query_url)

	#check status code
	if(data.status_code == 200 and len(data.json()['results']) > 0):
		id = data.json()['results'][0]['id']
		return id

	return None


print(search_movie('oceans eleven'))
