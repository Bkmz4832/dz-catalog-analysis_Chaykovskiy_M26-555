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

print(average_rating(test_movies))
print(catalog_age_stats(test_movies))
print(convert_minutes(135))