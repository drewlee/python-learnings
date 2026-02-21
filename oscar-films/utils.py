import shutil


def get_divider_line():
    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    out = "-" * width + "\n"
    return out


def print_divider():
    out = get_divider_line()
    print(out)
