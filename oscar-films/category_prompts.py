from data_interface import (
    get_all_categories,
    get_categories_for_sbstr,
    get_films_for_category,
)
from shared_prompts import (
    prompt_yes_no,
    prompt_selection_list,
    get_selection_msg,
)


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
        selected_idx = prompt_selection_list(categories, selection_msg)
        category = categories[selected_idx]
        films = get_films_for_category(category)
        return films, category

    print(f'\nNo matches found for "{substring}". Try again?')
    should_re_prompt = prompt_yes_no()
    if should_re_prompt:
        print("\n")
        return prompt_for_category()
