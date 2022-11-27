import pygame,sys
from pygame.locals import*

# Import from other files to access the functions and change displays
from integratedGuessGame import guessInstructions
from maze import mazeInstructions
from space import spaceInstructions
from applePicking import appleInstructions
from flappyGame import flappyInstructions

# Variables
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (202,255,122)
DARKGREEN = (121,220,91)

# Main Menu function
def menu(gamewindow):
    font = pygame.font.SysFont('modernno20', 23)

    # Set the name of Display
    pygame.display.set_caption("Main Menu")
    # Set Background - Using a picture
    menuBackground = pygame.transform.scale(pygame.image.load(
        "images/education background.jpg"), (1200, 800))
    gamewindow.blit(menuBackground, (0,0))

    # Title
    fontTitle = pygame.font.SysFont('rockwell', 40)
    title = fontTitle.render('MAIN MENU', True, BLACK)
    Title = title.get_rect()
    Title.center = (600, 70)
    gamewindow.blit(title, Title)
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

        # BACK button to the START Page
        if 10 + 60 > mouse[0] > 10 and 20 + 30 > mouse[1] > 15:
            pygame.draw.rect(gamewindow, WHITE, (10, 20, 60, 30))
            if click[0] == 1:
                from mainGame import startPage
                startPage()
        else:
            pygame.draw.rect(gamewindow, DARKGREEN, (10, 20, 60, 30))

        backFont = pygame.font.SysFont("constantia", 16)
        back = backFont.render('BACK', True, BLACK)
        Back = back.get_rect()
        Back.center = ((10 + (60 / 2)), (20 + (30 / 2)))
        gamewindow.blit(back, Back)

        # Player clicks the maze game button
        if 200 + 150 > mouse[0] > 200 and 150 + 50 > mouse[1] > 150:
            pygame.draw.rect(gamewindow, WHITE, (200, 150, 150, 50))
            if click[0] == 1:
                mazeInstructions(gamewindow)
        else:
            pygame.draw.rect(gamewindow, GREEN, (200, 150, 150, 50))

        mazeWord = font.render('Maze Game', True, BLACK)
        MazeWord = mazeWord.get_rect()
        MazeWord.center = ((200+(150/2)),(150+(50/2)))
        gamewindow.blit(mazeWord, MazeWord)

        # Player clicks the Apple Picking Game button
        if 200 + 150 > mouse[0] > 200 and 250 + 50 > mouse[1] > 250:
            pygame.draw.rect(gamewindow, WHITE, (200, 250, 150, 50))
            if click[0] == 1:
                appleInstructions(gamewindow)
        else:
            pygame.draw.rect(gamewindow, GREEN, (200, 250, 150, 50))

        search = font.render('Apple Picking', True, BLACK)
        Search = search.get_rect()
        Search.center = ((200+(150/2)),(250+(50/2)))
        gamewindow.blit(search, Search)

        # Player clicks the space game button
        if 200 + 150 > mouse[0] > 200 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(gamewindow, WHITE, (200, 350, 150, 50))
            if click[0] == 1:
                spaceInstructions(gamewindow)
        else:
            pygame.draw.rect(gamewindow, GREEN, (200, 350, 150, 50))

        space = font.render('Space Game', True, BLACK)
        Space = space.get_rect()
        Space.center = ((200 + (150 / 2)), (350 + (50 / 2)))
        gamewindow.blit(space, Space)

        # Player clicks the Guessing Game button
        if 400 + 150 > mouse[0] > 400 and 150 + 50 > mouse[1] > 150:
            pygame.draw.rect(gamewindow, WHITE, (400, 150, 150, 50))
            if click[0] == 1:
                guessInstructions(gamewindow)
        else:
            pygame.draw.rect(gamewindow, GREEN, (400, 150, 150, 50))

        guessWord = font.render('Guessing Game', True, BLACK)
        GuessWord = guessWord.get_rect()
        GuessWord.center = ((400 + (150 / 2)), (150 + (50 / 2)))
        gamewindow.blit(guessWord, GuessWord)

        # Player clicks the Flappy Game button
        if 400 + 150 > mouse[0] > 400 and 250 + 50 > mouse[1] > 250:
            pygame.draw.rect(gamewindow, WHITE, (400, 250, 150, 50))
            if click[0] == 1:
                flappyInstructions()
        else:
            pygame.draw.rect(gamewindow, GREEN, (400, 250, 150, 50))

        flappyWord = font.render('Flappy Game', True, BLACK)
        FlappyWord = flappyWord.get_rect()
        FlappyWord.center = ((400 + (150 / 2)), (250 + (50 / 2)))
        gamewindow.blit(flappyWord, FlappyWord)
        pygame.display.update()
    # End of while loop
# End of menu()
