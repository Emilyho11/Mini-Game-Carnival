import pygame,sys
pygame.init()
from mainMenu import menu

# Variables
BLUE = (130, 202, 250)
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (217,180,231)

# Font/Text function
def textFont(text, font):
    textLook = font.render(text, True, BLACK)
    return textLook, textLook.get_rect()
# End of textFont()

# Function that creates a "START" button to the Main Menu
def toMenuButton(gamewindow, message, x, y, width, height, firstColour, secondColour):
    # Allow player to use their mouse
    pygame.event.get(pygame.MOUSEBUTTONDOWN)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Create button
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gamewindow, secondColour, (x, y, width, height))
        if click[0] == 1:
            menu(gamewindow)
    else:
        pygame.draw.rect(gamewindow, firstColour, (x, y, width, height))

    startFont = pygame.font.SysFont("timesnewroman", 25)
    textLook, font = textFont(message, startFont)
    font.center = ((x+(width/2)),(y+(height/2)))
    gamewindow.blit(textLook, font)
    pygame.display.update()
# End of toMenuButton()

# Function that creates the START PAGE
def startPage():
    # Create the display: size, name
    gamewindow = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("START Page")

    # Set Background Image
    startBackground = pygame.transform.scale(pygame.image.load("startBackground.jpg"), (1200, 800))
    gamewindow.blit(startBackground, (0, 0))

    # play music
    pygame.mixer.init()
    pygame.mixer.music.load("../song.ogg")
    pygame.mixer.music.set_volume(0.5)
    # play music over and over again
    pygame.mixer.music.play(-1)

    # Title of Page: "Welcome"
    titleFont = pygame.font.SysFont('constantia', 40)
    titleLook, titleFont = textFont("WELCOME!", titleFont)
    titleFont.center = (600, 200)
    gamewindow.blit(titleLook, titleFont)
    pygame.display.update()

    # Game loop
    startScreen = True
    while startScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # End of for loop

        # Allow player to use the mouse
        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Add the music font
        musicFont = pygame.font.SysFont('timesnewroman', 20)
        MusicFont = musicFont.render('Music:', True, BLACK)
        gamewindow.blit(MusicFont, (1050, 5))

        # Turn on Music Button
        if 1110 + 45 > mouse[0] > 1110 and 0 + 35 > mouse[1] > 0:
            pygame.draw.rect(gamewindow, WHITE, (1110, 0, 45, 35), 2)
            if click[0] == 1:
                pygame.mixer.music.unpause()
        else:
            pygame.draw.rect(gamewindow, BLACK, (1110, 0, 45, 35), 2)

        fonts = pygame.font.SysFont('timesnewroman', 15)
        on = fonts.render('ON', True, BLACK)
        On = on.get_rect()
        On.center = ((1110 + (45 / 2)), (0 + (35 / 2)))
        gamewindow.blit(on, On)

        # Stop Music Button
        if 1155 + 45 > mouse[0] > 1155 and 0 + 35 > mouse[1] > 0:
            pygame.draw.rect(gamewindow, WHITE, (1155, 0, 45, 35), 2)
            if click[0] == 1:
                pygame.mixer.music.pause()
        else:
            pygame.draw.rect(gamewindow, BLACK, (1155, 0, 45, 35), 2)

        off = fonts.render('OFF', True, BLACK)
        Off = off.get_rect()
        Off.center = ((1155 + (45 / 2)), (0 + (35 / 2)))
        gamewindow.blit(off, Off)
        toMenuButton(gamewindow, "START",550,250,100,50, BLUE, WHITE)
        pygame.display.update()
    # End of while loop
# End of startPage()

# MAIN CODE TO RUN THE GAME --------------------------------------------------------------------------------------------
startPage()
# ----------------------------------------------------------------------------------------------------------------------