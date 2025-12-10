import os
import pandas as pd
from sqlalchemy import create_engine


def get_engine(db_path="data/imdb.db"):
    return create_engine(f"sqlite:///{db_path}")


def load_dataframes():
    try:
        engine = get_engine()
        movies = pd.read_sql_table("movies", con=engine)
        series = pd.read_sql_table("series", con=engine)
        return movies, series
    except Exception as e:
        print("Erro ao carregar DataFrames:", e)
        return None, None


def analyze_and_export(movies_df, series_df):
    sorted_df = movies_df.sort_values("rating", ascending=False)
    top9 = sorted_df[sorted_df["rating"] > 9.0]

    print("\nTop 5 filmes com nota > 9.0:")
    print(top9[["title", "rating"]].head(5))

    os.makedirs("data", exist_ok=True)

    try:
        movies_df.to_csv("data/movies.csv", index=False)
        series_df.to_csv("data/series.csv", index=False)

        movies_df.to_json("data/movies.json", orient="records", force_ascii=False)
        series_df.to_json("data/series.json", orient="records", force_ascii=False)

        print("\nArquivos exportados com sucesso!")
    except Exception as e:
        print("Erro ao exportar arquivos:", e)


def classify_rating(r):
    if r >= 9.0:
        return "Obra-prima"
    if r >= 8.0:
        return "Excelente"
    if r >= 7.0:
        return "Bom"
    return "Mediano"


def add_category_column(df):
    df = df.copy()
    df["categoria"] = df["rating"].apply(classify_rating)
    return df


def summary_by_category_year(df):
    return (
        df.groupby(["categoria", "year"])["id"]
        .count()
        .reset_index(name="qtd_filmes")
    )
