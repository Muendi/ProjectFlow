
def validate_user_input(input_data):
    username = input_data.get("username")
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")

    return input_data
