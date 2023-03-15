# Pac-man-Game
Pac-Man is an action maze chase video game; the player controls the eponymous character through an enclosed maze. The objective of the game is to eat all of the dots placed in the maze while avoiding four colored ghosts . My version is still a work in progress
 
 Detailed Breakdown Of Code:
 
 This code creates a simple Pac-Man game in Python. The code is comprised of two parts:

The PacMan class - This class represents the Pac-Man character in the game. The class has four methods, each representing the movement of Pac-Man in different directions. The class has two instance variables, x and y, which represent the current position of Pac-Man on the game screen.

The main game loop - This is where the game is played. The game is played in a while loop until the game is over. The loop performs the following steps:
a. Print the screen - The game screen is printed as a 5x5 grid of characters. The characters are either dots (.) or the letter "P" which represents Pac-Man. The location of Pac-Man on the screen is determined by the x and y instance variables of the PacMan object.
b. Get player input - The player is prompted to enter a move (left, right, up, down, or quit).
c. Move Pac-Man or end the game - Depending on the player's input, Pac-Man is moved in the appropriate direction or the game is ended by setting the game_over flag to True. If the game is over, the message "Game Over" is printed.
💜
