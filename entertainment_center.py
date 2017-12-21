import media
import fresh_tomatoes

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
