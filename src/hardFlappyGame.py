import pygame, sys
import random

pygame.init()
# Variables
BROWN = (178,146,103)
GREEN = (87,184,37)
YELLOW = (255, 255, 0)
BLUE = (165,222,233)
DARKBLUE = (139,153,186)
BLACK = (0, 0, 0)
GREY = (231,231,231)
DARKGREY = (172,172,172)
DARKERGREY = (143,146,143)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

font = pygame.font.SysFont('timesnewroman', 20)
pipes = []
scoreList = []
highScore = 0
gameStage = 1
gamewindow = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Hard Flappy Game")

# Player class
class Player():
    # Initialization method
    def __init__(self):
        self.x = 250
        self.y = 250
        self.moveY = 0

    # Method that makes the player jumps
    def fly(self):
        self.moveY = -10
    # End of fly()

    # Method that updates the location of the player
    def update(self):
        self.moveY += 0.7
        self.y += self.moveY
        if self.y >= 700:
            self.y = 700
            self.moveY = 0
        if self.moveY > 20:
            self.moveY = 20
    # End of update()

    # Method that creates the player(image)
    def draw(self, chosenImage):
        player = pygame.transform.scale(chosenImage, (50, 50))
        gamewindow.blit(player, (self.x, self.y))
    # End of draw()

    # Resets location of player
    def reset(self):
        self.x = 250
        self.y = 250
        self.moveY = 0
    # End of reset()

# Declare player
player = Player()

# Pipe class
class Pipe():
    # Initialization method
    def __init__(self):
        # Choose where the space between the pipes is located
        self.randCenter = random.randrange(200, 450)
        # Location where the pipe appears
        self.x = 1200
        # Space between the pipes
        self.size = 173

    # Method that updates pipe location
    def update(self):
        global player
        global pipes
        global gameStage
        global score
        # Speed of the moving screen
        self.x -= 5
        # Length Between each Pipe
        if self.x == 1100:
            pipes.append(Pipe())
        # Delete the pipe if it reaches past the left side of the display screen
        if self.x <= -200:
            del pipes[0]
        # Check for collisions (With player and pipe)
        if self.x >= 170 and self.x <= 290 and player.y <= (
                self.randCenter - self.size) or self.x >= 170 and self.x <= 290 and (player.y + 40) >= (
                self.randCenter + self.size):
            gameStage = 3
        # If player lands on the ground, game is over
        if player.y >= 610:
            gameStage = 3
    # End of update()

    # Draw the Pipes
    def draw(self):
        # Top Pipes
        pygame.draw.rect(gamewindow, DARKERGREY, (self.x, 0, 80, (self.randCenter - self.size)))
        # Bottom Pipes
        pygame.draw.rect(gamewindow, DARKERGREY, (self.x, (self.randCenter + self.size), 80, (495 - self.randCenter)))
    # End of draw()
pipes.append(Pipe())

