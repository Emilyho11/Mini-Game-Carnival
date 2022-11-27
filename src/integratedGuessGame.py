import pygame,sys
from pygame.locals import*

pygame.init()
# Variables
RED = (255, 0, 0)
ORANGE = (255, 155, 0)
YELLOW = (255, 255, 0)
GREEN = (8, 242, 47)
BLUE = (130, 202, 250)
PURPLE = (166, 0, 255)
PINK = (255, 160, 233)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)

# Guessing Choice Page Function
def guessingChoice(gamewindow):
    from reusableFunctions import backToMainMenu
    from animals import animalGuess
    from disney import disneyGuess

    # Set the name of Display
    pygame.display.set_caption("Guessing Game")
    # Set Background - Using a picture
    background = pygame.transform.scale(pygame.image.load(
        "images/questionMarks.jpg"), (1200, 800))
    gamewindow.blit(background, (0, 0))

    # Title
    fontTitle = pygame.font.SysFont('modernno20', 50)
    title = fontTitle.render('Guessing Game', True, BLACK)
    Title = title.get_rect()
    Title.center = (600, 100)
    gamewindow.blit(title, Title)

    fontSubtitle = pygame.font.SysFont('arialrounded', 40)
    choice = fontSubtitle.render('Select the TOPIC:', True, BLACK)
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

        # Button to the animal guessing game
        if 220 + 320 > mouse[0] > 220 and 300 + 220 > mouse[1] > 300:
            animals = pygame.transform.scale(pygame.image.load(
                "images/animal.jpg"), (330, 230))
            gamewindow.blit(animals, (220, 300))
            if click[0] == 1:
                animalGuess(gamewindow)
        else:
            animals = pygame.transform.scale(pygame.image.load(
                "images/animal.jpg"), (320, 220))
            gamewindow.blit(animals, (220, 300))

        # Button to the Disney guessing game
        if 620 + 320 > mouse[0] > 620 and 300 + 220 > mouse[1] > 300:
            disneyPic = pygame.transform.scale(pygame.image.load(
                "images/disney.jpg"), (330, 230))
            gamewindow.blit(disneyPic, (620, 300))
            if click[0] == 1:
                disneyGuess(gamewindow)
        else:
            disneyPic = pygame.transform.scale(pygame.image.load(
                "images/disney.jpg"), (320, 220))
            gamewindow.blit(disneyPic, (620, 300))
        backToMainMenu(gamewindow)
    # End of while loop
# End of guessingChoice()

# Guessing Game Instructions function
def guessInstructions(gamewindow):
    from reusableFunctions import backToMainMenu

    # Set Background - Using a picture
    guessBackground = pygame.transform.scale(pygame.image.load(
        "images/animalBackground.jpg"), (1200, 800))
    gamewindow.blit(guessBackground, (0, 0))
    pygame.display.set_caption("Guessing Game Instructions")
    instructionFont = pygame.font.SysFont('arialrounded', 40)
    instruction = instructionFont.render('Guessing Game Instructions', True, BLACK)
    Instruction = instruction.get_rect()
    Instruction.center = (600, 120)
    gamewindow.blit(instruction, Instruction)

    # Write the instructions
    counter = 0
    text = ['Lets see if you can guess the correct picture!',
            'You can choose your topic: ANIMALS or DISNEY',
            '',
            ' - Try to guess all 10 images!',
            ' - Click on the box (it changes colour), then type your answer!',
            ' - Click ENTER once you typed your answer.',
            '       * NOTE: Make sure you spell your answers correctly! *',
            '         You can have spaces/capital letters in your answers if you want',
            'GOOD LUCK!',
            '',
            '       * Click the START button to play! *']
    for x in text:
        counter += 1
        fonts = pygame.font.SysFont('constantia', 25).render(x, True, BLACK)
        gamewindow.blit(fonts, (280, 150 + (30 * counter)))
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

        # Guessing Choice button
        if 530 + 150 > mouse[0] > 530 and 520 + 50 > mouse[1] > 520:
            pygame.draw.rect(gamewindow, ORANGE, (530, 520, 150, 50))
            if click[0] == 1:
                guessingChoice(gamewindow)
        else:
            pygame.draw.rect(gamewindow, YELLOW, (530, 520, 150, 50))

        startFont = pygame.font.Font('freesansbold.ttf', 20)
        start = startFont.render('START GAME', True, BLACK)
        Start = start.get_rect()
        Start.center = ((530 + (150 / 2)), (520 + (50 / 2)))
        gamewindow.blit(start, Start)
        backToMainMenu(gamewindow)
    # End of while loop
# End of guessInstructions()
