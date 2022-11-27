import os
import sys
import pygame
import random
from pygame.locals import *

# Colours
GREEN = (29, 143, 48)
BLACK = (0, 0, 0)
BLUE = (51, 234, 223)
BROWN = (178, 146, 103)
DARKBLUE = (139, 153, 186)
GREY = (231, 231, 231)
DARKGREY = (172, 172, 172)
WHITE = (255, 255, 255)
PINK = (255, 191, 221)
YELLOW = (255, 255, 0)

# Player Class
class Player(pygame.sprite.Sprite):

    # Initialization Method
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([18, 18])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 18
        self.rect.y = 18

    # Method that moves the player
    def move(self, length, width):
        if length != 0:
            self.moving(length, 0)
        if width != 0:
            self.moving(0, width)
    # End of move()

    # Method that checks for collisions as the player is moving
    def moving(self, length, width):
        self.rect.x += length
        self.rect.y += width

        # Check if player collided with the wall
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                # Collide with left side of the wall
                if length > 0:
                    self.rect.right = wall.rect.left
                # Collide with right side of the wall
                if length < 0:
                    self.rect.left = wall.rect.right
                # Collide with top side of the wall
                if width > 0:
                    self.rect.bottom = wall.rect.top
                # Collide with bottom side of the wall
                if width < 0:
                    self.rect.top = wall.rect.bottom
        # End of for loop
    # End of moving()
# End of Player() class

# Coins Class
class Coin(pygame.sprite.Sprite):

    # Initialization Method
    def __init__(self, color, width, height):
        super().__init__()
        # Create an image of the coin
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        # Update the position of the player
        self.rect = self.image.get_rect()
# End of Coins() class

# Wall Class
class Wall(object):
    # Initialization Method
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 15, 15)
# End of Wall() class

