from shared_prompts import prompt_selection_list
from validators import is_valid_num_option


def get_select_options(options):
    out = ""
    for i in range(len(options)):
        out += f"  {i + 1}. {options[i]}\n"
    return out


def prompt_for_selection():
    select_options = [
        "Award category",
        "Genre",
        "Name of cast or crew member",
    ]
    print("Would you like a list of film recommendations?")

    selection_msg = "You can find films by:\n"
    selected_idx = prompt_selection_list(select_options, selection_msg)
    return selected_idx
