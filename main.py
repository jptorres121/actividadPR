from fastapi import FastAPI, HTTPException
from models import User, Movie
from schemas import UserCreate, MovieCreate
from typing import List
import crud
import operations
import tmdb_api

app = FastAPI()

@app.on_event("startup")
def startup():
    crud.__init__excel()

@app.post("/users/")
def create_user(user: UserCreate):
    users = crud.get_all_users()
    new_user = User(id = len(users) + 1, name = user.name)
    crud.create_user(new_user)
    return new_user

@app.get("/users/")
def get_users():
    return crud.get_user_by_id()


@app.post("/movies/")
def create_movie(movie: MovieCreate):
    user = crud.get_user_by_id(movie.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    all_movies = crud.get_all_movies(include_deleted=True)
    new_movie = Movie(
        id=len(all_movies) + 1,
        **movie.dict(),
        id_deleted=False
    )
    crud.create_movie(new_movie)
    return new_movie


@app.get("/movies/")
def get_movies(include_deleted: bool = False):
    return crud.get_all_movies(include_deleted)

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    crud.delete_movie(movie_id)
    return {"msg": "Pelicula marcada como eliminada y exportada"}

@app.get("/movies/search/")
def search_movie(title: str):
    return operations.search_movie_by_title(title)

@app.get("/movies/filter")
def filter_movies(animated: bool = None, nominated: bool = None,):
    return operations.filter_movies(animated, nominated)

@app.get("/tmdb/search/")
def search_tmdb(title: str):
    results = tmdb_api.search_tmdb_movie(title)
    if results is None:
        raise HTTPException(status_code=404, detail="No se pudo conectar con TMDB o no hay resultados")

    filtered = [
        {
            "title": movie.get("title", "Desconocido"),
            "release_date": movie.get("release_date", "No disponible")
        }
        for movie in results
    ]
    return filtered

@app.get("/users/")
def list_all_users():
    return crud.get_all_users()

@app.get("/users/active/")
def list_active_users():
    return crud.get_active_users()

@app.get("/users/deleted/")
def list_deleted_users():
    return crud.get_deleted_users()

@app.get("/users/{code}")
def get_user(code: str):
    return crud.get_user_by_code(code)

@app.delete("/users/{code}")
def delete_user(code: str):
    crud.delete_user_by_code(code)
    return {"msg": "Usuario marcado como eliminado"}
