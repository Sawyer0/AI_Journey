"""
Animation and text display functions.
"""
import time
from utils.time_utils import get_current_hour, get_time_emoji, get_time_greeting

def animate_text(text, delay=0.05):
    """Animate text by printing it character by character."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def create_name_banner(name):
    """Create an ASCII art banner with the user's name."""
    width = len(name) + 10  # Add padding
    
    top = "╔" + "═" * width + "╗"
    bottom = "╚" + "═" * width + "╝"
    middle = "║" + " " * width + "║"
    
    padding = (width - len(name)) // 2
    name_line = "║" + " " * padding + name + " " * (width - padding - len(name)) + "║"
    
    banner = f"""
    {top}
    {middle}
    {name_line}
    {middle}
    {bottom}
    """
    return banner

def create_decorative_element():
    """Create a time-based decorative element."""
    hour = get_current_hour()
    emoji = get_time_emoji(hour)
    greeting = get_time_greeting(hour)
    
    line = "=" * (len(greeting) + 20)
    return f"""
    {line}
    {emoji} {greeting} in the Matrix {emoji}
    {line}
    """ 