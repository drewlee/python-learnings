def is_valid_num_option(option, min_allowed=1, max_allowed=10):
    if not option:
        return False

    try:
        option_num = int(option)
        if option_num < min_allowed or option_num > max_allowed:
            return False
    except ValueError:
        return False

    return True


def is_valid_yes_no_option(option):
    return option.lower() == "y" or option.lower() == "n"