# Initialize Game
os.environ["Maze Game"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Maze Game")
gamewindow = pygame.display.set_mode((1200, 800))

# List to hold the walls
walls = []
# Create the player
player = Player()
blockList = pygame.sprite.Group()
allObjectsList = pygame.sprite.Group()
allObjectsList.add(player)

# Add 50 of the same coins
for i in range(50):
    block = Coin(YELLOW, 20, 15)

    # Set a random location for the coin
    block.rect.x = random.randrange(1100)
    block.rect.y = random.randrange(700)
    # Add the coin to the list of objects
    blockList.add(block)
    allObjectsList.add(block)
# End of for loop

# Maze Layout
# Holds the level in a list of strings
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W        W                                       W     W                             W",
    "W        W                                       W     W                             W",
    "WWWWWWW  W  WWWWWWWWW  W  WWWWWWWWWWWWWWWWWWWWW  W  W  W  WWWWWWWWWWWWWWWWWWWWWW  W  W",
    "W     W  W  W          W  W     W  W          W  W  W  W  W     W              W  W  W",
    "W     W  WWWW          W  W     W  W          W  WWWW  WWWW     W              W  W  W",
    "W  W            W  W   W  W  W  W  W          W  W     W     W  W  W  WWWWWWW  W  W  W",
    "W  W            W  W   W  W  W  W  W          W  W     W     W     W        W     W  W",
    "W  WWWWWWWWWWWWWW  WWWWW  W  WWWW  WWWWWWWWW  W  W  WWWW  WWWW     W        W     W  W",
    "W           W             W  W                W  W  W           WWWWWWWW    WWWWWWW  W",
    "W           W             W  W                W  W  W           W      W          W  W",
    "W  W  WWWW  W  W  WWWWWWWWW  W  WWWWWWWWWWWWWWW  W  WWWWWWWWWW  W      W          W  W",
    "W  W  W  W  W  W             W             W     W              W   W  WWWWWWWWW  W  W",
    "W  W  W  W  W  W             W             W     W              W   W             W  W",
    "W  W     W  W  WWWWWWWWWWWW  WWWWWWWWWWWW  W  WWWW  WWWWWWWWWWWWW   W             W  W",
    "W  W     W  W  W                        W  W  W  W  W        W  W   WWWWWWWWWWWWWWW  W",
    "W  WWWWWWWWWW  W                        W  W  W  W  W        W  W   W                W",
    "W           W  WWWW  WWWWWWWWWWWWWWWWW  W  W  W  W  W  W  W  W      W                W",
    "W           W     W  W                  W  W  W  W  W  W  W  W      W    WWWWWWWWWWWWW",
    "WWWWWWWWWW  W     W  W                  W  W     W     W  W  WWWWWWWW    W     W     W",
    "W           WWWW  W  W  W  WWWWWWWWWWWWWW  W     W     W  W         W    W     W     W",
    "W           W  W  W  W  W  W            W  WWWWWWWWWWWWW  W         W    W  W  W  W  W",
    "W  WWWWWWWWWW  W  W     W               W            W    WWWWWWWWWWWWW  W  W  W  W  W",
    "W  W           W  W     W         W  W  W            W    W           W     W  W  W  W",
    "W  W           WWWWWWWWWWWWWWWWWWWW  W  WWWWWWWW  W  W  WWW           W     W     W  W",
    "W  WWWW  WWWWWWW                     W            W  W       WWWWWWW  W  WWWW     W  W",
    "W        W                           W            W  W       W     W  W  W  WWWWWWW  W",
    "W        W          WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  W  WWWWWW     W  W  W           W",
    "WWWWWWWWWW   WWWW                                 W  W       W  W  W  W  W           W",
    "W            W  W                                 W  W       W  W  W  W  WWWWWWWWWWWWW",
    "W            W  WWWWWWWWWWWWWWW  WWWWWWWWWWWWWWW  W  W  WWW  W  W     W              W",
    "W  WWWWWWWWWWW  W             W                W  W  W    W  W  W     W              W",
    "W  W            W             W                W  W  W    W  W  WWWWWWWWWWWWWWWWWWW  W",
    "W  W            W  WWWWWWWWW  W  WWWWWWWWWWWW  WWWWWWW    W  W                    W  W",
    "W  W  WWWWWWWWWWW  W       W  W  W                   W    W  W                    W  W",
    "W                  W       W  W  W                   W  WWW  W  WWWWWWWWWWWWWWWWWWW  W",
    "W                  W  W    W  W  W  WWWWWWWWWWWWWWW  W  W    W  W     W              W",
    "W  WWWWWWWWWWWWWWWWW  W    W  W  W                W  W  W    W  W     W              W",
    "W  W     W         W  WWWWWW  W  W                W  W  W  WWW  W  W  W  W  WWWWWWWWWW",
    "W  W     W         W          W  WWWWWWWWWWWWWWW  W  W  W       W  W  W  W           W",
    "W  W  W  W         W          W    W           W  W  W  W       W  W  W  W           W",
    "W     W  WWWWWWWWWWWWWWWWWWW  W    W           W  W  W  WWWWWWWWW  W  W  WWWWWWWWWW  W",
    "W     W  W              W  W  W    W  WWWWWWW  W  W  W  W          W     W        W  W",
    "WWWWWWW  W              W  W  W    W  W     W  W  W  W  W          W     W        W  W",
    "W     W  WWWWWWWWWWWWW  W  W  W    W  W     W  W  W  W  W  WWWWWWWWWWWWWWWWWWWWW  W  W",
    "W                       W  W  W    W  W  W  W  W  W  W  W  W             W     W  W  W",
    "W  W                    W  W  W    W  W  W  W  W  W  W  W  W             W     W  W  W",
    "W  WWWWWWWWWWWWWWWWWWWWWW  W  WW   WWWW  W  W  W  W  W  W  WWWWWWWW  W   W  W  W  W  W",
    "W          W               W             W  W     W  W  W         W  W   W  W  W  W  W",
    "W          W               W             W  W     W  W  W         W  W   W  W  W  W  W",
    "WWWWWWWWW  W  WWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWW  W  WWWWWWWW  W  W   W  W  W  W  W",
    "W          W                     W       W  W  W     W         W  W  W   W  W  W     W",
    "W          W                     W       W  W  W     W         W  W  W   W  W  W     W",
    "W  WWWWWWWWWWWWWWWWWWWWWWWWWWWW  W   W   W  W  W  WWWWWWWWWWW  W  W  W   W  W  WWWWWWW",
    "W                                W   W         W               W     W      W        W",
    "W                                W   W         W               W     W      W        E",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# W = wall, E = exit
# Initializes the letters in the maze layout
x = 0
y = 0
exitSquare = ""
for row in level:
    for letter in row:
        if letter == "W":
            Wall((x, y))
        if letter == "E":
            exitSquare = pygame.Rect(x, y, 15, 15)
        x += 14
    y += 14
    x = 0
# End of for loop

# Maze Game Function
def mazeGame():
    from reusableFunctions import backToMainMenu
    score = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        # End of for loop

        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            # Speed of the player
            player.move(-10, 0)
        if key[pygame.K_RIGHT]:
            player.move(10, 0)
        if key[pygame.K_UP]:
            player.move(0, -10)
        if key[pygame.K_DOWN]:
            player.move(0, 10)

        allObjectsList.update()
        gamewindow.fill(GREEN)
        pygame.time.delay(40)

        # Output the Score after player collects coins
        font = pygame.font.SysFont('modernno20', 30)
        scorefont = font.render("Score: " + str(score), True, BLACK)
        Scorefont = scorefont.get_rect()
        Scorefont.center = (570, 85)
        gamewindow.blit(scorefont, Scorefont)

        # See if the player collided with any coins
        blocksCollision = pygame.sprite.spritecollide(player, blockList, True)

        # Count the score if player collected any coins.
        for block in blocksCollision:
            score += 1
        # End of for loop

        # Draw the maze in the gamewindow
        for wall in walls:
            pygame.draw.rect(gamewindow, DARKGREY, wall.rect)
            pygame.draw.rect(gamewindow, (255, 0, 0), exitSquare)
            pygame.draw.rect(gamewindow, BLUE, player.rect)
        # End of for loop

        # Draw the coins
        allObjectsList.draw(gamewindow)

        # Start Word
        startFont = pygame.font.Font('freesansbold.ttf', 20)
        start = startFont.render('Start -->', True, BLACK)
        Start = start.get_rect()
        Start.center = (70, 30)
        gamewindow.blit(start, Start)

        # Finish Word
        endFont = pygame.font.Font('freesansbold.ttf', 20)
        end = endFont.render('Finish', True, BLACK)
        End = end.get_rect()
        End.center = (1155, 770)
        gamewindow.blit(end, End)

        backToMainMenu(gamewindow)
        pygame.display.update()
    # End of while loop
# End of mazeGame()

# Maze Instructions Function
def mazeInstructions(gamewindow):
    from reusableFunctions import backToMainMenu

    LIGHTGREEN = (199, 255, 38)
    GREEN = (8, 242, 47)

    # Set Background - Using a picture
    mazeBackground = pygame.transform.scale(pygame.image.load("mazeBackground.jpg"), (1200, 800))
    gamewindow.blit(mazeBackground, (0, 0))

    pygame.display.set_caption("Maze Game Instructions")
    instructionFont = pygame.font.SysFont('arialrounded', 40)
    # Set the title
    instruction = instructionFont.render('Maze Game Instructions', True, BLACK)
    Instruction = instruction.get_rect()
    Instruction.center = (600, 80)
    gamewindow.blit(instruction, Instruction)

    # Write the instructions
    counter = 0
    text = ['Welcome to the Maze Game!',
            '',
            ' - Try to collect as many coins as you can while finding your way to the end!',
            '',
            ' * Click the START button to play! *']
    for x in text:
        counter += 1
        fonts = pygame.font.SysFont('constantia', 25).render(x, True, BLACK)
        gamewindow.blit(fonts, (280, 150 + (30 * counter)))
    # End of for loop
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            # Allow player to exit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # End of for loop
        # Allow player to use the mouse
        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Maze Game button
        if 280 + 150 > mouse[0] > 280 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(gamewindow, LIGHTGREEN, (280, 350, 150, 50))
            if click[0] == 1:
                mazeGame()
        else:
            pygame.draw.rect(gamewindow, GREEN, (280, 350, 150, 50))

        mazeFont = pygame.font.Font('freesansbold.ttf', 20)
        mazeWord = mazeFont.render('START GAME', True, BLACK)
        MazeWord = mazeWord.get_rect()
        MazeWord.center = ((280 + (150 / 2)), (350 + (50 / 2)))
        gamewindow.blit(mazeWord, MazeWord)

        # Main Menu button
        backToMainMenu(gamewindow)
        pygame.display.update()
    # End of while loop
# End of mazeInstructions()
