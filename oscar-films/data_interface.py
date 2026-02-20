from data import FILMS


def get_films_for_name(name):
    matches = {}

    for film in FILMS:
        for member in FILMS[film]["cast_and_crew"]:
            if name.lower() in member.lower():
                if member not in matches:
                    matches[member] = []
                matches[member].append(film)

    return matches
