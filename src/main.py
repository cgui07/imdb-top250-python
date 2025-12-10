from .scraping import get_movies_from_imdb
from .models import Series
from .db import (
    get_engine,
    create_tables,
    get_session,
    insert_movies,
    insert_series,
)
from .analysis import (
    load_dataframes,
    analyze_and_export,
    add_category_column,
    summary_by_category_year,
)


def main():
    print("Criando banco...")
    engine = get_engine()
    create_tables(engine)
    session = get_session(engine)

    print("Fazendo scraping do IMDb...")
    movies = get_movies_from_imdb()

    print("Criando séries...")
    series_list = [
        Series("Breaking Bad", 2008, seasons=5, episodes=62),
        Series("Game of Thrones", 2011, seasons=8, episodes=73),
    ]

    print("Inserindo dados no banco...")
    insert_movies(movies, session)
    insert_series(series_list, session)

    print("Carregando DataFrames...")
    movies_df, series_df = load_dataframes()

    print("\n5 primeiros filmes:")
    print(movies_df.head())

    print("\n5 primeiras séries:")
    print(series_df.head())

    print("\nExportando e analisando...")
    analyze_and_export(movies_df, series_df)

    movies_cat = add_category_column(movies_df)
    print("\nFilmes com categorias:")
    print(movies_cat[["title", "rating", "categoria"]].head(10))

    print("\nResumo por categoria e ano:")
    resumo = summary_by_category_year(movies_cat)
    print(resumo.head(20))


if __name__ == "__main__":
    main()
