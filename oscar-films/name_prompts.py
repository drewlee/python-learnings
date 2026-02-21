from validators import is_valid_num_option
from shared_prompts import prompt_yes_no, get_selection_msg, prompt_selection_list
from data_interface import get_films_for_name


def prompt_for_name():
    msg = "Enter a full or partial name of a cast or crew member:\n"
    name = input(msg)
    name = name.strip()

    if not name:
        print("Invalid entry\n")
        return prompt_for_name()

    films = get_films_for_name(name)
    if films:
        members = list(films.keys())
        members.sort()
        selection_msg = get_selection_msg("member", "members", len(members), name)
        selected = prompt_selection_list(members, selection_msg)

        # Recommendations
        return films[selected]

    print(f'No matches found for "{name}". Try again?')
    should_reprompt = prompt_yes_no()
    if should_reprompt:
        print("\n")
        return prompt_for_name()
