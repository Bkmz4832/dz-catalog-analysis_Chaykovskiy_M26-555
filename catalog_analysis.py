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


def convert_minutes(minutes):
    """Преобразует минуты в часы и оставшиеся минуты."""
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return hours, remaining_minutes

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

print(average_rating(test_movies))
print(catalog_age_stats(test_movies))
print(convert_minutes(135))
print(rating_tier(9.5))
print(rating_tier(8.2))
print(rating_tier(6.0))
print(rating_tier(3.5))
print(decade_label(2024))
print(decade_label(2018))
print(decade_label(2010))
print(decade_label(2020))