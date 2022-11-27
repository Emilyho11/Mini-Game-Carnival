import pygame,sys
from pygame.locals import*
from array import array
from random import randrange
intarray = array('i')
pygame.init()

# Variables:
RED = (255, 0, 0)
ORANGE = (255, 155, 0)
YELLOW = (255, 255, 0)
GREEN = (140, 240, 89)
BLUE = (130, 202, 250)
PURPLE = (166, 0, 255)
PINK = (255, 160, 233)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)
answer = False
x = 200
y = 500
velocity = 70
mathquestions = ["6 x 6 = ?",
                 "24 + 42 = ?",
                 "52 - 38 = ?",
                 "9 ÷ 3 = ?",
                 "17 x 2 = ?",
                 "49 - 26 = ?",
                 "72 + 16 = ?",
                 "96 ÷ 8 = ?",
                 "7 x 12 = ?",
                 "49 + 71 = ?"]
mathAnswers = ['36', '66', '14', '3', '34', '23', '88', '12', '84', '120']

appleLocationX = [540, 900, 420, 300, 700, 860, 520, 300, 550, 720]
appleLocationY = [170, 170, 330, 220, 220, 310, 270, 380, 370, 320]

# Randomize the locations
randLocationX = randrange(len(appleLocationX))
randomPlace = appleLocationX[randLocationX]

def fontNum(gamewindow, message, x, y):
    font = pygame.font.SysFont('arialrounded', 25)
    num = font.render(message, True, WHITE)
    Num = num.get_rect()
    Num.center = (x + 25, y + 30)
    gamewindow.blit(num, Num)
    pygame.display.update()

def appleScreen(gamewindow):
    pygame.display.set_caption("Apple Picking Game")

    # Background
    gamewindow.fill(BLUE)
    pygame.draw.rect(gamewindow, GREEN, (0, 450, 1200, 350))

    # Title
    font = pygame.font.Font('freesansbold.ttf', 30)
    explanation = font.render('Make all the apples disappear by answering the questions!', True, BLACK)
    Explanation = explanation.get_rect()
    Explanation.center = (600, 30)
    gamewindow.blit(explanation, Explanation)

    # Trees
    tree = pygame.transform.scale(pygame.image.load("tree.png"), (400, 500))
    gamewindow.blit(tree, (620, 150))
    for appletree in range(2):
        gamewindow.blit(tree, (230 + appletree * 190, 150))

    # Apple Picking Basket
    basket = pygame.transform.scale(pygame.image.load("basket.png"), (150, 150))
    gamewindow.blit(basket, (400, 500))
    gamewindow.blit(basket, (700, 500))
    pygame.display.update()


