from data import CATEGORIES, GENRES, FILMS


def get_all_categories():
    return CATEGORIES


def get_all_genres():
    return GENRES


def get_matches_for_substr(substring, collection):
    matches = filter(lambda x: substring.lower() in x.lower(), collection)
    matches = list(matches)
    matches.sort()
    return matches


def get_categories_for_sbstr(substring):
    return get_matches_for_substr(substring, CATEGORIES)


def get_genres_for_sbstr(substring):
    return get_matches_for_substr(substring, GENRES)


def get_films_for_entity(entity, key):
    matches = []
    for film in FILMS:
        if entity in FILMS[film][key]:
            matches.append(film)
    matches.sort()
    return matches


def get_films_for_genre(genre):
    return get_films_for_entity(genre, "genre")


def get_films_for_category(category):
    return get_films_for_entity(category, "category")


def get_films_for_name(name):
    matches = {}
    for film in FILMS:
        for member in FILMS[film]["cast_and_crew"]:
            if name.lower() in member.lower():
                if member not in matches:
                    matches[member] = []
                matches[member].append(film)

    return matches
