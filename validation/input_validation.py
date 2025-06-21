"""
Input validation functions.
"""

def validate_name(name):
    """Validate the user's name input."""
    if not name.strip():
        return False, "The Matrix cannot process an empty name."
    if len(name) > 20:
        return False, "That name is too long for the Matrix to process."
    if any(char in name for char in "!@#$%^&*()_+{}|:<>?"):
        return False, "The Matrix only accepts standard characters."
    return True, name.strip()

def get_user_choice():
    """Get and validate the user's pill choice."""
    print("\n    Choose your path:")
    print("    1. Take the red pill")
    print("    2. Take the blue pill")
    while True:
        try:
            choice = input("    Enter your choice (1 or 2): ")
            if choice in ['1', '2']:
                return choice
            print("    Invalid choice. The Matrix requires a clear decision.")
        except:
            print("    The Matrix cannot process that input.") 