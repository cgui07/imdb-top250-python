class TV:
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"


class Movie(TV):
    def __init__(self, title: str, year: int, rating: float):
        super().__init__(title, year)
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) – Nota: {self.rating:.1f}"


class Series(TV):
    def __init__(self, title: str, year: int, seasons: int, episodes: int):
        super().__init__(title, year)
        self.seasons = seasons
        self.episodes = episodes

    def __str__(self):
        return (
            f"{self.title} ({self.year}) - "
            f"Temporadas: {self.seasons}, Episódios: {self.episodes}"
        )
