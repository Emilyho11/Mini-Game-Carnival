import pygame, sys
import random
from pygame.locals import*

pygame.init()
# Variables
BROWN = (178,146,103)
GREEN = (87,184,37)
BLUE = (165,222,233)
DARKBLUE = (139,153,186)
BLACK = (0, 0, 0)
GREY = (231,231,231)
DARKGREY = (172,172,172)
WHITE = (255, 255, 255)
PINK = (255,191,221)
clock = pygame.time.Clock()

font = pygame.font.SysFont('timesnewroman', 20)
pipes = []
score = 0
highScore = 0
gameStage = 1
gamewindow = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Easy Flappy Game")

# Player Class
class Player():
    # Initialization Method
    def __init__(self):
        self.x = 250
        self.y = 250
        self.moveY = 0

    # Method that makes the player jump
    def fly(self):
        self.moveY = -10
    # End of fly()

    # Method that updates the player's location
    def update(self):
        self.moveY += 0.6
        self.y += self.moveY
        if self.y >= 700:
            self.y = 700
            self.moveY = 0
        if self.moveY > 20:
            self.moveY = 20
    # End of update()

    # Method that creates a player(image)
    def draw(self, chosenImage):
        player = pygame.transform.scale(chosenImage, (50, 50))
        gamewindow.blit(player, (self.x, self.y))
    # End of draw()

    # Method that resets the location of the player
    def reset(self):
        self.x = 250
        self.y = 250
        self.moveY = 0
    # End of reset()
# End of Player() class

# Declare the player
player = Player()

# Pipe class
class Pipe():
    # Initialization method
    def __init__(self):
        # Choose where the space between the pipes is located
        self.randCenter = random.randrange(130, 580)
        # Location where the pipe appears
        self.x = 1000
        # Space between the pipes
        self.size = 90

    # Method that updates the pipes
    def update(self):
        global player
        global pipes
        global gameStage
        global score
        # Speed of pipes when they move on screen. Makes the pipes move left
        self.x -= 5
        # Length Between each Pipe
        if self.x == 500:
            pipes.append(Pipe())
        # Delete the pipe if it reaches past the left side of the display screen
        if self.x <= -100:
            del pipes[0]
        # Check for collisions (With player and pipe)
        if self.x >= 170 and self.x <= 290 and player.y <= (
                self.randCenter - self.size) or self.x >= 170 and self.x <= 290 and (player.y + 40) >= (
                self.randCenter + self.size):
            gameStage = 3
        # If player made it past the pipe, add a score
        if self.x == 160 and player.y > (self.randCenter - 100) and player.y < (self.randCenter + 100):
            score += 1
        # If player lands on the ground, game is over
        if player.y >= 700:
            gameStage = 3
    # End of update()

    # Method that draws the Pipes
    def draw(self):
        # Draw the top pipes
        pygame.draw.rect(gamewindow, DARKGREY, (self.x, 0, 80, (self.randCenter - self.size)))
        # Draw the bottom pipes
        pygame.draw.rect(gamewindow, DARKGREY, (self.x, (self.randCenter + self.size), 80, (800 - self.randCenter)))
    # End of draw()
# End of Pipe() class
pipes.append(Pipe())

# Flappy Game function
def flappyGame():
    from reusableFunctions import backToMainMenu
    from random import randrange
    from images import flappyImages
    global gameStage
    global pipes
    global score
    global highScore

    # Randomize the image of player
    randomPics = randrange(len(flappyImages()))
    randImages = flappyImages()[randomPics]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check if player uses the keyboard
            if event.type == pygame.KEYDOWN:
                # Allow player to use the space bar
                if event.key == pygame.K_SPACE:
                    # If player hits the space bar, start game
                    if gameStage == 1:
                        gameStage = 2
                    # if player loses, reset game
                    elif gameStage == 3:
                        player.reset()
                        pipes = [Pipe()]
                        gameStage = 2
                        score = 0
                        flappyGame()
                    else:
                        player.fly()
        # End of for loop
        # Add background image
        easyBackground = pygame.transform.scale(pygame.image.load(
            "flappyBackground.png"), (1200, 800))
        gamewindow.blit(easyBackground, (0, 0))
        pygame.draw.rect(gamewindow, DARKGREY, (0, 735, 1200, 75))
        back()

        # Start of the game
        if gameStage == 1:
            pygame.draw.rect(gamewindow, GREY, (500, 150, 200, 80))
            pygame.draw.rect(gamewindow, DARKBLUE, (500, 150, 200, 80), 5)
            startingText = font.render("Press SPACE to play!", True, BLACK)
            gamewindow.blit(startingText, (510,180))

        # When Player is playing game
        if gameStage == 2:
            player.update()
            player.draw(randImages)

            # Draw the pipes
            for pipe in pipes:
                pipe.update()
                pipe.draw()
            # End of for loop

            # Display the score
            scoreFont = pygame.font.SysFont('timesnewroman', 30)
            scoreText = scoreFont.render("Score: " + str(score), True, BLACK)
            gamewindow.blit(scoreText, (550,40))

            # Get high score
            if score > highScore:
                highScore = score

        # When the player hits a pipe/when game is over
        if gameStage == 3:
            for pipe in pipes:
                pipe.draw()
            player.draw(randImages)

            # Draw the game over square
            pygame.draw.rect(gamewindow, GREY, (500, 150, 200, 200))
            pygame.draw.rect(gamewindow, BROWN, (500, 150, 200, 200), 5)
            # Display the score
            finalScore = font.render(("Score: " + str(score)), True, BLACK)
            FinalScore = finalScore.get_rect()
            FinalScore.center = ((600, 200))
            gamewindow.blit(finalScore, FinalScore)
            # Display the high score
            highScoreText = font.render(("High Score: " + str(highScore)), True, BLACK)
            HighScoreText = highScoreText.get_rect()
            HighScoreText.center = ((600, 250))
            gamewindow.blit(highScoreText, HighScoreText)

            againText = font.render("Press space to play", True, BLACK)
            AgainText = againText.get_rect()
            AgainText.center = ((600, 300))
            gamewindow.blit(againText, AgainText)

        # Call function that creates Main Menu button
        backToMainMenu(gamewindow)
        pygame.display.update()
        clock.tick(60)
    # End of while loop
