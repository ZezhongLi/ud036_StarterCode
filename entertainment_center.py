'''
This script movie information from data.txt,
then form movie model array for fresh_tomatoes module.
'''
import media
import fresh_tomatoes # This module generate html page using movie models.
'''
    1. read movie count from data.txt
    2. using for loop read movie information to form the movie model array
    3. using fresh_tomatoes to generate html pages and open it with default broswer
'''
filepath = 'data.txt'
fp = open(filepath)
movie_count = fp.readline()
movies = []
for i in range(0, int(movie_count)):
    movie = media.Movie(
                        fp.readline(),
                        fp.readline(),
                        fp.readline(),
                        fp.readline()
                        )
    movies.append(movie)
fresh_tomatoes.open_movies_page(movies)
