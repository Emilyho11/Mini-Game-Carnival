import pygame
pygame.init()

# Variables
BLUE = (130, 202, 250)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 155, 0)
YELLOW = (255, 255, 0)
GREEN = (8, 242, 47)
PURPLE = (166, 0, 255)
PINK = (255, 160, 233)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)

# Go to Main Menu (back) Function
def backToMainMenu(gamewindow):
    from mainMenu import menu
    # Main Menu button
    pygame.event.get(pygame.MOUSEBUTTONDOWN)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Main Menu Button
    if 1130 + 70 > mouse[0] > 1130 and 0 + 30 > mouse[1] > 0:
        pygame.draw.rect(gamewindow, WHITE, (1130, 0, 70, 30))
        if click[0] == 1:
            menu(gamewindow)
    else:
        pygame.draw.rect(gamewindow, YELLOW, (1130, 0, 70, 30))

    backFont = pygame.font.Font('freesansbold.ttf', 12)
    back = backFont.render('Main Menu', True, BLACK)
    Back = back.get_rect()
    Back.center = ((1130 + (70 / 2)), (0 + (30 / 2)))
    gamewindow.blit(back, Back)
    pygame.display.update()
# End of backToMainMenu()
