import pygame,sys
from pygame.locals import*
from images import animalImageList, animalImageAnswers

pygame.init()
# Variables
RED = (252, 77, 80)
ORANGE = (255, 155, 0)
YELLOW = (255, 255, 0)
GREEN = (8, 242, 47)
LIGHTGREEN = (192, 248, 125)
BLUE = (130, 202, 250)
PURPLE = (166, 0, 255)
PINK = (255, 160, 233)
BLACK = (0, 0, 0)
LIGHTGREY = (225,225,225)
DARKGREY = (159,159,159)
WHITE = (255, 255, 255)
alreadyShown = []
points = 0

# Call functions to get lists of animal images
imagesList = animalImageList()
answerPics = animalImageAnswers()

# Function that keeps the same animal screen
def animalScreen(gamewindow):
    # Set the name of Display
    pygame.display.set_caption("Animal Guessing Game")
    gamewindow.fill(BLUE)
    # Set Background - Using a picture
    background = pygame.transform.scale(pygame.image.load(
        "animalGuessingBackground.jpg"), (1200, 800))
    gamewindow.blit(background, (0, 0))

    # Title
    fontTitle = pygame.font.SysFont('modernno20', 40)
    title = fontTitle.render('Animal Guessing Game', True, BLACK)
    Title = title.get_rect()
    Title.center = (600, 90)
    gamewindow.blit(title, Title)

    answerFont = pygame.font.SysFont('modernno20', 30)
    answer = answerFont.render('Type your answer:', True, BLACK)
    gamewindow.blit(answer, (320,520))
    pygame.display.update()
# End of animalScreen()

# Function that creates a back button
def backToGuessingChoice(gamewindow):
    global points
    from integratedGuessGame import guessingChoice
    pygame.event.get(pygame.MOUSEBUTTONDOWN)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    menuButton(gamewindow)

    # BACK button
    if 0 + 70 > mouse[0] > 0 and 0 + 30 > mouse[1] > 0:
        pygame.draw.rect(gamewindow, WHITE, (0, 0, 70, 30))
        if click[0] == 1:
            # Reset lists/score when player exits the game
            alreadyShown.clear()
            points = 0
            guessingChoice(gamewindow)
    else:
        pygame.draw.rect(gamewindow, DARKGREY, (0, 0, 70, 30))

    backFont = pygame.font.Font('freesansbold.ttf', 14)
    back = backFont.render('BACK', True, BLACK)
    Back = back.get_rect()
    Back.center = ((0 + (70 / 2)), (0 + (30 / 2)))
    gamewindow.blit(back, Back)
    pygame.display.update()
# End of backToGuessingChoice()

# Function that creates a textbox to get user input
def textBox(gamewindow, input, inputRect, text):
    if input:
        color = YELLOW
    else:
        color = LIGHTGREY
    pygame.draw.rect(gamewindow, color, inputRect)
    font = pygame.font.SysFont("timesnewroman", 25)
    textInput = font.render(text, True, BLACK)
    gamewindow.blit(textInput, (inputRect.x + 5, inputRect.y + 5))
    inputRect.w = max(150, textInput.get_width() + 10)
    pygame.display.update()
# End of textBox()

