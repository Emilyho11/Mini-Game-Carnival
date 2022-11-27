import pygame, time, sys
from array import array
from random import randrange
from pygame.locals import *
intarray = array('i')
pygame.init()

# Variables:
RED = (255, 0, 0)
ORANGE = (255, 155, 0)
YELLOW = (255, 255, 0)
GREEN = (8, 242, 47)
BLUE = (130, 202, 250)
PURPLE = (166, 0, 255)
PINK = (255, 160, 233)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)

# Space Game Function
def spaceGame(gamewindow):
    from mainMenu import menu
    # Set of questions on planets
    questions = ["What is the hottest planet?",
                 "Which planet has the most moons?",
                 "What is the farthest planet from the sun?",
                 "What planet has life forms on it?",
                 "What planet is closest in size to Earth?",
                 "What is the brightest planet in the night sky?",
                 "Phobos and Deimos are moons of what planet?",
                 "What is the largest planet in the solar system?",
                 "What is the 6th planet from the sun?",
                 "What is the smallest planet?",
                 "What planet was named after the Roman goddess of love and beauty?",
                 "Which planet has oxygen and nitrogen?",
                 "Which planet (not including Earth) has mountains, valleys, and canyons?",
                 "Which planet orbits on its side?",
                 "Which is the fastest planet to orbit the sun?",
                 "Which planet has liquid water on the surface?",
                 "What is the 7th planet from the sun?",
                 "Which planet rotates in the opposite direction from all the other planets?",
                 "What is the most explored planet (not including Earth)?",
                 "Which planet has the shortest days?",
                 "Which planet has the largest moon in the solar system?",
                 "What is the second largest planet in the solar system?",
                 "Which planet has 13 rings?",
                 "What is the coldest planet in the solar system?",
                 "Which planet has rings visible to the naked eye?",
                 "_______ is called the \"Red planet\"",
                 "Which planet has a runaway greenhouse effect?"]
    # Set of answers to the questions
    answers = ["Venus", "Saturn", "Neptune", "Earth", "Venus", "Venus", "Mars", "Jupiter", "Saturn", "Mercury",
               "Venus", "Earth", "Mars", "Uranus", "Mercury", "Earth", "Uranus", "Venus", "Mars", "Jupiter", "Jupiter",
               "Saturn", "Uranus", "Neptune", "Saturn", "Mars", "Venus"]
    question_index = 0
    score = 0
    pygame.display.set_caption("Space Game")
    # Set Timer Variables
    clock = pygame.time.Clock()
    count = 0
    rate = 60
    startTime = 60

    # Game Loop
    mainscreen = True
    while (mainscreen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # End of for loop
        # Set Background - Using a picture
        spaceBackground = pygame.transform.scale(pygame.image.load("space background.jfif"), (1200, 800))
        gamewindow.blit(spaceBackground, (0, 0))

        # Set Planets and their names
        mercury = pygame.transform.scale(pygame.image.load("mercury.png"), (80, 70))
        gamewindow.blit(mercury, (300, 200))
        mercurytext = pygame.transform.scale(pygame.image.load("mercurytext.png"), (90, 70))
        gamewindow.blit(mercurytext, (295, 200))

        venus = pygame.transform.scale(pygame.image.load("venus.png"), (80, 80))
        gamewindow.blit(venus, (420, 200))
        venustext = pygame.transform.scale(pygame.image.load("venustext.png"), (80, 70))
        gamewindow.blit(venustext, (420, 200))

        earth = pygame.transform.scale(pygame.image.load("earth.png"), (90, 90))
        gamewindow.blit(earth, (535, 200))
        earthtext = pygame.transform.scale(pygame.image.load("earthtext.png"), (80, 70))
        gamewindow.blit(earthtext, (540, 205))

        mars = pygame.transform.scale(pygame.image.load("mars.png"), (100, 100))
        gamewindow.blit(mars, (645, 200))
        marstext = pygame.transform.scale(pygame.image.load("marstext.png"), (80, 60))
        gamewindow.blit(marstext, (655, 220))

        jupiter = pygame.transform.scale(pygame.image.load("jupiter.png"), (210, 210))
        gamewindow.blit(jupiter, (730, 150))
        jupitertext = pygame.transform.scale(pygame.image.load("jupitertext.png"), (90, 70))
        gamewindow.blit(jupitertext, (790, 220))

        saturn = pygame.transform.scale(pygame.image.load("saturn.png"), (220, 135))
        gamewindow.blit(saturn, (330, 330))
        saturntext = pygame.transform.scale(pygame.image.load("saturntext.png"), (90, 70))
        gamewindow.blit(saturntext, (400, 340))

        uranus = pygame.transform.scale(pygame.image.load("uranus.png"), (100, 100))
        gamewindow.blit(uranus, (550, 345))
        uranustext = pygame.transform.scale(pygame.image.load("uranustext.png"), (90, 70))
        gamewindow.blit(uranustext, (550, 355))

        neptune = pygame.transform.scale(pygame.image.load("neptune.png"), (110, 110))
        gamewindow.blit(neptune, (700, 350))
        neptunetext = pygame.transform.scale(pygame.image.load("neptunetext.png"), (100, 80))
        gamewindow.blit(neptunetext, (710, 370))

        # Instruction
        font = pygame.font.Font('freesansbold.ttf', 30)
        description = font.render('Click on the planet that best answers the question', True, WHITE)
        Description = description.get_rect()
        Description.center = (600, 100)
        gamewindow.blit(description, Description)

        # Display Questions
        randquestions = randrange(len(questions))
        font = pygame.font.Font('freesansbold.ttf', 30)
        questionone = font.render(questions[randquestions], True, YELLOW)
        Questionone = questionone.get_rect()
        Questionone.center = (600, 600)
        gamewindow.blit(questionone, Questionone)

        # Display Score
        font = pygame.font.Font('freesansbold.ttf', 30)
        scorefont = font.render("Score: " + str(score), True, YELLOW)
        Scorefont = scorefont.get_rect()
        Scorefont.center = (600, 50)
        gamewindow.blit(scorefont, Scorefont)

        # Display Main Menu button font
        pygame.draw.rect(gamewindow, YELLOW, (1130, 0, 70, 30))
        backFont = pygame.font.Font('freesansbold.ttf', 12)
        back = backFont.render('Main Menu', True, BLACK)
        Back = back.get_rect()
        Back.center = ((1130 + (70 / 2)), (0 + (30 / 2)))
        gamewindow.blit(back, Back)
        pygame.display.update()

        numofquestions = len(questions)
        planet_selected = ""
        question1 = True
        while (question1 and (question_index <= numofquestions)):
            pygame.event.get(pygame.MOUSEBUTTONDOWN)
            mouse = pygame.mouse.get_pos()

            # TIMER
            totalSeconds = startTime - (count // rate)
            # Divide by 60 to get the minutes
            minutes = totalSeconds // 60
            # Use modulus (remainder) to get seconds
            seconds = totalSeconds % 60

            # Use python string formatting to format in leading zeros
            outputTime = "Time left: {0:02}:{1:02}".format(minutes, seconds)

            # Blit to the screen
            pygame.draw.rect(gamewindow, BLACK, (18, 45, 150, 30))
            timeFont = pygame.font.Font(None, 25)
            text = timeFont.render(outputTime, True, WHITE)
            gamewindow.blit(text, [20, 50])

            if totalSeconds <= 0:
                # Set Background - Using a picture
                spaceBackground = pygame.transform.scale(pygame.image.load("solarSystem.jpg"), (1200, 800))
                gamewindow.blit(spaceBackground, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 50)
                timeOver = font.render('GAME OVER!', True, WHITE)
                TimeOver = timeOver.get_rect()
                TimeOver.center = (600, 100)
                gamewindow.blit(timeOver, TimeOver)
                finalScore = font.render("Final Score: " + str(score), True, GREEN)
                FinalScore = finalScore.get_rect()
                FinalScore.center = (600, 230)
                gamewindow.blit(finalScore, FinalScore)
                question1 = False
                mainscreen = False
                toButtons(gamewindow)
                pygame.display.update()

            count += 1
            # Limit frames per second
            clock.tick(rate)
            pygame.display.update()

            for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                # Button to go back to main menu
                if 1130 + 70 > mouse[0] > 1130 and 0 + 30 > mouse[1] > 0:
                    planet_selected = "Main Menu"

                if 300 + 80 > mouse[0] > 300 and 200 + 70 > mouse[1] > 200:
                    planet_selected = "Mercury"

                if 420 + 80 > mouse[0] > 420 and 200 + 80 > mouse[1] > 200:
                    planet_selected = "Venus"

                if 535 + 90 > mouse[0] > 535 and 200 + 90 > mouse[1] > 200:
                    planet_selected = "Earth"

                if 645 + 100 > mouse[0] > 645 and 200 + 100 > mouse[1] > 200:
                    planet_selected = "Mars"

                if 730 + 210 > mouse[0] > 730 and 150 + 210 > mouse[1] > 150:
                    planet_selected = "Jupiter"

                if 330 + 220 > mouse[0] > 330 and 330 + 135 > mouse[1] > 330:
                    planet_selected = "Saturn"

                if 550 + 100 > mouse[0] > 550 and 345 + 100 > mouse[1] > 345:
                    planet_selected = "Uranus"

                if 700 + 110 > mouse[0] > 700 and 350 + 110 > mouse[1] > 350:
                    planet_selected = "Neptune"

                # =============================================================================================

                # Output Correct or Incorrect
                for i in range(len(questions)):
                    # Get the index of the random question in the questions list
                    if questions[i] == questions[randquestions]:
                        # Check if the planet selected is the correct answer
                        if planet_selected == answers[i]:
                            gamewindow.fill(BLACK)
                            font = pygame.font.Font('freesansbold.ttf', 50)
                            correct = font.render('Correct!', True, GREEN)
                            score += 1
                            Correct = correct.get_rect()
                            Correct.center = (600, 350)
                            gamewindow.blit(correct, Correct)
                            question1 = False
                            mainscreen = True
                            pygame.display.update()
                            pygame.time.wait(300)

                        elif planet_selected == "Main Menu":
                            menu(gamewindow)

                        else:
                            gamewindow.fill(BLACK)
                            font = pygame.font.Font('freesansbold.ttf', 50)
                            incorrect = font.render('Incorrect. Try Again!', True, RED)
                            Incorrect = incorrect.get_rect()
                            Incorrect.center = (600, 350)
                            gamewindow.blit(incorrect, Incorrect)
                            # Lose a point if you get the wrong answer
                            score -= 1
                            # Make sure score does not go below 0 if player gets an incorrect answer
                            if score < 0:
                                score+=1
                            question1 = False
                            mainscreen = True
                            pygame.display.update()
                            pygame.time.wait(300)
                # End of inner for loop
            # End of for loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            # End of for loop
        # End of inner while loop
    # End of while loop
# End of spaceGame()

# Space Instructions Function
def spaceInstructions(gamewindow):
    from mainMenu import menu
    ORANGE = (249,195,100)
    YELLOW = (249,248,100)

    # Set Background - Using a picture
    spaceBackground = pygame.transform.scale(pygame.image.load("solarSystem.jpg"), (1200, 800))
    gamewindow.blit(spaceBackground, (0, 0))
    pygame.display.set_caption("Space Instructions")
    instructionFont = pygame.font.Font('freesansbold.ttf', 40)
    instruction = instructionFont.render('Space Game Instructions', True, WHITE)
    Instruction = instruction.get_rect()
    Instruction.center = (600, 80)
    gamewindow.blit(instruction, Instruction)

    # Write the instructions
    counter = 0
    text = ['Do you think you know the planets in our solar system? Lets see and find out!',
            '',
            '- There are a set of questions based on the different planets',
            '- Your goal is to answer as many questions as you can in 1 minute',
            '- To answer the questions, click on the correct planet',
            '',
            '- If you answer the question CORRECTLY, you earn a point',
            '- If you answer the question INCORRECTLY, you lose a point',
            '- * Note: Some questions may repeat. *',
            '       - It can be a bonus question if you already answered it correctly!',
            '',
            '* Click the START button to play! *']
    for x in text:
        counter += 1
        fonts = pygame.font.SysFont('constantia', 20).render(x, True, WHITE)
        gamewindow.blit(fonts, (50, 110+(30 * counter)))
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

        # Space Game button
        if 200 + 150 > mouse[0] > 200 and 600 + 50 > mouse[1] > 600:
            pygame.draw.rect(gamewindow, ORANGE, (200, 600, 150, 50))
            if click[0] == 1:
                spaceGame(gamewindow)
        else:
            pygame.draw.rect(gamewindow, YELLOW, (200, 600, 150, 50))

        startFont = pygame.font.Font('freesansbold.ttf', 20)
        start = startFont.render('START GAME', True, BLACK)
        Start = start.get_rect()
        Start.center = ((200 + (150 / 2)), (600 + (50 / 2)))
        gamewindow.blit(start, Start)

        # Main Menu button
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
    # End of while loop
# End of spaceInstructions()

# Answer page function
def spaceAnswers(gamewindow):
    from mainMenu import menu
    YELLOW = (249,248,100)

    # Set Background - Using a picture
    spaceBackground = pygame.transform.scale(pygame.image.load("darkSkyBackground.jpg"), (1200, 800))
    gamewindow.blit(spaceBackground, (0, 0))
    pygame.display.set_caption("Space Answers")

    # Write the space questions and answers
    counter1 = 0
    counter2 = 0
    text1 = ["What is the hottest planet?",
            "   - Venus",
            "Which planet has the most moons?",
            "   - Saturn",
            "What is the farthest planet from the sun?",
            "   - Neptune",
            "What planet has life forms on it?",
            "   - Earth",
            "What planet is closest in size to Earth?",
            "   - Venus",
            "What is the brightest planet in the night sky?",
            "   - Venus",
            "Phobos and Deimos are moons of what planet?",
            "   - Mars",
            "What is the largest planet in the solar system?",
            "   - Jupiter",
            "What is the 6th planet from the sun?",
            "   - Saturn",
            "What is the smallest planet?",
            "   - Mercury",
            "What planet was named after the Roman goddess of love and beauty?",
            "   - Venus",
            "Which planet has oxygen and nitrogen?",
            "   - Earth",
            "Which planet (not including Earth) has mountains, valleys, and canyons?",
            "   - Mars",
            "Which planet orbits on its side?",
            "   - Uranus"]
    text2 = ["Which is the fastest planet to orbit the sun?",
            "   - Mercury",
            "Which planet has liquid water on the surface?",
            "   - Earth",
            "What is the 7th planet from the sun?",
            "   - Uranus",
            "Which planet rotates in the opposite direction from all the other planets?",
            "   - Venus",
            "What is the most explored planet (not including Earth)?",
            "   - Mars",
            "Which planet has the shortest days?",
            "   - Jupiter",
            "Which planet has the largest moon in the solar system?",
            "   - Jupiter",
            "What is the second largest planet in the solar system?",
            "   - Saturn",
            "Which planet has 13 rings?",
            "   - Uranus",
            "What is the coldest planet in the solar system?",
            "   - Neptune",
            "Which planet has rings visible to the naked eye?",
            "   - Saturn",
            "_______ is called the \"Red planet\"",
            "   - Mars",
            "Which planet has a runaway greenhouse effect?",
            "   - Venus"]
    for x1 in text1:
        counter1 += 1
        fonts1 = pygame.font.SysFont('constantia', 17).render(x1, True, WHITE)
        gamewindow.blit(fonts1, (70, 30 + (25 * counter1)))
    # End of for loop

    for x2 in text2:
        counter2 += 1
        fonts2 = pygame.font.SysFont('constantia', 17).render(x2, True, WHITE)
        gamewindow.blit(fonts2, (640, 30 + (25 * counter2)))
    # End of for loop
    pygame.display.update()

    # Create this loop so that user can click on the 'x' button to exit
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # End of for loop

        # Allow player to use their mouse
        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Main Menu button
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

        # Play Again button
        if 0 + 100 > mouse[0] > 0 and 30 + 0 > mouse[1] > 0:
            pygame.draw.rect(gamewindow, WHITE, (0, 0, 100, 30))
            if click[0] == 1:
                spaceGame(gamewindow)
        else:
            pygame.draw.rect(gamewindow, YELLOW, (0, 0, 100, 30))

        againFont = pygame.font.Font('freesansbold.ttf', 14)
        again = againFont.render('Play Again', True, BLACK)
        Again = again.get_rect()
        Again.center = ((0 + (100 / 2)), (0 + (30 / 2)))
        gamewindow.blit(again, Again)
        pygame.display.update()
    # End of while loop
# End of spaceAnswers()

# Function for buttons
def toButtons(gamewindow):
    from mainMenu import menu
    while True:
        pygame.event.get(pygame.MOUSEBUTTONDOWN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Play Again Button
        if 630 + 120 > mouse[0] > 630 and 340 + 40 > mouse[1] > 340:
            pygame.draw.rect(gamewindow, WHITE, (630, 340, 120, 40))
            if click[0] == 1:
                spaceGame(gamewindow)
        else:
            pygame.draw.rect(gamewindow, YELLOW, (630, 340, 120, 40))

        fonts = pygame.font.Font('freesansbold.ttf', 20)
        again = fonts.render('Play Again!', True, BLACK)
        Again = again.get_rect()
        Again.center = ((630 + (120 / 2)), (340 + (40 / 2)))
        gamewindow.blit(again, Again)

        # Answers Button
        if 430 + 120 > mouse[0] > 430 and 340 + 40 > mouse[1] > 340:
            pygame.draw.rect(gamewindow, WHITE, (430, 340, 120, 40))
            if click[0] == 1:
                spaceAnswers(gamewindow)
        else:
            pygame.draw.rect(gamewindow, YELLOW, (430, 340, 120, 40))

        answer = fonts.render('Answers', True, BLACK)
        Answer = answer.get_rect()
        Answer.center = ((430 + (120 / 2)), (340 + (40 / 2)))
        gamewindow.blit(answer, Answer)

        # Main Menu button
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
    # End of while loop
# End of toButtons()
