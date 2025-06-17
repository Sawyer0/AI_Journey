import time
import random
from datetime import datetime

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
    # Different decorative elements based on time of day
    hour = datetime.now().hour
    
    def get_time_emoji():
        if 5 <= hour < 12:
            return "☀️"
        elif 12 <= hour < 17:
            return "🌞"
        elif 17 <= hour < 22:
            return "🌅"
        else:
            return "🌙"
    
    def get_time_greeting():
        if 5 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 17:
            return "Afternoon"
        elif 17 <= hour < 22:
            return "Evening"
        else:
            return "Night"
    
    emoji = get_time_emoji()
    greeting = get_time_greeting()
    
    # Create a dynamic decorative line
    line = "=" * (len(greeting) + 20)
    return f"""
    {line}
    {emoji} {greeting} in the Matrix {emoji}
    {line}
    """

def animate_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def analyze_name(name):
    # Analyze the name for special characteristics
    analysis = []
    
    def check_name_length():
        if len(name) > 10:
            return "Your name is quite long, like the endless corridors of the Matrix."
        elif len(name) < 4:
            return "A short name, efficient like the machines."
        return None
    
    def check_name_composition():
        if name.isalpha():
            return "A pure name, untainted by numbers."
        elif any(char.isdigit() for char in name):
            return "Your name contains numbers, like the Matrix's code."
        return None
    
    def check_name_case():
        if name[0].isupper():
            return "Starting with a capital letter, like a new beginning."
        return None
    
    # Run all checks and collect results
    checks = [check_name_length, check_name_composition, check_name_case]
    for check in checks:
        result = check()
        if result:
            analysis.append(result)
    
    return analysis

def create_welcome_message(name):
    # Special responses for certain names
    def get_special_response():
        special_names = {
            "neo": "The One has returned... Welcome back, Mr. Anderson.",
            "morpheus": "The captain of the Nebuchadnezzar... Welcome, Morpheus.",
            "trinity": "The last of the hovercrafts... Welcome, Trinity.",
            "smith": "Mr. Anderson... I mean, Mr. Smith. How unexpected.",
            "oracle": "The mother of the Matrix... Welcome, Oracle."
        }
        return special_names.get(name.lower())
    
    def get_random_message():
        messages = [
            f"Mr. {name}... I've been expecting you.",
            f"Welcome to the Matrix, {name}.",
            f"Take the red pill, {name}...",
            f"The Matrix has you, {name}...",
            f"Follow the white rabbit, {name}..."
        ]
        return random.choice(messages)
    
    # Try to get a special response, fall back to random if none exists
    return get_special_response() or get_random_message()

def get_matrix_quote():
    quotes = [
        "There is no spoon.",
        "I know kung fu.",
        "The Matrix has you...",
        "Free your mind.",
        "There is no escaping the Matrix.",
        "The Matrix is everywhere.",
        "I'm going to show you how deep the rabbit hole goes.",
        "You take the blue pill, the story ends.",
        "You take the red pill, you stay in Wonderland.",
        "I'm trying to free your mind.",
        "But I can only show you the door.",
        "You have to walk through it.",
        "The Matrix is a system, Neo.",
        "That system is our enemy.",
        "When you're ready, you won't have to."
    ]
    return random.choice(quotes)

def validate_name(name):
    if not name.strip():
        return False, "The Matrix cannot process an empty name."
    if len(name) > 20:
        return False, "That name is too long for the Matrix to process."
    if any(char in name for char in "!@#$%^&*()_+{}|:<>?"):
        return False, "The Matrix only accepts standard characters."
    return True, name.strip()

def get_user_choice():
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

def get_pill_response(choice, name):
    if choice == '1':
        return f"{name}, you've chosen the red pill.\nThe Matrix will show you how deep the rabbit hole goes..."
    else:
        return f"{name}, you've chosen the blue pill.\nYou will wake up in your bed and believe whatever you want to believe..."

def main():
    # Get and validate the user's name
    while True:
        name = input("Please enter your first name: ")
        is_valid, message = validate_name(name)
        if is_valid:
            name = message
            break
        print(f"\n    {message}")
        print("    Please try again.")
    
    # Display the time-based decorative element
    print(create_decorative_element())
    
    # Display the ASCII banner with the name
    print(create_name_banner(name))
    
    # Add dramatic pause
    print("\n    ", end='')
    time.sleep(1.5)  # Dramatic pause before the message
    
    # Analyze the name and display insights first
    name_analysis = analyze_name(name)
    if name_analysis:
        print("\n    ", end='')
        animate_text("Analyzing your name in the Matrix...", delay=0.03)
        time.sleep(0.5)
        for insight in name_analysis:
            print("    ", end='')
            animate_text(insight, delay=0.03)
    
    # Display the welcome message with animation
    time.sleep(1)
    print("\n    ", end='')
    animate_text(create_welcome_message(name))
    
    # Get user's pill choice
    choice = get_user_choice()
    
    # Display pill response
    time.sleep(1)
    print("\n    ", end='')
    animate_text(get_pill_response(choice, name))
    
    # Display Matrix quotes
    time.sleep(1)
    print("\n    ", end='')
    animate_text("The Matrix speaks...", delay=0.03)
    time.sleep(0.5)
    
    # Display quotes with animation
    print("    ", end='')
    animate_text(get_matrix_quote(), delay=0.03)
    
    # 50% chance for a second quote
    if random.random() < 0.5:
        time.sleep(0.5)
        print("    ", end='')
        animate_text(get_matrix_quote(), delay=0.03)
    
    # 25% chance for a third quote
    if random.random() < 0.25:
        time.sleep(0.5)
        print("    ", end='')
        animate_text(get_matrix_quote(), delay=0.03)

if __name__ == "__main__":
    main()