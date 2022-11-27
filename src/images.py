import pygame

# Function that returns a list of animal images
def animalImageList():
    tigerPic = pygame.transform.scale(pygame.image.load("tiger.jpg"), (360, 260))
    toucanPic = pygame.transform.scale(pygame.image.load(
        "toucan.jpg"), (360, 260))
    cheetahPic = pygame.transform.scale(pygame.image.load(
        "cheetah.jpg"), (360, 260))
    eaglePic = pygame.transform.scale(pygame.image.load("eagle.png"), (360, 260))
    lionPic = pygame.transform.scale(pygame.image.load("lion.jpg"), (360, 260))
    catPic = pygame.transform.scale(pygame.image.load("cat.jpg"), (360, 260))
    kangarooPic = pygame.transform.scale(pygame.image.load(
        "kangaroo.jpg"), (360, 260))
    cowPic = pygame.transform.scale(pygame.image.load("cow.jpg"), (360, 260))
    raccoonPic = pygame.transform.scale(pygame.image.load(
        "raccoon.jpg"), (360, 260))
    meerkatPic = pygame.transform.scale(pygame.image.load(
        "meerkat.jpg"), (360, 260))
    lemurPic = pygame.transform.scale(pygame.image.load("lemur.jpg"), (360, 260))
    pigPic = pygame.transform.scale(pygame.image.load("pig.jpg"), (360, 260))
    armadilloPic = pygame.transform.scale(pygame.image.load(
        "armadillo.jpg"), (360, 260))
    zebraPic = pygame.transform.scale(pygame.image.load("zebra.jpg"), (360, 260))
    antelopePic = pygame.transform.scale(pygame.image.load(
        "antelope.jpg"), (360, 260))
    pandaPic = pygame.transform.scale(pygame.image.load("panda.jpg"), (360, 260))
    giraffePic = pygame.transform.scale(pygame.image.load(
        "giraffe.jpg"), (360, 260))
    owlPic = pygame.transform.scale(pygame.image.load("owl.jpg"), (360, 260))
    butterflyPic = pygame.transform.scale(pygame.image.load(
        "butterfly.jpg"), (360, 260))
    snakePic = pygame.transform.scale(pygame.image.load("snake.jpg"), (360, 260))
    chameleonPic = pygame.transform.scale(pygame.image.load(
        "chameleon.jpg"), (360, 260))
    frogPic = pygame.transform.scale(pygame.image.load("frog.jpg"), (360, 260))
    turtlePic = pygame.transform.scale(pygame.image.load(
        "turtle.jpg"), (360, 260))
    hedgehogPic = pygame.transform.scale(pygame.image.load(
        "hedgehog.png"), (360, 260))
    porcupinePic = pygame.transform.scale(pygame.image.load(
        "porcupine.jpg"), (360, 260))
    squirrelPic = pygame.transform.scale(pygame.image.load(
        "squirrel.jpg"), (360, 260))
    swanPic = pygame.transform.scale(pygame.image.load("swan.jpg"), (360, 260))

    images = [tigerPic, toucanPic, cheetahPic, eaglePic, lionPic, catPic, kangarooPic, cowPic, raccoonPic,
              meerkatPic, lemurPic, pigPic, armadilloPic, zebraPic, antelopePic, pandaPic, giraffePic, owlPic,
              butterflyPic, snakePic, chameleonPic, frogPic, turtlePic, hedgehogPic, porcupinePic, squirrelPic, swanPic]
    return images
# End of animalImageList()

