import media
import fresh_tomatoes as ft
"""In this file you can create an object of the class Movie from media 
module."""
#This is an object that stores the values(title,poster_url,trailer_link)
#for the movie Toy Story.
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous"
                        " when a new spaceman figure supplants him as top"
                        " toy in a boy's room.",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8"
                        "/2013/02/toy_story_wallpaper_by_artifypics-"
                        "d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#This is an object that stores the values(title,poster_url,trailer_link)
#for the movie Deadpool.
deadpool = media.Movie("Deadpool",
                       "A former Special Forces operative turned mercenary"
                       " is subjected to a rogue experiment that leaves him"
                       " with accelerated healing powers, adopting the alter"
                       " ego Deadpool.",
                       "http://cdn3-www.comingsoon.net/assets/uploads/"
                       "gallery/deadpool/deadpool_ver9.jpg",
                       "https://www.youtube.com/watch?v=Xithigfg7dA")
#This is an object that stores the values(title,poster_url,trailer_link)
#for the movie 12 Angry Men.
tangrymen = media.Movie("12 Angry Men",
                        "A jury holdout attempts to prevent a miscarriage"
                        " of justice by forcing his colleagues to reconsider"
                        " the evidence.",
                        "http://ia.media-imdb.com/images/M/MV5BODQwOTc5MDM2N"
                        "15BMl5BanBnXkFtZTcwODQxNTEzNA@@._V1_UY1200_CR85,0"
                        ",630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=fSG38tk6TpI")
#movies is the list that cotaines all the Movie object we have created 
#earlier.
movies = {toy_story, deadpool, tangrymen}
#We are sending the list of objects to the open_movies_page method of 
#the fresh_tomatoes module.
ft.open_movies_page(movies)
