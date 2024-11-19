# Number Guessing Game

A simple **Number Guessing Game** built with **Python** and **Flask**. The game generates a random number between 1 and 10, and the user tries to guess the number 
by clicking on buttons with different numbers. Each time the user clicks a number, they receive feedback on whether the guessed number is higher, lower or equal to the target number.

## How the Game Works

- The game displays a series of buttons, each representing a number between 1 and 10.
- A random number is selected as the target number.
- Each time the player clicks a button with a number, the game gives feedback
- Once the player guesses the correct number, the game restarts with a new random number.

## Features

- **Random number generation**: The target number is randomly selected between 1 and 10.
- **User-friendly interface**: The user can click on number buttons to make their guess.
- **Instant feedback**: The user receives feedback immediately after each guess.
- **New game on win**: After correctly guessing the number, a new game starts automatically.

## Technologies Used

- **Python**: Programming language for backend logic.
- **Flask**: Web framework used to create the web application.
- **HTML, CSS**: Used to structure and style the user interface.
- **Flask sessions**: Used to store the target number and guessed numbers.

## How to Run the Project Locally

### Prerequisites
Make sure you have **Python** installed. You can download it from [here](https://www.python.org/downloads/)

### Steps to Install and Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/saarrka/Python-projects.git

2. Navigate to the Number Guessing folder:
   ```bash
    cd Python-projects/Number Guessing

3. Create a virtual environment:
   ```bash
     python -m venv venv

4. Activate the virtual environment:
   #### Windows:
   ```bash
     venv\Scripts\activate
   ```
   #### Linux/MacOS:
   ```bash
     source venv/bin/activate
   ```
   
5. Run the Flask app:
   ```bash
   python app.py
   
6. Open your browser and go to:
   ```bash
     http://127.0.0.1:5000/
       
   
  
