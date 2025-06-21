"""
Time-related utility functions.
"""
from datetime import datetime

def get_current_hour():
    """Get the current hour for time-based greetings."""
    return datetime.now().hour

def get_time_emoji(hour):
    """Get the appropriate emoji for the current time of day."""
    if 5 <= hour < 12:
        return "☀️"
    elif 12 <= hour < 17:
        return "🌞"
    elif 17 <= hour < 22:
        return "🌅"
    else:
        return "🌙"

def get_time_greeting(hour):
    """Get the appropriate greeting for the current time of day."""
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 22:
        return "Evening"
    else:
        return "Night" 