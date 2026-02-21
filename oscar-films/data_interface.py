from data import CATEGORIES, FILMS


def get_films_for_name(name):
    matches = {}
    for film in FILMS:
        for member in FILMS[film]["cast_and_crew"]:
            if name.lower() in member.lower():
                if member not in matches:
                    matches[member] = []
                matches[member].append(film)

    return matches


def get_all_categories():
    return CATEGORIES


def get_categories_for_sbstr(substring):
    matches = filter(lambda x: substring.lower() in x.lower(), CATEGORIES)
    matches = list(matches)
    matches.sort()

    return matches


def get_films_for_category(category):
    matches = []
    for film in FILMS:
        if category in FILMS[film]["category"]:
            matches.append(film)
    matches.sort()
    return matches
