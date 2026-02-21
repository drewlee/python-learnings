from selection_prompts import prompt_for_selection
from name_prompts import prompt_for_name
from category_prompts import prompt_for_category


def print_film_recs(recs):
    print(f"Film recommendations based on {None}:\n")
    print(recs)


def run():
    selection = prompt_for_selection()
    recs = None

    if selection == 1:
        recs = prompt_for_category()
    elif selection == 2:
        pass
    elif selection == 3:
        recs = prompt_for_name()
    else:
        # It shouldn't be possible to get here
        raise Exception("Invalid selection value")

    if recs:
        # TODO: pretty print the recommend films
        print_film_recs(recs)


run()
