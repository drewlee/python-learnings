from validators import is_valid_yes_no_option, is_valid_num_option
import shutil


def print_divider():
    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print("-" * width + "\n")


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

    if options_len > 1:
        prompt = "Enter a number corresponding to an option:\n"
        option = input(prompt).strip()
        is_valid = is_valid_num_option(option, maxAllowed=options_len)

        if not is_valid:
            print(f'"{option}" is not a valid option\n')
            return prompt_selection_list(options, lead_msg)

        option_int = int(option)
        index = option_int - 1
        selected = options[index]
        confirmation = f'Selected "{selected}"'

        print("\n" + confirmation)
        print_divider()

        return index

    print_divider()
    return 0
