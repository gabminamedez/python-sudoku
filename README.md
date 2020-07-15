# Python Sudoku GUI

## Description
This is a Sudoku Desktop application written in Python. This is my first attempt at coding with PyGame, Python's module for creating games. This is a classic 9x9 board that follows the same rules of that of the classic Japanese puzzle.

## Project Directory Guide
1. **main.py** is the main Python file where the GUI is programmed.
2. **solver.py** contains aggregate functions for solving a generic Sudoku puzzle. These functions are imported in main.py as the backbone for logic.
3. **Pipfile** is used for the virtual enviroment to determine the dependencies needed to run the project.
3. **Pipfile.lock** provides the specific details for each dependency installed in the virtual environment.

## Instructions for local machine use:
1. Download this project.
2. If you haven't already, install the pipenv tool with Python using the command line ```pip install pipenv```. This is considering that you have Python already installed in your machine.
3. ```cd``` to the directory of the project.
4. Open the command line and enter the command ```pipenv shell``` to activate the virtual environment.
5. While still in the command line, enter the command ```python main.py``` and the GUI will launch. Enjoy!

## Packages / libraries / modules / frameworks used:
1. **pygame** Python module for the game GUI.
2. **time** Python tool for computing the time elapsed in a specific period in the program.
 
## Project Notes
1. As of now, the project only has a single board combination to work with. You may experiment with it by configuring the board found in main.py.
2. This app involves very simple Sudoku concepts, in addition, the time elapsed to solve the board as well as the number of errors during are recorded and displayed at the bottom of the window.
