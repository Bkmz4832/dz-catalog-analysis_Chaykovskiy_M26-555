import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# ЭТАП 1. Числа и математические операции

def average_rating(movies):
    """Возвращает среднюю оценку фильмов."""
    total = 0

    for movie in movies:
        total += movie["rating"]

    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает статистику возраста фильмов."""
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    oldest_age = max(ages)
    newest_age = min(ages)
    average_age = math.ceil(sum(ages) / len(ages)) 

    return oldest_age, newest_age, average_age


def duration_in_hours(minutes):
    """Преобразует минуты в строку с часами и минутами."""
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"


# ЭТАП 2. Условия и сопоставление с образцом

def rating_tier(rating):
    """Определяет категорию фильма по рейтингу."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Определяет категорию фильма по году выпуска."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# ЭТАП 3. Циклы

def print_non_comedy_titles(movies):
    """Выводит названия фильмов, не относящихся к комедиям."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue

        print(movie["title"])


def find_first_masterpiece(movies):
    """Находит первый фильм с рейтингом выше 9.0."""
    index = 0

    while index < len(movies):
        movie = movies[index]

        if movie["rating"] > 9.0:
            print(f"Найден фильм: {movie['title']}")
            break

        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее заданной продолжительности."""
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count


# ЭТАП 4. Работа со строками

def normalize_title(title):
    """Приводит название фильма к правильному регистру."""
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_words.append(word[0].upper() + word[1:])

    return " ".join(normalized_words)


def make_slug(title):
    """Создаёт slug из названия фильма."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Формирует строку с информацией о фильме."""
    title = normalize_title(movie["title"])
    rating = movie["rating"]
    year = movie["year"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({year}) — {rating}/10, '
        f"{duration}, жанры: {genres}"
    )


# ЭТАП 5. Сортировка

def titles_sorted_by_rating(movies):
    """Возвращает названия фильмов по убыванию рейтинга."""
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Возвращает первые n фильмов в виде пар (название, рейтинг)."""
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    return [
        (movie["title"], movie["rating"])
        for movie in sorted_movies[:n]
    ]


# ЭТАП 6. Словари

def count_by_genre(movies):
    """Подсчитывает количество фильмов каждого жанра."""
    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts


def actor_filmography(movies):
    """Создаёт список фильмов для каждого актёра."""
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []

            filmography[actor].append(movie["title"])

    return filmography


above_average_movies = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average_rating(movies)
}


# ЭТАП 7. Множества

def all_genres(movies):
    """Возвращает множество всех уникальных жанров."""
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres


def common_actors(movie1, movie2):
    """Возвращает общих актёров двух фильмов."""
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])

    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры первого каталога, отсутствующие во втором."""
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b


# ЭТАП 8. Генераторы

def iter_high_rated(movies, min_rating=8.0):
    """Возвращает фильмы с рейтингом не ниже заданного."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# ЭТАП 9. Итоговый отчёт

def build_report(movies):
    """Формирует итоговый отчёт по каталогу фильмов."""

    print("ОТЧЁТ ПО КАТАЛОГУ")

    print(f"Средний рейтинг: {average_rating(movies)}")

    _, _, average_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {average_age} лет")

    print("\nТоп-3 фильма:")

    for title, _rating in top_n_by_rating(movies, 3):
        movie = next(
            movie for movie in movies
            if movie["title"] == title
        )
        print(f"  {format_report_line(movie)}")

    print("\nФильмов по жанрам:")

    genre_counts = count_by_genre(movies)

    for genre, count in sorted(
        genre_counts.items(),
        key=lambda item: (-item[1], item[0]),
    ):
        print(f"  {genre} — {count}")

    genres = sorted(all_genres(movies))
    print("\nВсе жанры каталога:", ", ".join(genres))

    total_duration = sum(
        movie["duration_min"]
        for movie in movies
        if movie["rating"] > 7
    )

    print(
        "\nОбщая продолжительность фильмов "
        f"с рейтингом выше 7: {total_duration} минут"
    )


if __name__ == "__main__":
    build_report(movies)