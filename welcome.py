import time
import random

def create_name_banner(name):
    # Calculate the width needed for the name
    width = len(name) + 10  # Add some padding
    
    # Create the top and bottom borders
    top = "╔" + "═" * width + "╗"
    bottom = "╚" + "═" * width + "╝"
    middle = "║" + " " * width + "║"
    
    # Create the name line with proper centering
    padding = (width - len(name)) // 2
    name_line = "║" + " " * padding + name + " " * (width - padding - len(name)) + "║"
    
    # Combine all parts
    banner = f"""
    {top}
    {middle}
    {name_line}
    {middle}
    {bottom}
    """
    return banner

def create_decorative_element():
    return """
    ✧･ﾟ: *✧･ﾟ:*  *:･ﾟ✧*:･ﾟ✧
    """

def animate_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def create_welcome_message(name):
    # Special responses for certain names
    if name.lower() == "neo":
        return "The One has returned... Welcome back, Mr. Anderson."
    elif name.lower() == "morpheus":
        return "The captain of the Nebuchadnezzar... Welcome, Morpheus."
    elif name.lower() == "trinity":
        return "The last of the hovercrafts... Welcome, Trinity."
    elif name.lower() == "smith":
        return "Mr. Anderson... I mean, Mr. Smith. How unexpected."
    elif name.lower() == "oracle":
        return "The mother of the Matrix... Welcome, Oracle."
    else:
        # Random welcome messages for other names
        messages = [
            f"Mr. {name}... I've been expecting you.",
            f"Welcome to the Matrix, {name}.",
            f"Take the red pill, {name}...",
            f"The Matrix has you, {name}...",
            f"Follow the white rabbit, {name}..."
        ]
        return random.choice(messages)

def get_matrix_quote():
    quotes = [
        "There is no spoon.",
        "I know kung fu.",
        "The Matrix has you...",
        "Free your mind.",
        "There is no escaping the Matrix."
    ]
    return random.choice(quotes)

def main():
    # Get the user's name
    name = input("Please enter your first name: ")
    
    # Display the decorative element
    print(create_decorative_element())
    
    # Display the ASCII banner with the name
    print(create_name_banner(name))
    
    # Add dramatic pause
    print("\n    ", end='')
    time.sleep(1.5)  # Dramatic pause before the message
    
    # Display the welcome message with animation
    animate_text(create_welcome_message(name))
    
    # Add a random Matrix quote with a pause
    if random.random() < 0.3:  # 30% chance to show an additional quote
        time.sleep(1)
        print("\n    ", end='')
        animate_text(get_matrix_quote(), delay=0.03)

if __name__ == "__main__":
    main()