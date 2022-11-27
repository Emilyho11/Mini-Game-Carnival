import pygame,sys
from pygame.locals import*
from images import disneyImageList, disneyImageAnswers

pygame.init()
# Variables
RED = (252, 77, 80)
YELLOW = (255, 255, 0)
GREEN = (8, 242, 47)
BLUE = (130, 202, 250)
PURPLE = (166, 0, 255)
PINK = (255, 160, 233)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)
alreadyShown = []
points = 0

# Call the functions that returns a list of disney images
imagesList = disneyImageList()
answerPics = disneyImageAnswers()

# Function that creates a textbox to get user input
def disneyTextBox(gamewindow, input, inputRect, text):
    if input:
        color = PURPLE
    else:
        color = PINK
    pygame.draw.rect(gamewindow, color, inputRect)
    font = pygame.font.SysFont("timesnewroman", 25)
    textInput = font.render(text, True, BLACK)
    gamewindow.blit(textInput, (inputRect.x + 5, inputRect.y + 5))
    inputRect.w = max(210, textInput.get_width() + 10)
    pygame.display.update()
# End of disneyTextBox()

# Disney Screen Function - It displays the same look on the screen
def disneyScreen(gamewindow):
    # Set the name of Display
    pygame.display.set_caption("Disney Guessing Game")
    # Set Background - Using a picture
    background = pygame.transform.scale(pygame.image.load(
        "disneyBackground.jpeg"), (1200, 800))
    gamewindow.blit(background, (0, 0))

    # Title
    fontTitle = pygame.font.SysFont('modernno20', 40)
    title = fontTitle.render('Disney Guessing Game', True, BLACK)
    Title = title.get_rect()
    Title.center = (600, 80)
    gamewindow.blit(title, Title)

    answerFont = pygame.font.SysFont('modernno20', 30)
    answer = answerFont.render('Type your answer:', True, BLACK)
    gamewindow.blit(answer, (360, 540))
    pygame.display.update()
# End of disneyScreen()

