import json
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from .models import Movie


def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_imdb_html(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.text

def parse_top_250(html: str, limit: int = None) -> List[Dict]:
    soup = BeautifulSoup(html, "html.parser")

    ul = soup.select_one("ul.ipc-metadata-list")
    if ul is None:
        raise ValueError("Não foi possível encontrar a lista do TOP 250. O layout pode ter mudado.")

    items = ul.select("li.ipc-metadata-list-summary-item")

    movies = []

    for item in items:
        title_tag = item.select_one("h3")
        title = title_tag.text.strip() if title_tag else "Sem título"
        year_tag = item.select_one("span.ipc-metadata-list-summary-item__li")
        try:
            year = int(year_tag.text.strip()) if year_tag else 0
        except:
            year = 0
        rating_tag = item.select_one("span.ipc-rating-star--rating")
        try:
            rating = float(rating_tag.text.strip()) if rating_tag else 0.0
        except:
            rating = 0.0

        movies.append({
            "title": title,
            "year": year,
            "rating": rating,
        })

        if limit and len(movies) >= limit:
            break

    return movies

def get_movies_from_imdb() -> List[Movie]:
    config = load_config()
    url = config["imdb_url"]
    limit = config.get("n_filmes", 250)

    html = fetch_imdb_html(url)
    movies_dicts = parse_top_250(html, limit)

    movies = [
        Movie(m["title"], m["year"], m["rating"])
        for m in movies_dicts
    ]

    return movies