# Animal Guessing Game function
def animalGuess(gamewindow):
    from random import randrange
    global points
    # Create text box shape
    inputRect = pygame.Rect(550, 515, 150, 40)
    animalScreen(gamewindow)
    # Randomize images shown on screen
    randPics = randrange(len(imagesList))
    # List of answers to the images
    answers = ["Tiger", "Toucan", "Cheetah", "Eagle", "Lion", "Cat", "Kangaroo", "Cow", "Raccoon", "Meerkat",
               "Lemur", "Pig", "Armadillo", "Zebra", "Antelope", "Panda", "Giraffe", "Owl", "Butterfly", "Snake",
               "Chameleon", "Frog", "Turtle", "Hedgehog", "Porcupine", "Squirrel", "Swan"]

    # Output the Score
    font = pygame.font.Font('freesansbold.ttf', 30)
    scorefont = font.render("Score: " + str(points), True, (38,145,87))
    Scorefont = scorefont.get_rect()
    Scorefont.center = (600, 150)
    gamewindow.blit(scorefont, Scorefont)

    # Player can only guess 10 animal pictures every time they play the game
    # If player did not guess 10 times yet
    if len(alreadyShown) < 10:
        # Check to make sure the images do not repeat
        if imagesList[randPics] not in alreadyShown:
            alreadyShown.append(imagesList[randPics])
            # Output the images on screen
            images = imagesList[randPics]
            Images = images.get_rect()
            Images.center = (600, 330)
            gamewindow.blit(images, Images)
        # If images do repeat, shuffle the images again
        else:
            animalGuess(gamewindow)
    # If player guesses 10 times, game is over
    else:
        # Set Background - Using a picture
        overBackground = pygame.transform.scale(pygame.image.load(
            "animalBackground.jpg"), (1200, 800))
        gamewindow.blit(overBackground, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 50)
        timeOver = font.render('GAME OVER!', True, WHITE)
        TimeOver = timeOver.get_rect()
        TimeOver.center = (600, 100)
        gamewindow.blit(timeOver, TimeOver)
        # Output final score
        finalScore = font.render("Final Score: " + str(points), True, GREEN)
        FinalScore = finalScore.get_rect()
        FinalScore.center = (600, 230)
        gamewindow.blit(finalScore, FinalScore)
        buttons(gamewindow)
        pygame.display.update()
    pygame.display.update()

    # Game loop
    input = False
    text = ""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Check if player uses their mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Let the player type their guess only if they clicked on the textbox
                if inputRect.collidepoint(event.pos):
                    input = True
                else:
                    input = False
            # Check if player uses keyboard
            elif event.type == pygame.KEYDOWN:
                # Check if textbox was clicked
                if input:
                    # If 11 letters were typed in textbox, don't let player type anymore
                    if len(text) > 11:
                        input = False
                        # Check if player uses backspace key
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                    # Check if player uses backspace key
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    # Check if player uses enter/return key
                    elif event.key == pygame.K_RETURN:
                        for i in range(len(imagesList)):
                            if imagesList[i] == imagesList[randPics]:
                                # Remove all spaces in user input
                                text = text.replace(' ', '')
                                # Check if player guesses the answer correctly
                                if text.capitalize() == answers[i]:
                                    gamewindow.fill(LIGHTGREEN)
                                    congratsBackground = pygame.transform.scale(pygame.image.load(
                                        "congratsBackground.png"), (1200, 800)).convert_alpha()
                                    gamewindow.blit(congratsBackground, (0, 0))
                                    font = pygame.font.Font('freesansbold.ttf', 60)
                                    correct = font.render('Correct!', True, BLACK)
                                    Correct = correct.get_rect()
                                    Correct.center = (600, 120)
                                    gamewindow.blit(correct, Correct)
                                    points += 1

                                    # Output the word answer
                                    answerFont = pygame.font.SysFont('timesnewroman', 50)
                                    answer2 = answerFont.render(answers[i], True, BLACK)
                                    Answer2 = answer2.get_rect()
                                    Answer2.center = (600, 570)
                                    gamewindow.blit(answer2, Answer2)

                                    # Output the answer picture
                                    pics = answerPics[i]
                                    Pics = pics.get_rect()
                                    Pics.center = (600, 340)
                                    gamewindow.blit(pics, Pics)
                                    pygame.display.update()
                                    pygame.time.wait(2200)
                                    animalGuess(gamewindow)

                                # Check if player gets the answer wrong
                                else:
                                    gamewindow.fill(RED)
                                    font = pygame.font.Font('freesansbold.ttf', 60)
                                    incorrect = font.render('Incorrect!', True, WHITE)
                                    Incorrect = incorrect.get_rect()
                                    Incorrect.center = (600, 100)
                                    gamewindow.blit(incorrect, Incorrect)
                                    answerFont = pygame.font.SysFont('timesnewroman', 50)
                                    answer = answerFont.render("The Correct Answer is : " + answers[i], True, BLACK)
                                    Answer = answer.get_rect()
                                    Answer.center = (600, 550)
                                    gamewindow.blit(answer, Answer)

                                    # Output the answer picture
                                    pics = answerPics[i]
                                    Pics = pics.get_rect()
                                    Pics.center = (600, 330)
                                    gamewindow.blit(pics, Pics)
                                    pygame.display.update()
                                    pygame.time.wait(3000)
                                    animalGuess(gamewindow)
                        # End of inner for loop
                    else:
                        text += event.unicode
        # End of for loop
        # Create back button
        backToGuessingChoice(gamewindow)
        # Create text box
        textBox(gamewindow, input, inputRect, text)
    # End of while loop
# End of animalGuess()

# Function for buttons
def buttons(gamewindow):
    global points
    while True:
        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Play Again Button
        if 550 + 120 > mouse[0] > 550 and 340 + 40 > mouse[1] > 340:
            pygame.draw.rect(gamewindow, WHITE, (550, 340, 120, 40))
            if click[0] == 1:
                # Reset variables when player starts game
                alreadyShown.clear()
                points = 0
                animalGuess(gamewindow)
        else:
            pygame.draw.rect(gamewindow, YELLOW, (550, 340, 120, 40))

        fonts = pygame.font.Font('freesansbold.ttf', 20)
        again = fonts.render('Play Again!', True, BLACK)
        Again = again.get_rect()
        Again.center = ((550 + (120 / 2)), (340 + (40 / 2)))
        gamewindow.blit(again, Again)
        menuButton(gamewindow)
    # End of while loop
# End of buttons()

# Main Menu function button
def menuButton(gamewindow):
    from mainMenu import menu
    global points
    pygame.event.get(pygame.MOUSEBUTTONDOWN)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Main Menu button
    if 1130 + 70 > mouse[0] > 1130 and 0 + 30 > mouse[1] > 0:
        pygame.draw.rect(gamewindow, WHITE, (1130, 0, 70, 30))
        if click[0] == 1:
            alreadyShown.clear()
            points = 0
            menu(gamewindow)
    else:
        pygame.draw.rect(gamewindow, YELLOW, (1130, 0, 70, 30))

    backFont = pygame.font.Font('freesansbold.ttf', 12)
    back = backFont.render('Main Menu', True, BLACK)
    Back = back.get_rect()
    Back.center = ((1130 + (70 / 2)), (0 + (30 / 2)))
    gamewindow.blit(back, Back)
    pygame.display.update()
# End of menuButton()