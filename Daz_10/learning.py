def format_name(f_name: str, l_name: str) -> str:
    """
    Formats the given first name and last name into a single string in title case.
    :param f_name: First name
    :param l_name: Last name
    :exception ValueError: If either `f_name` or `l_name` is an empty string.
    :return: The formatted name in title case.
    """
    if f_name == "" or l_name == "":
        raise ValueError("One or more arguments are empty.")
    return f"{f_name.title()} {l_name.title()}"


print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
