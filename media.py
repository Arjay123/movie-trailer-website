class Movie:
	def __init__(self, title, trailer_youtube_url, poster_image_url, overview):
		self.title = title

		#FIXME - check if valid url?
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_image_url
		self.overview = overview


