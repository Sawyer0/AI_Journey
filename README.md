# First Project: AI Journey & Matrix Welcome

This project consists of two components:
1. A sophisticated Matrix-themed welcome script in Python
2. A simple webpage documenting the start of an AI journey

## Matrix Welcome Script

An interactive Python script that creates a dramatic, Matrix-themed welcome experience with multiple features and dynamic responses.

### Features

- Interactive name input with validation
- Time-aware greetings with appropriate emojis
- ASCII art box display with centered name
- Special responses for Matrix-themed names
- Red pill/Blue pill choice system
- Dynamic name analysis
- Matrix quotes based on user choices
- Animated typing effects
- Error handling and input validation

### Requirements

- Python 3.x
- No additional packages required (uses only built-in Python modules)

### How to Run the Welcome Script

1. Make sure you have Python installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/Sawyer0/AI_Journey.git
   cd AI_Journey
   ```

3. Create and activate a virtual environment:
   ```bash
   # Create the virtual environment
   python -m venv venv

   # Activate it on Windows (Git Bash)
   source venv/Scripts/activate

   # Activate it on Windows (Command Prompt)
   venv\Scripts\activate

   # Activate it on macOS/Linux
   source venv/bin/activate

   # You'll see (venv) in your terminal when it's active
   ```

4. Run the script:
   ```bash
   python main.py
   ```

5. When you're done, deactivate the virtual environment:
   ```bash
   deactivate
   ```

> **Note**: The virtual environment (venv) keeps the project's Python setup clean and isolated. Each user creates their own venv, which is why the `venv/` folder is not included in the repository.

### Example Output

```
Please enter your first name: Neo

    ===============================
    🌞 Afternoon in the Matrix 🌞
    ===============================

    ╔════════════════╗
    ║                ║
    ║      Neo       ║
    ║                ║
    ╚════════════════╝

    The One has returned... Welcome back, Mr. Anderson.

    Choose your path:
    1. Take the red pill
    2. Take the blue pill
```

## Web Component

A simple HTML webpage that marks the beginning of an AI journey.

### Features
- Clean, minimalist design
- Responsive layout
- Modern styling with custom CSS

### How to View
Visit [https://sawyer0.github.io/AI_Journey](https://sawyer0.github.io/AI_Journey) or open `index.html` in any modern web browser.

## Customization

You can modify either component:

### Welcome Script
- Adjust animation timing in the `animate_text` function
- Add new special names and responses
- Modify the ASCII box design
- Add new Matrix quotes
- Customize time-based greetings

### Webpage
- Update the content to document your AI journey
- Modify the styling in the CSS section
- Add more interactive elements

## Project Structure
```
AI_Journey/
├── display/        # Animation and display functions
├── messages/       # Message and response handling
├── utils/         # Time-related utilities
├── validation/    # Input validation
├── main.py        # Main program
├── index.html     # Project webpage
└── styles.css     # Webpage styling
```

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and enhance either component with your own features! 