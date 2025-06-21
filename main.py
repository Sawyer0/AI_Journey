"""
Main program for the Matrix welcome script.
"""
import time
import random

from display.animation import animate_text, create_name_banner, create_decorative_element
from messages.responses import create_welcome_message, get_matrix_quote, get_pill_response, analyze_name
from validation.input_validation import validate_name, get_user_choice

def main():
    """Main program execution."""
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
    time.sleep(1.5)
    
    # Analyze the name and display insights
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
    animate_text(get_matrix_quote(choice), delay=0.03)
    
    # 50% chance for a second quote
    if random.random() < 0.5:
        time.sleep(0.5)
        print("    ", end='')
        animate_text(get_matrix_quote(choice), delay=0.03)

if __name__ == "__main__":
    main() 