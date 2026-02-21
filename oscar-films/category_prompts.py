from data_interface import (
    get_all_categories,
    get_categories_for_sbstr,
    get_films_for_category,
)
from shared_prompts import prompt_yes_no, prompt_selection_list, get_selection_msg


def prompt_for_category():
    prompt = (
        "Enter the full or partial name of an award category\n"
        'such as, "supporting actress" or "best picture".\n'
        'Or enter "list" to select from a list of categories:\n'
    )
    substring = input(prompt).strip()

    if not substring:
        print("Invalid entry\n")
        return prompt_for_category()

    if substring == "list":
        categories = get_all_categories()
        selection_msg = f"There are {len(categories)} award categories:\n"
    else:
        categories = get_categories_for_sbstr(substring)
        selection_msg = None

    if categories:
        if not selection_msg:
            selection_msg = get_selection_msg(
                "category", "categories", len(categories), substring
            )
        category = prompt_selection_list(categories, selection_msg)
        films = get_films_for_category(category)
        return films

    print(f'\nNo matches found for "{substring}". Try again?')
    should_re_prompt = prompt_yes_no()
    if should_re_prompt:
        print("\n")
        return prompt_for_category()


def prompt_for_category_selection(name, options):
    options_len = len(options)
    print("\n" + f'There are {options_len} categories matching "{name}"')
    for i in range(options_len):
        print(f"  {i + 1}. {options[i]}")

    msg = "Enter a number corresponding to one of the options:\n"
    print(msg)
