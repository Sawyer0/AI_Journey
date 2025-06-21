"""
Message and response handling functions.
"""
import random

def create_welcome_message(name):
    """Create a personalized welcome message."""
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
    
    return get_special_response() or get_random_message()

def get_matrix_quote(choice):
    """Get a random Matrix quote based on pill choice."""
    red_pill_quotes = [
        "There is no spoon.",
        "I know kung fu.",
        "The Matrix has you...",
        "Free your mind.",
        "There is no escaping the Matrix.",
        "The Matrix is everywhere.",
        "I'm going to show you how deep the rabbit hole goes.",
        "You take the red pill, you stay in Wonderland.",
        "I'm trying to free your mind.",
        "But I can only show you the door.",
        "You have to walk through it.",
        "The Matrix is a system, Neo.",
        "That system is our enemy.",
        "When you're ready, you won't have to."
    ]
    
    blue_pill_quotes = [
        "The Matrix has you...",
        "You take the blue pill, the story ends.",
        "You wake up in your bed and believe whatever you want to believe.",
        "The Matrix is the world that has been pulled over your eyes.",
        "What you know you can't explain, but you feel it.",
        "You've been living in a dream world.",
        "The Matrix is everywhere.",
        "It is all around us.",
        "Even now, in this very room.",
        "You can see it when you look out your window.",
        "Or when you turn on your television.",
        "You can feel it when you go to work.",
        "When you go to church.",
        "When you pay your taxes."
    ]
    
    return random.choice(red_pill_quotes if choice == '1' else blue_pill_quotes)

def get_pill_response(choice, name):
    """Get the response based on the pill choice."""
    if choice == '1':
        return f"{name}, you've chosen the red pill.\nThe Matrix will show you how deep the rabbit hole goes..."
    else:
        return f"{name}, you've chosen the blue pill.\nYou will wake up in your bed and believe whatever you want to believe..."

def analyze_name(name):
    """Analyze the name for special characteristics."""
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
    
    checks = [check_name_length, check_name_composition, check_name_case]
    for check in checks:
        result = check()
        if result:
            analysis.append(result)
    
    return analysis 