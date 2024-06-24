# Connect-Four-Game

Welcome to the Connect Four game! This is a Python implementation of the classic Connect Four game with a simple command-line interface and an optional graphical user interface (GUI) using Tkinter.

Table of Contents
- Features
- Installation
- Running the Game
- Playing the Game
- Screenshots
- Contributing
- License

## Features
- Command-line interface for quick play
- Optional GUI using Tkinter for a more interactive experience
- AI opponent using the minimax algorithm
  
## Installation
- ## Prerequisites
  - Python 3.x
  - Pip (Python package installer)

## Steps
  1. Clone the repository by following command: " git clone https://github.com/MuhammadUsman-10/Connect-Four-Game.git "
  2. Then locate to the directory older by the following command: " cd Connect-Four-Game "
  3. If you want to create an executable version, Then run following commands:
     1. pip install pyinstaller
     2. pyinstaller --onefile connect_four.py

## Running The Game
- ## CLI Version
  - To run the command-line version of the game, use the following command: " python connect_four.py "
    
- ## GUI Version
  - To run the GUI version of the game, ensure you have Tkinter installed (it usually comes with Python by default). Then, run: " python connect_four_gui.py "

## Playing the Game
- ## Command-Line Instructions
  1. The game will display an empty 10x10 board.
  2. Players take turns to input the column number (0-9) where they want to drop their token.
  3. The game checks for a win condition after each move. The first player to connect four of their tokens horizontally, vertically, or diagonally wins.
  4. If the board is full and no player has connected four tokens, the game ends in a draw.
    
- ## GUI Instructions
  1. The GUI displays a 10x10 grid of buttons.
  2. Players click on the column where they want to drop their token.
  3. The game automatically updates the board and checks for a win condition.
  4. The first player to connect four of their tokens horizontally, vertically, or diagonally wins.
  5. If the board is full and no player has connected four tokens, the game ends in a draw.
 
## ScreenShots

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
