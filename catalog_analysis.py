import math


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

test_movies = [
    {"title": "Фильм 1", "year": 2000, "rating": 8.5},
    {"title": "Фильм 2", "year": 2020, "rating": 7.5},
    {"title": "Фильм 3", "year": 2010, "rating": 9.0},
]

def rating_tier(rating):
    """Определяет категорию фильма по рейтингу."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне" if rating >= 5 else "слабо"
    else:
        return "слабо"


def decade_label(year):
    """Определяет категорию фильма по году выпуска."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


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

    return f"{title} ({year}) | Оценка: {rating} | {duration} | Жанры: {genres}"

test_movie = {
    "title": "the silent city",
    "year": 2020,
    "rating": 8.5,
    "duration_min": 155,
    "genres": {"drama", "thriller"},
}

print(format_report_line(test_movie))

print(make_slug("Silent Hours"))
print(average_rating(test_movies))
print(catalog_age_stats(test_movies))
print(duration_in_hours(155))
print(rating_tier(9.5))
print(rating_tier(8.2))
print(rating_tier(6.0))
print(rating_tier(3.5))
print(decade_label(2024))
print(decade_label(2018))
print(decade_label(2010))
print(decade_label(2020))