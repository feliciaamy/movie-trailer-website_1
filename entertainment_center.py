import media
import fresh_tomatoes
from py_compile import compile

# Compile fresh_tomatoes with .pyc form
compile('fresh_tomatoes.py')


# Create a dictionary with title as the key and information as the value
def __GetInfo(tFile):
    movie_info = {}
    temp_title = ''
    # Open File
    with open(tFile) as f:
        content = f.readlines()
    f.close()
    for i in range(len(content)):
        if content[i] == '\n':
            pass
        elif i % 2 == 0:
            temp_title = content[i].replace('\n', '')
        else:
            movie_info[temp_title] = content[i].replace('\n', '')
    return movie_info


# Making movie objects and put the details in
def refreshMovies():
    # Create movie instances without any information except title
    toy_story = media.Movie('Toy Story')
    avatar = media.Movie('Avatar')
    hunger_games = media.Movie('The Hunger Games')
    good_luck_chuck = media.Movie('Good Luck Chuck')
    divergent = media.Movie('Divergent')
    TFIOS = media.Movie('The Fault in Our Star')
    inside_out = media.Movie('Inside Out')
    up = media.Movie('Up')
    tangled = media.Movie('Tangled')

    # The list of movies
    movies = [avatar, toy_story,
              hunger_games, good_luck_chuck, divergent,
              TFIOS, inside_out, up, tangled]

    # Input all the information inside the movie instances
    for movie in movies:
        # Set the information of the movie
        # Information: Title, storyline, poster url, trailer url,
        # rating, and rank
        title = movie.title
        movie.setTitle(title)
        movie.setStoryline(movie_storyline[title])
        movie.setPoster(movie_poster_url[title])
        movie.setTrailer(movie_youtube_url[title])
        movie.setRating(movie_rating[title])
        movie.setRank(movie_rank[title])

    # Transfer the movies information to the website in the form of html file
    fresh_tomatoes.open_movies_page(movies)


# Create a description dictionary
movie_storyline = __GetInfo('movie_storyline.txt')

# Create a poster URL dictionary
movie_poster_url = __GetInfo('movie_poster_url.txt')

# Create a youtube URL dictionary
movie_youtube_url = __GetInfo('movie_youtube_url.txt')

# Create a movie rating dictionary
movie_rating = __GetInfo('movie_rating.txt')

# Create a movie rank dictionary
movie_rank = __GetInfo('movie_rank.txt')


# Refresh/input the movie information to html file
refreshMovies()