# Disney Guessing Game Function
def disneyGuess(gamewindow):
    from random import randrange
    global points
    # Create the user input rectangle
    inputRect = pygame.Rect(590, 537, 150, 40)
    disneyScreen(gamewindow)
    # Randomly generate the disney images
    randPics = randrange(len(imagesList))
    answers = ["stitch", "cinderella", "ariel", "beast", "genie", "abu", "anna", "elsa", "bambi", "pinocchio",
               "peterpan", "captainhook", "dumbo", "cheshirecat", "mulan", "belle", "tarzan", "mickeymouse", "goofy",
               "pluto", "rapunzel", "gus", "hades", "nemo", "baymax", "jafar", "lady", "ladytremaine", "lumiere",
               "magiccarpet", "maleficent", "marypoppins", "moana", "mushu", "olaf", "pumbaa", "timon",
               "winniethepooh", "rafiki", "sebastian", "flounder", "sven", "tigger", "tinkerbell", "tramp", "ursula",
               "wreck-itralph", "buzzlightyear", "woody", "aladdin", "dory", "wall-e", "mike", "yoda", "joy", "sadness",
               "minniemouse", "merida", "maui", "lightningmcqueen", "mater", "chewbacca", "chip", "forky", "hercules"]

    outputAnswers = ["Stitch (Lilo and Stitch)", "Cinderella", "Ariel (The Little Mermaid)", "Beast (Beauty and the Beast)",
                "Genie (Aladdin)", "Abu (Aladdin)", "Anna (Frozen)", "Elsa (Frozen)", "Bambi", "Pinocchio",
                "Peter Pan", "Captain Hook (Peter Pan)", "Dumbo", "Cheshire Cat (Alice in Wonderland)", "Mulan",
                "Belle (Beauty and the Beast)", "Tarzan", "Mickey Mouse", "Goofy (Mickey Mouse)", "Pluto (Mickey Mouse)",
                "Rapunzel (Tangled)", "Gus (Cinderella)", "Hades (Hercules)", "Nemo (Finding Nemo)",
                "Baymax (Big Hero 6)", "Jafar (Aladdin)", "Lady (Lady and the Tramp)", "Lady Tremaine (Cinderella)",
                "Lumiere (Beauty and the Beast)", "Magic Carpet (Aladdin)", "Maleficent", "Mary Poppins", "Moana",
                "Mushu (Mulan)", "Olaf (Frozen)", "Pumbaa (The Lion King)", "Timon (The Lion King)", "Winnie the Pooh",
                "Rafiki (The Lion King)", "Sebastian (The Little Mermaid)", "Flounder (The Little Mermaid)",
                "Sven (Frozen)", "Tigger (Winnie the Pooh)", "Tinker Bell", "Tramp (Lady and the Tramp)",
                "Ursula (The Little Mermaid)", "Wreck-it Ralph", "Buzz Lightyear (Toy Story)", "Woody (Toy Story)",
                "Aladdin", "Dory (Finding Nemo)", "WALL-E", "Mike (Monsters Inc.)", "Yoda (Star Wars)", "Joy (Inside Out)",
                "Sadness (Inside Out)", "Minnie Mouse", "Merida (Brave)", "Maui (Moana)", "Lightning McQueen (Cars)",
                "Mater (Cars)", "Chewbacca (Star Wars)", "Chip (Beauty and the Beast)", "Forky (Toy Story 4)", "Hercules"]

    # Output the Score
    font = pygame.font.SysFont('modernno20', 45)
    scorefont = font.render("Score: " + str(points), True, RED)
    Scorefont = scorefont.get_rect()
    Scorefont.center = (600, 150)
    gamewindow.blit(scorefont, Scorefont)

    # Player can only guess 10 disney pictures each time they play the game
    # If player did not guess 10 times yet
    if len(alreadyShown) < 10:
        # Make sure the pictures shown do not repeat
        if imagesList[randPics] not in alreadyShown:
            alreadyShown.append(imagesList[randPics])
            images = imagesList[randPics]
            Images = images.get_rect()
            Images.center = (600, 340)
            gamewindow.blit(images, Images)
        else:
            disneyGuess(gamewindow)
    # If player did guessed 10 times, it is game over
    else:
        # Set Background - Using a picture
        overBackground = pygame.transform.scale(pygame.image.load(
            "disneyBackground.jpeg"), (1200, 800))
        gamewindow.blit(overBackground, (0, 0))
        font = pygame.font.SysFont('constantia', 60)
        timeOver = font.render('GAME OVER!', True, BLACK)
        TimeOver = timeOver.get_rect()
        TimeOver.center = (600, 230)
        gamewindow.blit(timeOver, TimeOver)
        # Output final score
        finalScore = font.render("Final Score: " + str(points), True, RED)
        FinalScore = finalScore.get_rect()
        FinalScore.center = (600, 335)
        gamewindow.blit(finalScore, FinalScore)
        disneyButtons(gamewindow)
    pygame.display.update()

    input = False
    text = ""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Check if mouse is used
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if inputRect.collidepoint(event.pos):
                    input = True
                else:
                    input = False
            # Check if keyboard is used
            elif event.type == pygame.KEYDOWN:
                # Check if there are letters in the textbox
                if input:
                    # If text in the text box has over 17 letters, player can't type anymore
                    if len(text) > 17:
                        input = False
                        # Let player use the backspace key
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                    # Let player use the backspace key
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    # If player uses the enter/return key
                    elif event.key == pygame.K_RETURN:
                        for i in range(len(imagesList)):
                            if imagesList[i] == imagesList[randPics]:
                                # Remove all spaces in user input
                                text = text.replace(' ', '')
                                # Check if the text entered is the right answer (use indexing)
                                if text.lower() == answers[i]:
                                    points += 1
                                    # Set background
                                    gamewindow.fill(BLUE)
                                    congratsBackground = pygame.transform.scale(pygame.image.load(
                                        "congratsBackground.png"), (1200, 800))
                                    gamewindow.blit(congratsBackground, (0, 0))
                                    font = pygame.font.Font('freesansbold.ttf', 60)
                                    correct = font.render('Correct!', True, BLACK)
                                    Correct = correct.get_rect()
                                    Correct.center = (600, 120)
                                    gamewindow.blit(correct, Correct)

                                    # Output the word answer
                                    answerFont = pygame.font.SysFont('timesnewroman', 50)
                                    answer2 = answerFont.render(outputAnswers[i], True, BLACK)
                                    Answer2 = answer2.get_rect()
                                    Answer2.center = (600, 590)
                                    gamewindow.blit(answer2, Answer2)

                                    # Output the answer picture
                                    pics = answerPics[i]
                                    Pics = pics.get_rect()
                                    Pics.center = (600, 350)
                                    gamewindow.blit(pics, Pics)
                                    pygame.display.update()
                                    pygame.time.wait(2200)
                                    disneyGuess(gamewindow)
                                # If the text entered is the wrong answer
                                else:
                                    gamewindow.fill(RED)
                                    font = pygame.font.Font('freesansbold.ttf', 60)
                                    incorrect = font.render('Incorrect!', True, WHITE)
                                    Incorrect = incorrect.get_rect()
                                    Incorrect.center = (600, 100)
                                    gamewindow.blit(incorrect, Incorrect)
                                    answerFont = pygame.font.SysFont('timesnewroman', 50)
                                    answer = answerFont.render('The Correct Answer is :', True, BLACK)
                                    Answer = answer.get_rect()
                                    Answer.center = (600, 550)
                                    gamewindow.blit(answer, Answer)

                                    # Output the word answer
                                    answer2 = answerFont.render(outputAnswers[i], True, BLACK)
                                    Answer2 = answer2.get_rect()
                                    Answer2.center = (600, 610)
                                    gamewindow.blit(answer2, Answer2)

                                    # Output the answer picture
                                    pics = answerPics[i]
                                    Pics = pics.get_rect()
                                    Pics.center = (600, 320)
                                    gamewindow.blit(pics, Pics)
                                    pygame.display.update()
                                    pygame.time.wait(3000)
                                    disneyGuess(gamewindow)
                        # End of inner for loop
                    else:
                        text += event.unicode
        # End of for loop
        # Call the Back button function
        toGuessingChoice(gamewindow)
        # Create user input textbox
        disneyTextBox(gamewindow, input, inputRect, text)
    # End of while loop