def applePicking(gamewindow):
    from reusableFunctions import backToMainMenu
    randQuestions = randrange(len(mathquestions))
    appleScreen(gamewindow)

    # Function that allows player to click the apple
    def clickApple(gamewindow, appleSelected, x, y, appleNum, num, randQuestions):
        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x + 50 > mouse[0] > x and y + 50 > mouse[1] > y):
            if click[0] == 1:
                appleSelected = appleNum[num]

        for i in range(len(mathquestions)):
            if mathquestions[i] == mathquestions[randQuestions]:
                if appleSelected == mathAnswers[i]:
                    gamewindow.fill(BLUE)
                    congratsBackground = pygame.transform.scale(pygame.image.load(
                        "congratsBackground.png"),
                                                                (1200, 800))
                    gamewindow.blit(congratsBackground, (0, 0))
                    font = pygame.font.Font('freesansbold.ttf', 60)
                    correct = font.render('Correct!', True, BLACK)
                    Correct = correct.get_rect()
                    Correct.center = (600, 120)
                    gamewindow.blit(correct, Correct)
                    pygame.display.update()
                    pygame.time.wait(3000)
                    applePicking(gamewindow)

    # Math Questions
    font = pygame.font.Font('freesansbold.ttf', 40)
    questionone = font.render(mathquestions[randQuestions], True, BLACK)
    Questionone = questionone.get_rect()
    Questionone.center = (600, 700)
    gamewindow.blit(questionone, Questionone)

    # Apples
    apple = pygame.transform.scale(pygame.image.load("apple.png"), (50, 50))
    for items in range(len(appleLocationX)):
        gamewindow.blit(apple, (appleLocationX[items], appleLocationY[items]))

    # Answers on apples
    appleNum = []
    while len(appleNum) < 10:
        randAnswers = randrange(len(mathAnswers))
        if mathAnswers[randAnswers] not in appleNum:
            appleNum.append(mathAnswers[randAnswers])

    apple1 = fontNum(gamewindow, appleNum[0], 540, 170)
    apple2 = fontNum(gamewindow, appleNum[1], 900, 170)
    apple3 = fontNum(gamewindow, appleNum[2], 420, 330)
    apple4 = fontNum(gamewindow, appleNum[3], 300, 220)
    apple5 = fontNum(gamewindow, appleNum[4], 700, 220)
    apple6 = fontNum(gamewindow, appleNum[5], 860, 310)
    apple7 = fontNum(gamewindow, appleNum[6], 520, 270)
    apple8 = fontNum(gamewindow, appleNum[7], 300, 380)
    apple9 = fontNum(gamewindow, appleNum[8], 550, 370)
    apple10 = fontNum(gamewindow, appleNum[9], 720, 320)
    pygame.display.update()

    points = 0
    appleanswer = False
    applebuttons = True
    appleSelected = ""
    while (applebuttons):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        backToMainMenu(gamewindow)
        backToAppleInstructions(gamewindow)

        # Player can click the apple
        clickApple(gamewindow, appleSelected, 540, 170, appleNum, 0, randQuestions)
        clickApple(gamewindow, appleSelected, 900, 170, appleNum, 1, randQuestions)
        clickApple(gamewindow, appleSelected, 420, 330, appleNum, 2, randQuestions)
        clickApple(gamewindow, appleSelected, 300, 220, appleNum, 3, randQuestions)
        clickApple(gamewindow, appleSelected, 700, 220, appleNum, 4, randQuestions)
        clickApple(gamewindow, appleSelected, 860, 310, appleNum, 5, randQuestions)
        clickApple(gamewindow, appleSelected, 520, 270, appleNum, 6, randQuestions)
        clickApple(gamewindow, appleSelected, 300, 380, appleNum, 7, randQuestions)
        clickApple(gamewindow, appleSelected, 550, 370, appleNum, 8, randQuestions)
        clickApple(gamewindow, appleSelected, 720, 320, appleNum, 9, randQuestions)


def backToAppleInstructions(gamewindow):
    pygame.event.get(pygame.MOUSEBUTTONDOWN)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # BACK button
    if 0 + 70 > mouse[0] > 0 and 0 + 30 > mouse[1] > 0:
        pygame.draw.rect(gamewindow, WHITE, (0, 0, 70, 30))
        if click[0] == 1:
            appleInstructions(gamewindow)
    else:
        pygame.draw.rect(gamewindow, GREY, (0, 0, 70, 30))

    backFont = pygame.font.Font('freesansbold.ttf', 14)
    back = backFont.render('BACK', True, BLACK)
    Back = back.get_rect()
    Back.center = ((0 + (70 / 2)), (0 + (30 / 2)))
    gamewindow.blit(back, Back)
    pygame.display.update()


def appleInstructions(gamewindow):
    from reusableFunctions import backToMainMenu
    # Set Background - Using a picture
    spaceBackground = pygame.transform.scale(pygame.image.load(
        "appleBackground.jpg"), (1200, 800))
    gamewindow.blit(spaceBackground, (0, 0))
    pygame.display.set_caption("TicTacToe")

    pygame.draw.rect(gamewindow, YELLOW, (350,300,565,230))

    instructionFont = pygame.font.SysFont('arialrounded', 40)
    instruction = instructionFont.render('Apple Picking Instructions', True, BLACK)
    gamewindow.blit(instruction, (365,305))

    # Write the instructions
    counter = 0
    text = ['Welcome to Apple Picking Game!',
            ' - Select the apple that best answers the question',
            '',
            'Click the START button to play!']
    for x in text:
        counter += 1
        fonts = pygame.font.SysFont('constantia', 25).render(x, True, BLACK)
        gamewindow.blit(fonts, (365, 350 + (30 * counter)))

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

        # Button to apple picking game
        if 360 + 150 > mouse[0] > 360 and 550 + 50 > mouse[1] > 550:
            pygame.draw.rect(gamewindow, GREY, (360, 550, 150, 50))
            if click[0] == 1:
                applePicking(gamewindow)
        else:
            pygame.draw.rect(gamewindow, YELLOW, (360, 550, 150, 50))

        startFont = pygame.font.Font('freesansbold.ttf', 20)
        start = startFont.render('START GAME', True, BLACK)
        Start = start.get_rect()
        Start.center = ((360 + (150 / 2)), (550 + (50 / 2)))
        gamewindow.blit(start, Start)
        backToMainMenu(gamewindow)