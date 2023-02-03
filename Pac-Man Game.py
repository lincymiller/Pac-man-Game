"""
Pacman implementation by Lincy Miller
Website: https://www.lincymiller.tech
Github: https://www.github.com/lincymiller
LinkedIn: https://www.linkedin.com/in/lincy-m-99b228128/
"""




class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1


# Initialize Pac-Man
pacman = PacMan(0, 0)

# Main game loop
game_over = False
while not game_over:
    # Print the screen
    for y in range(5):
        for x in range(5):
            if x == pacman.x and y == pacman.y:
                print("P", end=" ")
            else:
                print(".", end=" ")
        print()

    # Get player input
    move = input("Enter move (left, right, up, down, quit): ")

    # Move Pac-Man or end the game
    if move == "left":
        pacman.move_left()
    elif move == "right":
        pacman.move_right()
    elif move == "up":
        pacman.move_up()
    elif move == "down":
        pacman.move_down()
    elif move == "quit":
        game_over = True
        print("Game Over")