# Function that returns a list of animal image answers
def animalImageAnswers():
    tigerPic = pygame.transform.scale(pygame.image.load(
        "tigerAnswer.jpg"), (410, 290))
    toucanPic = pygame.transform.scale(pygame.image.load(
        "toucanAnswer.jpg"), (360, 260))
    cheetahPic = pygame.transform.scale(pygame.image.load(
        "cheetahAnswer.jpg"), (360, 310))
    eaglePic = pygame.transform.scale(pygame.image.load(
        "eagleAnswer.jpg"), (360, 260))
    lionPic = pygame.transform.scale(pygame.image.load(
        "lionAnswer.jpg"), (360, 300))
    catPic = pygame.transform.scale(pygame.image.load(
        "catAnswer.jpg"), (390, 290))
    kangarooPic = pygame.transform.scale(pygame.image.load(
        "kangarooAnswer.jpg"), (380, 280))
    cowPic = pygame.transform.scale(pygame.image.load(
        "cowAnswer.jpg"), (360, 260))
    raccoonPic = pygame.transform.scale(pygame.image.load(
        "raccoonAnswer.jpg"), (360, 260))
    meerkatPic = pygame.transform.scale(pygame.image.load(
        "meerkatAnswer.jpg"), (360, 260))
    lemurPic = pygame.transform.scale(pygame.image.load(
        "lemurAnswer.jpg"), (380, 260))
    pigPic = pygame.transform.scale(pygame.image.load(
        "pigAnswer.jpg"), (360, 300))
    armadilloPic = pygame.transform.scale(pygame.image.load(
        "armadilloAnswer.jpg"), (370, 260))
    zebraPic = pygame.transform.scale(pygame.image.load(
        "zebraAnswer.jpg"), (360, 260))
    antelopePic = pygame.transform.scale(pygame.image.load(
        "antelopeAnswer.jpg"), (430, 250))
    pandaPic = pygame.transform.scale(pygame.image.load(
        "pandaAnswer.jpg"), (360, 260))
    giraffePic = pygame.transform.scale(pygame.image.load(
        "giraffeAnswer.jpg"), (360, 280))
    owlPic = pygame.transform.scale(pygame.image.load(
        "owlAnswer.jpg"), (360, 260))
    butterflyPic = pygame.transform.scale(pygame.image.load(
        "butterflyAnswer.jpg"), (360, 260))
    snakePic = pygame.transform.scale(pygame.image.load(
        "snakeAnswer.jpg"), (380, 280))
    chameleonPic = pygame.transform.scale(pygame.image.load(
        "chameleonAnswer.jpg"), (420, 260))
    frogPic = pygame.transform.scale(pygame.image.load(
        "frogAnswer.jpg"), (360, 260))
    turtlePic = pygame.transform.scale(pygame.image.load(
        "turtleAnswer.png"), (420, 290))
    hedgehogPic = pygame.transform.scale(pygame.image.load(
        "hedgehogAnswer.jpg"), (380, 280))
    porcupinePic = pygame.transform.scale(pygame.image.load(
        "porcupineAnswer.jpg"), (360, 260))
    squirrelPic = pygame.transform.scale(pygame.image.load(
        "squirrelAnswer.jpg"), (360, 260))
    swanPic = pygame.transform.scale(pygame.image.load(
        "swanAnswer.jpg"), (360, 260))

    images = [tigerPic, toucanPic, cheetahPic, eaglePic, lionPic, catPic, kangarooPic, cowPic, raccoonPic,
            meerkatPic, lemurPic, pigPic, armadilloPic, zebraPic, antelopePic, pandaPic, giraffePic, owlPic,
            butterflyPic, snakePic, chameleonPic, frogPic, turtlePic, hedgehogPic, porcupinePic, squirrelPic, swanPic]
    return images
# End of animalImageAnswers()