# End of disneyGuess()

# Function that creates a button to go to the Disney Game
def disneyButtons(gamewindow):
    from animals import menuButton
    global points
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # End of for loop
        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Play Again Button
        if 550 + 120 > mouse[0] > 550 and 460 + 40 > mouse[1] > 460:
            pygame.draw.rect(gamewindow, WHITE, (550, 460, 120, 40))
            if click[0] == 1:
                alreadyShown.clear()
                points = 0
                disneyGuess(gamewindow)
        else:
            pygame.draw.rect(gamewindow, YELLOW, (550, 460, 120, 40))

        fonts = pygame.font.Font('freesansbold.ttf', 20)
        again = fonts.render('Play Again!', True, BLACK)
        Again = again.get_rect()
        Again.center = ((550 + (120 / 2)), (460 + (40 / 2)))
        gamewindow.blit(again, Again)
        menuButton(gamewindow)
    # End of while loop
# End of disneyButtons()

# Function that creates a back button
def toGuessingChoice(gamewindow):
    from animals import menuButton
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
            alreadyShown.clear()
            points = 0
            guessingChoice(gamewindow)
    else:
        pygame.draw.rect(gamewindow, YELLOW, (0, 0, 70, 30))

    backFont = pygame.font.Font('freesansbold.ttf', 14)
    back = backFont.render('BACK', True, BLACK)
    Back = back.get_rect()
    Back.center = ((0 + (70 / 2)), (0 + (30 / 2)))
    gamewindow.blit(back, Back)
    pygame.display.update()
# End of toGuessingChoice()
