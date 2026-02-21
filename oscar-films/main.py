from selection_prompts import prompt_for_selection
from category_prompts import prompt_for_category
from genre_prompts import prompt_for_genre
from name_prompts import prompt_for_name
from shared_prompts import prompt_yes_no
from utils import get_divider_line, print_divider


def print_film_recs(films, criteria):
    # print(films)
    out = f'Film recommendations based on "{criteria}":\n'
    # out += get_divider_line()
    for film in films:
        # Film name
        out += f"\n  {film["name"]}\n\n"

        # Nominations
        out += "    Nominated for:\n"
        for item in film["category"]:
            out += f"    - {item}\n"
        out += "\n"

        out += get_divider_line()
    print(out)


def run():
    intro = (
        "  The 98th Academy Awards feature a wide assortment of exciting\n"
        "  and intriguing contenders! Explore the catalog of titles based on\n"
        "  nominations, leading stars, and other distinguishing criteria.\n"
    )
    print_divider()
    print(intro)
    print_divider()

    while True:
        selection = prompt_for_selection()
        recs = None

        if selection == 0:
            recs = prompt_for_category()
        elif selection == 1:
            recs = prompt_for_genre()
        elif selection == 2:
            recs = prompt_for_name()
        else:
            raise Exception("Invalid selection value")

        if recs and len(recs) == 2:
            films, criteria = recs
            print_film_recs(films, criteria)

            print("Get more recommendations?")
            if not prompt_yes_no():
                break
        else:
            raise Exception("Invalid recommendations format")


if __name__ == "__main__":
    run()
