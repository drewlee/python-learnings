from functools import reduce
from validators import is_valid_num_option


def get_select_options(options):
    out = ""
    for i in range(len(options)):
        out += f"  {i + 1}. {options[i]}\n"
    return out


def prompt_for_selection(is_retry=False):
    select_options = [
        "Award category",
        "Genre",
        "Name of cast or crew member",
    ]

    if not is_retry:
        print("Would you like a list of film recommendations?\n")

    prompt = "You can find films by:\n"
    prompt += get_select_options(select_options) + "\n"
    prompt += "To begin, enter the number corresponding to an option:\n"

    option = input(prompt)
    option = option.strip()
    is_valid = is_valid_num_option(option, maxAllowed=3)

    if not is_valid:
        print(f'"{option}" is not a valid option\n')
        return prompt_for_selection(True)

    option_int = int(option)

    confirmation = f"Selected recommendation by: {select_options[option_int - 1]}"
    print("\n" + confirmation + "\n")
    print("-" * len(confirmation) + "\n")

    return option_int
