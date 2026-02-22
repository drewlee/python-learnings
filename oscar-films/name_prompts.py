from shared_prompts import (
    prompt_yes_no,
    get_selection_msg,
    prompt_selection_list,
)
from data_interface import get_films_for_name


def prompt_for_name():
    msg = "Enter a full or partial name of a cast or crew member:\n"
    name = input(msg).strip()

    if not name:
        print("Invalid entry\n")
        return prompt_for_name()

    films = get_films_for_name(name)
    if films:
        members = list(films.keys())
        members.sort()
        selection_msg = get_selection_msg("member", "members", len(members), name)
        selected_idx = prompt_selection_list(members, selection_msg)
        member = members[selected_idx]
        return films[member], member

    print(f'No matches found for "{name}". Try again?')
    should_re_prompt = prompt_yes_no()
    if should_re_prompt:
        print("\n")
        return prompt_for_name()

    return None
