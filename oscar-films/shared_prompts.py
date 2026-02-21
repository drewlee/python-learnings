from validators import is_valid_yes_no_option, is_valid_num_option


def get_selection_msg(s_noun, pl_noun, count, token):
    noun = s_noun if count == 1 else pl_noun
    is_are = "is" if count == 1 else "are"
    out = f'There {is_are} {count} {noun} matching "{token}":\n'

    return out


def prompt_yes_no():
    msg = 'Enter "y" for yes or "n" for no:\n'
    option = input(msg).strip()
    is_valid = is_valid_yes_no_option(option)

    if not is_valid:
        print(f'"{option}" is not a valid option\n')
        return prompt_yes_no()

    return option == "y"


def prompt_selection_list(options, lead_msg):
    options_len = len(options)
    out = "\n" + lead_msg
    for i in range(options_len):
        out += f"  {i + 1}. {options[i]}\n"
    print(out)

    prompt = "Enter a number corresponding to one of the options:\n"
    option = input(prompt).strip()
    is_valid = is_valid_num_option(option, maxAllowed=options_len)

    if not is_valid:
        print(f'"{option}" is not a valid option\n')
        return prompt_selection_list(options, lead_msg)

    option_int = int(option)
    selected = options[option_int - 1]
    print(f'Selected "{selected}"\n')
    return selected
