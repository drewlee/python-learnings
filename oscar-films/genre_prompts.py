from data_interface import (
    get_all_genres,
    get_genres_for_sbstr,
    get_films_for_genre,
)
from shared_prompts import (
    get_selection_msg,
    prompt_selection_list,
    prompt_yes_no,
)


def format_genres(genres):
    return list(map(lambda x: x[0].upper() + x[1:], genres))


def prompt_for_genre():
    prompt = (
        "Enter the full or partial name of a film genre\n"
        'such as "drama" or "documentary".\n'
        'Or enter "list" to select from a list of genres.\n'
    )
    substring = input(prompt).strip()

    if not substring:
        print("Invalid entry\n")
        return prompt_for_genre()

    if substring == "list":
        genres = get_all_genres()
        selection_msg = f"There are {len(genres)} genres:\n"
    else:
        genres = get_genres_for_sbstr(substring)
        selection_msg = None

    if genres:
        if not selection_msg:
            selection_msg = get_selection_msg("genre", "genres", len(genres), substring)
        genres = format_genres(genres)
        selected_idx = prompt_selection_list(genres, selection_msg)
        genre = genres[selected_idx]
        films = get_films_for_genre(genre.lower())
        return films, genre

    print(f'\nNo matches found for "{substring}". Try again?')
    should_re_prompt = prompt_yes_no()
    if should_re_prompt:
        print("\n")
        return prompt_for_genre()
