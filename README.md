# movie-trailer-website
Project 1 for Udacity's Full Stack Engineer class. Creates a webpage with a list of movies specified by the user that contains 
information like the movie title, synopsis, youtube video of the trailer and an image of the movie poster.

## Install
Download the repo manually. Necessary libraries can be installed through the requirements.txt file and pip by using the command

```
pip install -r requirements.txt
```

An api key from TMDB will be necessary to use the movie searching feature. Store the api key in a text file called
```
api_key.txt
```

## Libraries used
[Requests](http://docs.python-requests.org/en/master/) - Used to send and receive requests for the TMDB API

## Usage
Usage is fairly simple:
```
python entertainment_center.py
```

User will be presented with a few options:

a - Add movie to list manually<br>
d - Delete movie from list<br>
g - Generate web page<br>
s - Search movie database for movie<br>
v - View current movie list<br>

When 'g' is selected, a webpage will be created in the same folder under the name.
```
fresh_tomatoes.html
```

# Webpage features
The webpage displays all the movies added to the list in entertainment_center.py along with an image of the movie poster.<br>
Hovering the mouse cursor over a movie poster will display the movie synopsis in a tooltip.<br>
Clicking on a movie poster will display the movie's trailer in a YouTube video.

# Sample webpage
![pageres]sample.png
