import pygame,sys
from pygame.locals import*
# Variables
BLUE = (130, 202, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTPURPLE = (240,206,253)
PINK = (255,147,214)
GREY = (222,225,223)
DARKBLUE = (24,32,83)

def searchGame(gamewindow):

    # Set the name of Display
    pygame.display.set_caption("Search and Find Game")
    # Set Background - Using a picture
    gamewindow.fill(DARKBLUE)
    menuBackground = pygame.transform.scale(pygame.image.load(
        "hidden background.png"), (1200, 650))
    gamewindow.blit(menuBackground, (0, 0))

    # Title
    fontTitle = pygame.font.Font('freesansbold.ttf', 25)
    title = fontTitle.render('Search & Find Game', True, WHITE)
    Title = title.get_rect()
    Title.center = (660, 40)
    gamewindow.blit(title, Title)
    pygame.display.update()

    # Create this loop so that user can click on the 'x' button to exit
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def searchFindInstructions(gamewindow):
    pygame.display.set_caption("Search & Find Game Instructions")
    gamewindow.fill(GREY)
    instructionFont = pygame.font.Font('freesansbold.ttf', 40)
    instruction = instructionFont.render('Search & Find Game Instructions', True, BLACK)
    Instruction = instruction.get_rect()
    Instruction.center = (600, 80)
    gamewindow.blit(instruction, Instruction)
    pygame.display.update()

    # Create this loop so that user can click on the 'x' button to exit
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 800 + 150 > mouse[0] > 800 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(gamewindow, LIGHTPURPLE, (800, 600, 150, 50))
            if click[0] == 1:
                searchGame(gamewindow)
        else:
            pygame.draw.rect(gamewindow, PINK, (800, 600, 150, 50))

        mazeFont = pygame.font.Font('freesansbold.ttf', 20)
        mazeWord = mazeFont.render('START GAME', True, BLACK)
        MazeWord = mazeWord.get_rect()
        MazeWord.center = ((800 + (150 / 2)), (600 + (50 / 2)))
        gamewindow.blit(mazeWord, MazeWord)

        pygame.display.update()