def format_name(first_name, last_name):

    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs"

    first_name = first_name.title()
    last_name = last_name.title()

    return f"Result: {first_name} {last_name}"

print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
