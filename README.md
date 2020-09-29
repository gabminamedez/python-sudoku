# python-sudoku-gui
This is a Sudoku Desktop application written in Python. This is my first attempt at coding with PyGame, Python's module for creating games. This is a classic 9x9 board that follows the same rules of that of the classic Japanese puzzle.

## Project Directory Guide
1. `main.py` is the main Python file where the GUI is programmed.
2. `solver.py` contains aggregate functions for solving a generic Sudoku puzzle. These functions are imported in main.py as the backbone for logic.
3. **venv** is the folder of the virtual environment.

## Instructions for local machine use:
1. Clone this repository.
2. Open the command line interface and `cd` to the directory of this repository.
3. Enter the command `pip install -r requirements.txt` to install the required modules.
4. While still in the command line, enter the command `python main.py` and the GUI will launch. Enjoy!

## Packages / libraries / modules / frameworks used:
1. **pygame** Python module for the game GUI.
2. **time** Python tool for computing the time elapsed in a specific period in the program.
 
## Project Notes
1. As of now, the project only has a single board combination to work with. You may experiment with it by configuring the board found in `main.py`.
2. This app involves very simple Sudoku concepts, in addition, the time elapsed to solve the board as well as the number of errors during are recorded and displayed at the bottom of the window.
