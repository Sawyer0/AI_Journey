def get_welcome_message(name):
    return f"Welcome, {name}! We're glad to have you here."

def main():
    # Get the user's name
    name = input("Please enter your name: ")
    
    # Generate and print the welcome message
    welcome_message = get_welcome_message(name)
    print(welcome_message)

if __name__ == "__main__":
    main()