# Harder Flappy Game function
def hardFlappyGame():
    from random import randrange
    from images import flappyImages
    global gameStage
    global pipes
    global highScore

    minutes = 0
    seconds = 0
    milliseconds = 0
    newSeconds = 0
    scoreTime = 0

    # Randomize the image of player
    randomPics = randrange(len(flappyImages()))
    randImages = flappyImages()[randomPics]

    timeOver = False
    while not timeOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check if player uses the keyboard
            if event.type == pygame.KEYDOWN:
                # Allow player to use the space bar
                if event.key == pygame.K_SPACE:
                    if gameStage == 1:
                        gameStage = 2
                    # If game is over, reset everything
                    elif gameStage == 3:
                        player.reset()
                        pipes = [Pipe()]
                        gameStage = 2
                        timeOver = True
                        hardFlappyGame()
                    else:
                        player.fly()
        # End of for loop

        # Add background image
        hardBackground = pygame.transform.scale(pygame.image.load(
            "runningBackground.png"), (1200, 800))
        gamewindow.blit(hardBackground, (0, 0))
        pygame.draw.rect(gamewindow, GREEN, (0, 660, 1200, 300))

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

            # Draw pipes onto the display
            for pipe in pipes:
                pipe.update()
                pipe.draw()

            # Add timer when player starts game
            if milliseconds > 1000:
                seconds += 1
                newSeconds += 1
                milliseconds -= 1000

            # Add seconds up to 60. Then add the minutes
            if seconds > 60:
                minutes += 1
                seconds -= 60

            # Repeat the time (60 seconds)
            milliseconds += clock.tick_busy_loop(60)
            timeFont = pygame.font.SysFont('timesnewroman', 30)
            timeOutput = timeFont.render("Time: {}:{}".format(minutes, seconds), True, BLACK)
            gamewindow.blit(timeOutput, (550, 50))

            # Find high score from timer
            if newSeconds > highScore:
                highScore = newSeconds
                scoreList.append(highScore)
                scoreTime = ((highScore - (60 * minutes)) / 100) + minutes

            else:
                if len(scoreList) > 0:
                    highScore = max(scoreList)
                    scoreTime = ((highScore - (60 * minutes)) / 100) + minutes

        # When the player hits a pipe
        if gameStage == 3:
            for pipe in pipes:
                pipe.draw()
            player.draw(randImages)

            # Create the output once game is over
            pygame.draw.rect(gamewindow, GREY, (500, 150, 200, 200))
            pygame.draw.rect(gamewindow, BROWN, (500, 150, 200, 200), 5)
            # Output player's time
            finalScore = font.render(("Time: " + str(minutes) + ":" + str(seconds)), True, BLACK)
            FinalScore = finalScore.get_rect()
            FinalScore.center = ((600, 200))
            gamewindow.blit(finalScore, FinalScore)
            # Output high score
            highScoreText = font.render(("High Score: " + str(scoreTime)), True, BLACK)
            HighScoreText = highScoreText.get_rect()
            HighScoreText.center = ((600, 250))
            gamewindow.blit(highScoreText, HighScoreText)

            againText = font.render("Press SPACE to play", True, BLACK)
            AgainText = againText.get_rect()
            AgainText.center = ((600, 300))
            gamewindow.blit(againText, AgainText)

        backButton()
        clock.tick(420)
    # End of while loop
# End of hardFlappyGame()

# BACK and MENU button function
def backButton():
    from flappyGame import flappyInstructions
    from mainMenu import menu
    global highScore
    pygame.event.get(pygame.MOUSEBUTTONDOWN)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Main Menu Button
    if 1130 + 70 > mouse[0] > 1130 and 0 + 30 > mouse[1] > 0:
        pygame.draw.rect(gamewindow, WHITE, (1130, 0, 70, 30))
        if click[0] == 1:
            scoreList.clear()
            highScore = 0
            menu(gamewindow)
    else:
        pygame.draw.rect(gamewindow, YELLOW, (1130, 0, 70, 30))

    menuFont = pygame.font.Font('freesansbold.ttf', 12)
    menuButton = menuFont.render('Main Menu', True, BLACK)
    MenuButton = menuButton.get_rect()
    MenuButton.center = ((1130 + (70 / 2)), (0 + (30 / 2)))
    gamewindow.blit(menuButton, MenuButton)

    # BACK button
    if 0 + 70 > mouse[0] > 0 and 0 + 30 > mouse[1] > 0:
        pygame.draw.rect(gamewindow, WHITE, (0, 0, 70, 30))
        if click[0] == 1:
            scoreList.clear()
            highScore = 0
            flappyInstructions()
    else:
        pygame.draw.rect(gamewindow, GREY, (0, 0, 70, 30))

    backFont = pygame.font.Font('freesansbold.ttf', 14)
    back = backFont.render('BACK', True, BLACK)
    Back = back.get_rect()
    Back.center = ((0 + (70 / 2)), (0 + (30 / 2)))
    gamewindow.blit(back, Back)
    pygame.display.update()
# End of backButton()
