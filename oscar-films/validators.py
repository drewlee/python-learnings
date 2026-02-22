def is_valid_num_option(option, minAllowed=1, maxAllowed=10):
    if not option:
        return False

    try:
        option_num = int(option)
        if option_num < minAllowed or option_num > maxAllowed:
            return False
    except ValueError:
        return False

    return True


def is_valid_yes_no_option(option):
    return option.lower() == "y" or option.lower() == "n"
