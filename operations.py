from crud import get_all_movies
from models import Movie

def filter_movies(animated: bool = None, nominated: bool = None):
    movies = get_all_movies()
    if animated is not None:
        movies = [m for m in movies if m.is_animated == animated]
    if nominated is not None:
        movies = [m for m in movies if m.nominated == nominated]
    return movies

def search_movie_by_title(title: str):
    movies = get_all_movies()
    return [m for m in movies if title.lower() in m.title.lower()]