# End of flappyGame()

# Flappy Game Instructions function
def flappyInstructions():
    from reusableFunctions import backToMainMenu

    # Set Background - Using a picture
    spaceBackground = pygame.transform.scale(pygame.image.load(
        "flappyBackground.png"), (1200, 800))
    gamewindow.blit(spaceBackground, (0, 0))
    pygame.display.set_caption("Flappy Game Instructions")
    instructionFont = pygame.font.SysFont('arialrounded', 40)
    instruction = instructionFont.render('Flappy Game Instructions', True, BLACK)
    Instruction = instruction.get_rect()
    Instruction.center = (600, 80)
    gamewindow.blit(instruction, Instruction)

    # Write the instructions
    counter = 0
    text = ['Lets see if you can beat your HIGH SCORE!',
            ' - PRESS the SpaceBar to move your character!',
            ' - Do not touch the ground or hit any of the pipes!',
            '',
            ' - The EASY version counts your score.',
            ' - The HARD version records your time.',
            '',
            '* Click the START button to play! *']
    for x in text:
        counter += 1
        fonts = pygame.font.SysFont('constantia', 25).render(x, True, BLACK)
        gamewindow.blit(fonts, (350, 100 + (30 * counter)))
    # End of for loop
    pygame.display.update()

    # Create this loop so that user can click on the 'x' button to exit
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # End of for loop

        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Start Game Button
        if 390 + 150 > mouse[0] > 390 and 390 + 50 > mouse[1] > 390:
            pygame.draw.rect(gamewindow, WHITE, (390, 390, 150, 50))
            if click[0] == 1:
                easyHardChoice(gamewindow)
        else:
            pygame.draw.rect(gamewindow, BLUE, (390, 390, 150, 50))

        startFont = pygame.font.Font('freesansbold.ttf', 20)
        start = startFont.render('START GAME', True, BLACK)
        Start = start.get_rect()
        Start.center = ((390 + (150 / 2)), (390 + (50 / 2)))
        gamewindow.blit(start, Start)
        backToMainMenu(gamewindow)
    # End of while loop
# End of flappyInstructions()

# BACK button function
def back():
    pygame.event.get(pygame.MOUSEBUTTONDOWN)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # BACK button
    if 0 + 70 > mouse[0] > 0 and 0 + 30 > mouse[1] > 0:
        pygame.draw.rect(gamewindow, WHITE, (0, 0, 70, 30))
        if click[0] == 1:
            flappyInstructions()
    else:
        pygame.draw.rect(gamewindow, GREY, (0, 0, 70, 30))

    backFont = pygame.font.Font('freesansbold.ttf', 14)
    back = backFont.render('BACK', True, BLACK)
    Back = back.get_rect()
    Back.center = ((0 + (70 / 2)), (0 + (30 / 2)))
    gamewindow.blit(back, Back)
# End of back()

# Player can choose to play the easy or hard game page - function
def easyHardChoice(gamewindow):
    from reusableFunctions import backToMainMenu
    from hardFlappyGame import hardFlappyGame

    # Set Background - Using a picture
    spaceBackground = pygame.transform.scale(pygame.image.load(
        "outsideBackground.jpg"), (1200, 800))
    gamewindow.blit(spaceBackground, (0, 0))
    # Set the name of Display
    pygame.display.set_caption("Flappy Game")

    # Title
    fontTitle = pygame.font.SysFont('modernno20', 50)
    title = fontTitle.render('Flappy Game', True, BLACK)
    Title = title.get_rect()
    Title.center = (600, 100)
    gamewindow.blit(title, Title)

    fontSubtitle = pygame.font.SysFont('arialrounded', 40)
    choice = fontSubtitle.render('Select the Level of Difficulty:', True, BLACK)
    Choice = choice.get_rect()
    Choice.center = (600, 200)
    gamewindow.blit(choice, Choice)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # End of for loop
        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Button to the Easy Flappy Game
        if 400 + 100 > mouse[0] > 400 and 300 + 80 > mouse[1] > 300:
            pygame.draw.rect(gamewindow, BLUE, (400, 300, 100, 80))
            if click[0] == 1:
                flappyGame()
        else:
            pygame.draw.rect(gamewindow, PINK, (400, 300, 100, 80))

        difficultyFont = pygame.font.SysFont('modernno20', 30)
        easy = difficultyFont.render('EASY', True, BLACK)
        Easy = easy.get_rect()
        Easy.center = ((400 + (100 / 2)), (300 + (80 / 2)))
        gamewindow.blit(easy, Easy)

        # Button to the Hard Flappy Game
        if 700 + 100 > mouse[0] > 700 and 300 + 80 > mouse[1] > 300:
            pygame.draw.rect(gamewindow, BLUE, (700, 300, 100, 80))
            if click[0] == 1:
                hardFlappyGame()
        else:
            pygame.draw.rect(gamewindow, PINK, (700, 300, 100, 80))

        hard = difficultyFont.render('HARD', True, BLACK)
        Hard = hard.get_rect()
        Hard.center = ((700 + (100 / 2)), (300 + (80 / 2)))
        gamewindow.blit(hard, Hard)
        backToMainMenu(gamewindow)
    # End of while loop
# End of easyHardChoice()