# Function that returns a list of disney images
def disneyImageList():
    stitch = pygame.transform.scale(pygame.image.load("stitch.png"), (360, 260))
    cinderella = pygame.transform.scale(pygame.image.load(
        "cinderella.jpg"), (360, 260))
    ariel = pygame.transform.scale(pygame.image.load("ariel.png"), (380, 280))
    beast = pygame.transform.scale(pygame.image.load("beast.jpg"), (310, 290))
    genie = pygame.transform.scale(pygame.image.load("genie.jpg"), (360, 260))
    abu = pygame.transform.scale(pygame.image.load("abu.jpg"), (360, 260))
    anna = pygame.transform.scale(pygame.image.load("anna.jpeg"), (360, 270))
    elsa = pygame.transform.scale(pygame.image.load("elsa.jpg"), (360, 260))
    bambi = pygame.transform.scale(pygame.image.load("bambi.png"), (380, 280))
    pinocchio = pygame.transform.scale(pygame.image.load(
        "pinocchio.jpg"), (360, 260))
    peterPan = pygame.transform.scale(pygame.image.load(
        "peterPan.jpg"), (360, 260))
    captainHook = pygame.transform.scale(pygame.image.load(
        "captainHook.png"), (360, 260))
    dumbo = pygame.transform.scale(pygame.image.load("dumbo.jpg"), (360, 260))
    cheshire = pygame.transform.scale(pygame.image.load(
        "cheshireCat.jpg"), (360, 260))
    mulan = pygame.transform.scale(pygame.image.load("mulan.jpg"), (360, 260))
    belle = pygame.transform.scale(pygame.image.load("belle.jpg"), (360, 260))
    tarzan = pygame.transform.scale(pygame.image.load("tarzan.jpg"), (360, 280))
    mickey = pygame.transform.scale(pygame.image.load(
        "mickeyMouse.jpg"), (360, 260))
    goofy = pygame.transform.scale(pygame.image.load("goofy.jpg"), (370, 270))
    pluto = pygame.transform.scale(pygame.image.load("pluto.png"), (360, 260))
    rapunzel = pygame.transform.scale(pygame.image.load(
        "rapunzel.png"), (360, 260))
    gus = pygame.transform.scale(pygame.image.load("gus.jpg"), (270, 320))
    hades = pygame.transform.scale(pygame.image.load("hades.jpg"), (410, 270))
    nemo = pygame.transform.scale(pygame.image.load("nemo.png"), (360, 280))
    baymax = pygame.transform.scale(pygame.image.load("baymax.png"), (320, 320))
    jafar = pygame.transform.scale(pygame.image.load("jafar.png"), (360, 260))
    lady = pygame.transform.scale(pygame.image.load("lady.jpg"), (360, 260))
    ladyTremaine = pygame.transform.scale(pygame.image.load(
        "ladyTremaine.jpg"), (360, 260))
    lumiere = pygame.transform.scale(pygame.image.load("lumiere.jpg"), (330, 300))
    carpet = pygame.transform.scale(pygame.image.load(
        "magicCarpet.png"), (360, 260))
    maleficent = pygame.transform.scale(pygame.image.load(
        "maleficent.jpg"), (370, 270))
    maryPoppins = pygame.transform.scale(pygame.image.load(
        "marryPoppins.png"), (360, 260))
    moana = pygame.transform.scale(pygame.image.load("moana.jpg"), (360, 260))
    mushu = pygame.transform.scale(pygame.image.load("mushu.jpg"), (360, 260))
    olaf = pygame.transform.scale(pygame.image.load("olaf.jfif"), (380, 280))
    pumbaa = pygame.transform.scale(pygame.image.load("pumbaa.jpg"), (360, 260))
    timon = pygame.transform.scale(pygame.image.load("timon.png"), (300, 320))
    winnie = pygame.transform.scale(pygame.image.load("winnie.png"), (360, 260))
    rafiki = pygame.transform.scale(pygame.image.load("rafiki.jpg"), (360, 260))
    sebastian = pygame.transform.scale(pygame.image.load(
        "sebastian.jpeg"), (360, 260))
    flounder = pygame.transform.scale(pygame.image.load(
        "flounder.jpg"), (380, 280))
    sven = pygame.transform.scale(pygame.image.load("sven.jpg"), (380, 280))
    tigger = pygame.transform.scale(pygame.image.load("tigger.jpg"), (360, 260))
    tinkerBell = pygame.transform.scale(pygame.image.load(
        "tinkerbell.jpeg"), (360, 260))
    tramp = pygame.transform.scale(pygame.image.load("tramp.jpg"), (360, 260))
    ursula = pygame.transform.scale(pygame.image.load("ursula.jpg"), (380, 280))
    wreck = pygame.transform.scale(pygame.image.load(
        "wreckitRalph.jpg"), (360, 260))
    buzz = pygame.transform.scale(pygame.image.load("buzz.jfif"), (360, 260))
    woody = pygame.transform.scale(pygame.image.load("woody.jpg"), (360, 260))
    aladdin = pygame.transform.scale(pygame.image.load("aladdin.jpg"), (360, 260))
    dory = pygame.transform.scale(pygame.image.load("dori.jpg"), (380, 260))
    walle = pygame.transform.scale(pygame.image.load("walle.jpg"), (360, 260))
    mike = pygame.transform.scale(pygame.image.load("mike.png"), (360, 280))
    yoda = pygame.transform.scale(pygame.image.load("yoda.jpg"), (360, 260))
    joy = pygame.transform.scale(pygame.image.load("joy.png"), (380, 280))
    sadness = pygame.transform.scale(pygame.image.load("sadness.jpg"), (360, 260))
    minnie = pygame.transform.scale(pygame.image.load("minnie.jpg"), (360, 260))
    merida = pygame.transform.scale(pygame.image.load("merida.jpg"), (360, 260))
    maui = pygame.transform.scale(pygame.image.load("maui.jpg"), (320, 310))
    mcqueen = pygame.transform.scale(pygame.image.load("mcqueen.jpg"), (360, 260))
    mater = pygame.transform.scale(pygame.image.load("mater.jpg"), (360, 260))
    chewbacca = pygame.transform.scale(pygame.image.load(
        "chewbacca.jpg"), (360, 260))
    chip = pygame.transform.scale(pygame.image.load("chip.jpg"), (360, 260))
    forky = pygame.transform.scale(pygame.image.load("forky.jpg"), (380, 280))
    hercules = pygame.transform.scale(pygame.image.load(
        "hercules.png"), (380, 260))

    images = [stitch, cinderella, ariel, beast, genie, abu, anna, elsa, bambi, pinocchio, peterPan, captainHook, dumbo,
              cheshire, mulan, belle, tarzan, mickey, goofy, pluto, rapunzel, gus, hades, nemo, baymax, jafar, lady,
              ladyTremaine, lumiere, carpet, maleficent, maryPoppins, moana, mushu, olaf, pumbaa, timon, winnie, rafiki,
              sebastian, flounder, sven, tigger, tinkerBell, tramp, ursula, wreck, buzz, woody, aladdin, dory, walle,
              mike, yoda, joy, sadness, minnie, merida, maui, mcqueen, mater, chewbacca, chip, forky, hercules]
    return images
