from selection_prompts import prompt_for_selection
from category_prompts import prompt_for_category
from genre_prompts import prompt_for_genre
from name_prompts import prompt_for_name


def print_film_recs(films, item):
    print(f'Film recommendations based on "{item}":\n')
    # TODO: pretty print the recommend films
    for film in films:
        print(film)


def run():
    selection = prompt_for_selection()
    recs = None

    if selection == 1:
        recs = prompt_for_category()
    elif selection == 2:
        recs = prompt_for_genre()
    elif selection == 3:
        recs = prompt_for_name()
    else:
        # It shouldn't be possible to get here
        raise Exception("Invalid selection value")

    if recs and len(recs) == 2:
        print_film_recs(recs[0], recs[1])


run()
