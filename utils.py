# project_flow/utils.py
# Introduce a separate module for utility functions
def validate_user_input(input_data):
    username = input_data.get("username")
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    # ... (Other validation rules)
    return input_data