# End of disneyImageList

# Function that returns a list of disney image answers
def disneyImageAnswers():
    stitch = pygame.transform.scale(pygame.image.load(
        "stitchAnswer.png"), (300, 350))
    cinderella = pygame.transform.scale(pygame.image.load(
        "cinderellaAnswer.jpg"), (460, 280))
    ariel = pygame.transform.scale(pygame.image.load(
        "arielAnswer.jpg"), (290, 330))
    beast = pygame.transform.scale(pygame.image.load(
        "beastAnswer.png"), (410, 320))
    genie = pygame.transform.scale(pygame.image.load(
        "genieAnswer.jpg"), (380, 280))
    abu = pygame.transform.scale(pygame.image.load("abuAnswer.jpg"), (470, 280))
    anna = pygame.transform.scale(pygame.image.load("annaAnswer.jpg"), (320, 340))
    elsa = pygame.transform.scale(pygame.image.load("elsaAnswer.jpg"), (350, 330))
    bambi = pygame.transform.scale(pygame.image.load(
        "bambiAnswer.jpg"), (390, 290))
    pinocchio = pygame.transform.scale(pygame.image.load(
        "pinocchioAnswer.png"), (350, 310))
    peterPan = pygame.transform.scale(pygame.image.load(
        "peterPanAnswer.jfif"), (420, 290))
    captainHook = pygame.transform.scale(pygame.image.load(
        "captainHookAnswer.jpg"), (380, 280))
    dumbo = pygame.transform.scale(pygame.image.load(
        "dumboAnswer.jpg"), (340, 340))
    cheshire = pygame.transform.scale(pygame.image.load(
        "cheshireCatAnswer.jpg"), (380, 280))
    mulan = pygame.transform.scale(pygame.image.load(
        "mulanAnswer.jpg"), (390, 310))
    belle = pygame.transform.scale(pygame.image.load(
        "belleAnswer.png"), (300, 350))
    tarzan = pygame.transform.scale(pygame.image.load(
        "tarzanAnswer.jpg"), (370, 300))
    mickey = pygame.transform.scale(pygame.image.load(
        "mickeyMouseAnswer.jfif"), (500, 310))
    goofy = pygame.transform.scale(pygame.image.load(
        "goofyAnswer.png"), (340, 310))
    pluto = pygame.transform.scale(pygame.image.load(
        "plutoAnswer.jpg"), (390, 280))
    rapunzel = pygame.transform.scale(pygame.image.load(
        "rapunzelAnswer.jpg"), (390, 320))
    gus = pygame.transform.scale(pygame.image.load("gusAnswer.jpg"), (300, 330))
    hades = pygame.transform.scale(pygame.image.load(
        "hadesAnswer.jpg"), (400, 280))
    nemo = pygame.transform.scale(pygame.image.load("nemoAnswer.png"), (390, 290))
    baymax = pygame.transform.scale(pygame.image.load(
        "baymaxAnswer.jpg"), (330, 330))
    jafar = pygame.transform.scale(pygame.image.load(
        "jafarAnswer.jpg"), (440, 280))
    lady = pygame.transform.scale(pygame.image.load("ladyAnswer.jpg"), (350, 290))
    ladyTremaine = pygame.transform.scale(pygame.image.load(
        "ladyTremaineAnswer.jpg"), (410, 290))
    lumiere = pygame.transform.scale(pygame.image.load(
        "lumiereAnswer.jpg"), (460, 260))
    carpet = pygame.transform.scale(pygame.image.load(
        "magicCarpetAnswer.jpg"), (360, 300))
    maleficent = pygame.transform.scale(pygame.image.load(
        "maleficentAnswer.jpg"), (370, 320))
    maryPoppins = pygame.transform.scale(pygame.image.load(
        "marryPoppinsAnswer.jpg"), (380, 280))
    moana = pygame.transform.scale(pygame.image.load(
        "moanaAnswer.jpg"), (320, 330))
    mushu = pygame.transform.scale(pygame.image.load(
        "mushuAnswer.png"), (380, 280))
    olaf = pygame.transform.scale(pygame.image.load("olafAnswer.jpg"), (380, 280))
    pumbaa = pygame.transform.scale(pygame.image.load(
        "pumbaaAnswer.jpg"), (360, 350))
    timon = pygame.transform.scale(pygame.image.load(
        "timonAnswer.jpg"), (260, 330))
    winnie = pygame.transform.scale(pygame.image.load(
        "winnieAnswer.jpg"), (380, 280))
    rafiki = pygame.transform.scale(pygame.image.load(
        "rafikiAnswer.jpg"), (380, 280))
    sebastian = pygame.transform.scale(pygame.image.load(
        "sebastianAnswer.png"), (380, 280))
    flounder = pygame.transform.scale(pygame.image.load(
        "flounderAnswer.jpg"), (370, 290))
    sven = pygame.transform.scale(pygame.image.load("svenAnswer.jpg"), (390, 290))
    tigger = pygame.transform.scale(pygame.image.load(
        "tiggerAnswer.jpg"), (380, 280))
    tinkerBell = pygame.transform.scale(pygame.image.load(
        "tinkerbellAnswer.png"), (380, 350))
    tramp = pygame.transform.scale(pygame.image.load(
        "trampAnswer.png"), (320, 340))
    ursula = pygame.transform.scale(pygame.image.load(
        "ursulaAnswer.png"), (380, 280))
    wreck = pygame.transform.scale(pygame.image.load(
        "wreckitRalphAnswer.png"), (360, 280))
    buzz = pygame.transform.scale(pygame.image.load("buzzAnswer.jpg"), (390, 330))
    woody = pygame.transform.scale(pygame.image.load(
        "woodyAnswer.jpg"), (380, 280))
    aladdin = pygame.transform.scale(pygame.image.load(
        "aladdinAnswer.jpg"), (350, 310))
    dory = pygame.transform.scale(pygame.image.load("doriAnswer.jpg"), (420, 290))
    walle = pygame.transform.scale(pygame.image.load(
        "walleAnswer.jpg"), (380, 280))
    mike = pygame.transform.scale(pygame.image.load("mikeAnswer.jpg"), (370, 270))
    yoda = pygame.transform.scale(pygame.image.load("yodaAnswer.jpg"), (340, 350))
    joy = pygame.transform.scale(pygame.image.load("joyAnswer.jpg"), (390, 290))
    sadness = pygame.transform.scale(pygame.image.load(
        "sadnessAnswer.jpg"), (380, 290))
    minnie = pygame.transform.scale(pygame.image.load(
        "minnieAnswer.jpg"), (360, 290))
    merida = pygame.transform.scale(pygame.image.load(
        "meridaAnswer.jfif"), (360, 290))
    maui = pygame.transform.scale(pygame.image.load("mauiAnswer.jpg"), (300, 320))
    mcqueen = pygame.transform.scale(pygame.image.load(
        "mcqueenAnswer.jpg"), (430, 290))
    mater = pygame.transform.scale(pygame.image.load(
        "materAnswer.jpg"), (400, 300))
    chewbacca = pygame.transform.scale(pygame.image.load(
        "chewbaccaAnswer.jpg"), (430, 280))
    chip = pygame.transform.scale(pygame.image.load("chipAnswer.jpg"), (390, 290))
    forky = pygame.transform.scale(pygame.image.load(
        "forkyAnswer.jpg"), (390, 300))
    hercules = pygame.transform.scale(pygame.image.load(
        "herculesAnswer.png"), (330, 350))

    images = [stitch, cinderella, ariel, beast, genie, abu, anna, elsa, bambi, pinocchio, peterPan, captainHook, dumbo,
              cheshire, mulan, belle, tarzan, mickey, goofy, pluto, rapunzel, gus, hades, nemo, baymax, jafar, lady,
              ladyTremaine, lumiere, carpet, maleficent, maryPoppins, moana, mushu, olaf, pumbaa, timon, winnie, rafiki,
              sebastian, flounder, sven, tigger, tinkerBell, tramp, ursula, wreck, buzz, woody, aladdin, dory, walle,
              mike, yoda, joy, sadness, minnie, merida, maui, mcqueen, mater, chewbacca, chip, forky, hercules]
    return images
