import requests

def search_tmdb_movie(title: str):
    url = f"https://api.themoviedb.org/3/search/movie?query={title}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOWUzYWQ2NDMxOWUxZDdkMjg1OGE1Y2U2Nzg2OThkOCIsIm5iZiI6MTc0Mzg3NTk2OC40NjcsInN1YiI6IjY3ZjE2ZjgwOTMxY2UxNzRhMmQ5OWY2NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wGVBtkqjmf9gCu-A1y19Z4CuI_uvNVRp68E_rA9xARU"
    }

    response = requests.get(url, headers=headers)

    print("DEBUG:", response.status_code, response.text)

    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return None
