from prompts import prompt_for_category, prompt_for_name


def run():
    category = prompt_for_category()
    recommendations = None

    if category == 1:
        pass
    elif category == 2:
        pass
    elif category == 3:
        recommendations = prompt_for_name()
    else:
        pass

    if recommendations:
        # Print the recommendations
        # f"Film recommendations based on {}"
        pass


run()
