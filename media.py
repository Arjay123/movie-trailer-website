class Movie(object):
    """
    Represents a movie, containing information that a user may want to know
    about the movie

    Attributes:
            title - Title of the movie
            trailer_youtube_url - Link to the youtube video of the movie's trailer
            poster_image_url - Link to an image file of the movie's poster
            overview - Quick synopsis of the movie's plot
    """

    def __init__(self, title, trailer_youtube_url, poster_image_url, overview):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.overview = overview
