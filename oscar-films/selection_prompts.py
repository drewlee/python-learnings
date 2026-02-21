from shared_prompts import prompt_selection_list


def prompt_for_selection():
    select_options = [
        "Award category",
        "Genre",
        "Name of cast or crew member",
    ]
    print("Get a list of film recommendations?")

    selection_msg = "You can find films by:\n"
    selected_idx = prompt_selection_list(select_options, selection_msg)
    return selected_idx