# End of disneyImageAnswers()

# Function that returns a list of Character/Player images
def flappyImages():
    bird = pygame.transform.scale(pygame.image.load("b1.png"), (80, 80))
    angryBird = pygame.transform.scale(pygame.image.load(
        "angryBird.png"), (60, 60))
    whale = pygame.transform.scale(pygame.image.load("whale.png"), (120, 80))
    snake = pygame.transform.scale(pygame.image.load(
        "flappySnake.png"), (80, 80))
    flappyBird = pygame.transform.scale(pygame.image.load(
        "flappyBird.png"), (120, 60))
    sheep = pygame.transform.scale(pygame.image.load("sheep.png"), (100, 70))
    seal = pygame.transform.scale(pygame.image.load("seal.png"), (70, 70))
    hedgehog = pygame.transform.scale(pygame.image.load(
        "flappyHedgehog.png"), (120, 100))
    parrot = pygame.transform.scale(pygame.image.load("parrot.png"), (80, 80))
    hen = pygame.transform.scale(pygame.image.load("flappyHen.png"), (90, 90))
    fly = pygame.transform.scale(pygame.image.load("flappyFly.png"), (90, 90))
    star = pygame.transform.scale(pygame.image.load("star.png"), (100, 100))
    pinkBird = pygame.transform.scale(pygame.image.load(
        "pinkBird.png"), (100, 100))
    bee = pygame.transform.scale(pygame.image.load("bee.jpg"), (100, 100))
    cat = pygame.transform.scale(pygame.image.load("flappyCat.png"), (100, 100))
    penguin = pygame.transform.scale(pygame.image.load(
        "flappyPing.jpg"), (100, 100))
    pig = pygame.transform.scale(pygame.image.load("flyingPig.png"), (100, 100))

    images = [bird, angryBird, whale, snake, flappyBird, sheep, seal, hedgehog, parrot, hen, fly, star,
              pinkBird, bee, cat, penguin, pig]
    return images
# End of flappyImages()
