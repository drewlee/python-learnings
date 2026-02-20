from validators import is_valid_num_option, is_valid_yes_no_option
from data_interface import get_films_for_name


def prompt_for_category(is_retry=False):
    msg = ""
    if not is_retry:
        msg += "Would you like a list of film recommendations?\n"

    msg += "You can find films by:\n" +\
        "  1. Award category\n" +\
        "  2. Genre, or\n" +\
        "  3. Name of a cast or crew member\n" +\
        "\n" +\
        "To begin, enter a number corresponding to one of the options:\n"

    option = input(msg)
    option = option.strip()
    is_valid = is_valid_num_option(option, maxAllowed=3)

    if not is_valid:
        print(f'"{option}" is not a valid option\n')
        return prompt_for_category(True)

    option_int = int(option)
    categories = [
        "award category",
        "genre",
        "name of cast or crew member",
    ]

    print(f"Selected recommendation by {categories[option_int - 1]}\n")
    return option_int


def prompt_for_name():
    msg = "Enter a full or partial name of a cast or crew member:\n"
    name = input(msg)
    name = name.strip()

    if not name:
        print("Invalid entry")
        prompt_for_name()
        return

    films = get_films_for_name(name)
    if films:
        members = list(films.keys())
        members.sort()
        selected = prompt_for_name_selection(name, members)
        # Recommendations
        print(films[selected])
    else:
        print(f"No matches found for {name}")
        should_reprompt = prompt_for_new_name()
        if should_reprompt:
            prompt_for_name()


def prompt_for_new_name():
    msg = 'Try a different name? Enter "y" for yes or "n" for no\n'
    option = input(msg)
    option = option.strip()
    is_valid = is_valid_yes_no_option(option)

    if not is_valid:
        print(f'"{option}" is not a valid option\n')
        return prompt_for_new_name()

    return option == 'y'


def prompt_for_name_selection(name, members):
    members_len = len(members)
    print(f'There are {members_len} members matching "{name}":')
    for i in range(members_len):
        print(f"  {i + 1}. {members[i]}")

    msg = "Enter a number corresponding to one of the options:\n"
    option = input(msg)
    option = option.strip()
    is_valid = is_valid_num_option(option, maxAllowed=members_len)

    if not is_valid:
        print(f'"{option}" is not a valid option\n')
        return prompt_for_name_selection(name, members)

    option_int = int(option)
    member = members[option_int - 1]
    print(f"Selected {member}\n")

    return member
