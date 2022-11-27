import pygame

# Function that returns a list of animal images
def animalImageList():
    tigerPic = pygame.transform.scale(pygame.image.load("images/tiger.jpg"), (360, 260))
    toucanPic = pygame.transform.scale(pygame.image.load(
        "images/toucan.jpg"), (360, 260))
    cheetahPic = pygame.transform.scale(pygame.image.load(
        "images/cheetah.jpg"), (360, 260))
    eaglePic = pygame.transform.scale(pygame.image.load("images/eagle.png"), (360, 260))
    lionPic = pygame.transform.scale(pygame.image.load("images/lion.jpg"), (360, 260))
    catPic = pygame.transform.scale(pygame.image.load("images/cat.jpg"), (360, 260))
    kangarooPic = pygame.transform.scale(pygame.image.load(
        "images/kangaroo.jpg"), (360, 260))
    cowPic = pygame.transform.scale(pygame.image.load("images/cow.jpg"), (360, 260))
    raccoonPic = pygame.transform.scale(pygame.image.load(
        "images/raccoon.jpg"), (360, 260))
    meerkatPic = pygame.transform.scale(pygame.image.load(
        "images/meerkat.jpg"), (360, 260))
    lemurPic = pygame.transform.scale(pygame.image.load("images/lemur.jpg"), (360, 260))
    pigPic = pygame.transform.scale(pygame.image.load("images/pig.jpg"), (360, 260))
    armadilloPic = pygame.transform.scale(pygame.image.load(
        "images/armadillo.jpg"), (360, 260))
    zebraPic = pygame.transform.scale(pygame.image.load("images/zebra.jpg"), (360, 260))
    antelopePic = pygame.transform.scale(pygame.image.load(
        "images/antelope.jpg"), (360, 260))
    pandaPic = pygame.transform.scale(pygame.image.load("images/panda.jpg"), (360, 260))
    giraffePic = pygame.transform.scale(pygame.image.load(
        "images/giraffe.jpg"), (360, 260))
    owlPic = pygame.transform.scale(pygame.image.load("images/owl.jpg"), (360, 260))
    butterflyPic = pygame.transform.scale(pygame.image.load(
        "images/butterfly.jpg"), (360, 260))
    snakePic = pygame.transform.scale(pygame.image.load("images/snake.jpg"), (360, 260))
    chameleonPic = pygame.transform.scale(pygame.image.load(
        "images/chameleon.jpg"), (360, 260))
    frogPic = pygame.transform.scale(pygame.image.load("images/frog.jpg"), (360, 260))
    turtlePic = pygame.transform.scale(pygame.image.load(
        "images/turtle.jpg"), (360, 260))
    hedgehogPic = pygame.transform.scale(pygame.image.load(
        "images/hedgehog.png"), (360, 260))
    porcupinePic = pygame.transform.scale(pygame.image.load(
        "images/porcupine.jpg"), (360, 260))
    squirrelPic = pygame.transform.scale(pygame.image.load(
        "images/squirrel.jpg"), (360, 260))
    swanPic = pygame.transform.scale(pygame.image.load("images/swan.jpg"), (360, 260))

    images = [tigerPic, toucanPic, cheetahPic, eaglePic, lionPic, catPic, kangarooPic, cowPic, raccoonPic,
              meerkatPic, lemurPic, pigPic, armadilloPic, zebraPic, antelopePic, pandaPic, giraffePic, owlPic,
              butterflyPic, snakePic, chameleonPic, frogPic, turtlePic, hedgehogPic, porcupinePic, squirrelPic, swanPic]
    return images
# End of animalImageList()

# Function that returns a list of animal image answers
def animalImageAnswers():
    tigerPic = pygame.transform.scale(pygame.image.load(
        "images/tigerAnswer.jpg"), (410, 290))
    toucanPic = pygame.transform.scale(pygame.image.load(
        "images/toucanAnswer.jpg"), (360, 260))
    cheetahPic = pygame.transform.scale(pygame.image.load(
        "images/cheetahAnswer.jpg"), (360, 310))
    eaglePic = pygame.transform.scale(pygame.image.load(
        "images/eagleAnswer.jpg"), (360, 260))
    lionPic = pygame.transform.scale(pygame.image.load(
        "images/lionAnswer.jpg"), (360, 300))
    catPic = pygame.transform.scale(pygame.image.load(
        "images/catAnswer.jpg"), (390, 290))
    kangarooPic = pygame.transform.scale(pygame.image.load(
        "images/kangarooAnswer.jpg"), (380, 280))
    cowPic = pygame.transform.scale(pygame.image.load(
        "images/cowAnswer.jpg"), (360, 260))
    raccoonPic = pygame.transform.scale(pygame.image.load(
        "images/raccoonAnswer.jpg"), (360, 260))
    meerkatPic = pygame.transform.scale(pygame.image.load(
        "images/meerkatAnswer.jpg"), (360, 260))
    lemurPic = pygame.transform.scale(pygame.image.load(
        "images/lemurAnswer.jpg"), (380, 260))
    pigPic = pygame.transform.scale(pygame.image.load(
        "images/pigAnswer.jpg"), (360, 300))
    armadilloPic = pygame.transform.scale(pygame.image.load(
        "images/armadilloAnswer.jpg"), (370, 260))
    zebraPic = pygame.transform.scale(pygame.image.load(
        "images/zebraAnswer.jpg"), (360, 260))
    antelopePic = pygame.transform.scale(pygame.image.load(
        "images/antelopeAnswer.jpg"), (430, 250))
    pandaPic = pygame.transform.scale(pygame.image.load(
        "images/pandaAnswer.jpg"), (360, 260))
    giraffePic = pygame.transform.scale(pygame.image.load(
        "images/giraffeAnswer.jpg"), (360, 280))
    owlPic = pygame.transform.scale(pygame.image.load(
        "images/owlAnswer.jpg"), (360, 260))
    butterflyPic = pygame.transform.scale(pygame.image.load(
        "images/butterflyAnswer.jpg"), (360, 260))
    snakePic = pygame.transform.scale(pygame.image.load(
        "images/snakeAnswer.jpg"), (380, 280))
    chameleonPic = pygame.transform.scale(pygame.image.load(
        "images/chameleonAnswer.jpg"), (420, 260))
    frogPic = pygame.transform.scale(pygame.image.load(
        "images/frogAnswer.jpg"), (360, 260))
    turtlePic = pygame.transform.scale(pygame.image.load(
        "images/turtleAnswer.png"), (420, 290))
    hedgehogPic = pygame.transform.scale(pygame.image.load(
        "images/hedgehogAnswer.jpg"), (380, 280))
    porcupinePic = pygame.transform.scale(pygame.image.load(
        "images/porcupineAnswer.jpg"), (360, 260))
    squirrelPic = pygame.transform.scale(pygame.image.load(
        "images/squirrelAnswer.jpg"), (360, 260))
    swanPic = pygame.transform.scale(pygame.image.load(
        "images/swanAnswer.jpg"), (360, 260))

    images = [tigerPic, toucanPic, cheetahPic, eaglePic, lionPic, catPic, kangarooPic, cowPic, raccoonPic,
            meerkatPic, lemurPic, pigPic, armadilloPic, zebraPic, antelopePic, pandaPic, giraffePic, owlPic,
            butterflyPic, snakePic, chameleonPic, frogPic, turtlePic, hedgehogPic, porcupinePic, squirrelPic, swanPic]
    return images
# End of animalImageAnswers()

# Function that returns a list of disney images
def disneyImageList():
    stitch = pygame.transform.scale(pygame.image.load("images/stitch.png"), (360, 260))
    cinderella = pygame.transform.scale(pygame.image.load(
        "images/cinderella.jpg"), (360, 260))
    ariel = pygame.transform.scale(pygame.image.load("images/ariel.png"), (380, 280))
    beast = pygame.transform.scale(pygame.image.load("images/beast.jpg"), (310, 290))
    genie = pygame.transform.scale(pygame.image.load("images/genie.jpg"), (360, 260))
    abu = pygame.transform.scale(pygame.image.load("images/abu.jpg"), (360, 260))
    anna = pygame.transform.scale(pygame.image.load("images/anna.jpeg"), (360, 270))
    elsa = pygame.transform.scale(pygame.image.load("images/elsa.jpg"), (360, 260))
    bambi = pygame.transform.scale(pygame.image.load("images/bambi.png"), (380, 280))
    pinocchio = pygame.transform.scale(pygame.image.load(
        "images/pinocchio.jpg"), (360, 260))
    peterPan = pygame.transform.scale(pygame.image.load(
        "images/peterPan.jpg"), (360, 260))
    captainHook = pygame.transform.scale(pygame.image.load(
        "images/captainHook.png"), (360, 260))
    dumbo = pygame.transform.scale(pygame.image.load("images/dumbo.jpg"), (360, 260))
    cheshire = pygame.transform.scale(pygame.image.load(
        "images/cheshireCat.jpg"), (360, 260))
    mulan = pygame.transform.scale(pygame.image.load("images/mulan.jpg"), (360, 260))
    belle = pygame.transform.scale(pygame.image.load("images/belle.jpg"), (360, 260))
    tarzan = pygame.transform.scale(pygame.image.load("images/tarzan.jpg"), (360, 280))
    mickey = pygame.transform.scale(pygame.image.load(
        "images/mickeyMouse.jpg"), (360, 260))
    goofy = pygame.transform.scale(pygame.image.load("images/goofy.jpg"), (370, 270))
    pluto = pygame.transform.scale(pygame.image.load("images/pluto.png"), (360, 260))
    rapunzel = pygame.transform.scale(pygame.image.load(
        "images/rapunzel.png"), (360, 260))
    gus = pygame.transform.scale(pygame.image.load("images/gus.jpg"), (270, 320))
    hades = pygame.transform.scale(pygame.image.load("images/hades.jpg"), (410, 270))
    nemo = pygame.transform.scale(pygame.image.load("images/nemo.png"), (360, 280))
    baymax = pygame.transform.scale(pygame.image.load("images/baymax.png"), (320, 320))
    jafar = pygame.transform.scale(pygame.image.load("images/jafar.png"), (360, 260))
    lady = pygame.transform.scale(pygame.image.load("images/lady.jpg"), (360, 260))
    ladyTremaine = pygame.transform.scale(pygame.image.load(
        "images/ladyTremaine.jpg"), (360, 260))
    lumiere = pygame.transform.scale(pygame.image.load("images/lumiere.jpg"), (330, 300))
    carpet = pygame.transform.scale(pygame.image.load(
        "images/magicCarpet.png"), (360, 260))
    maleficent = pygame.transform.scale(pygame.image.load(
        "images/maleficent.jpg"), (370, 270))
    maryPoppins = pygame.transform.scale(pygame.image.load(
        "images/marryPoppins.png"), (360, 260))
    moana = pygame.transform.scale(pygame.image.load("images/moana.jpg"), (360, 260))
    mushu = pygame.transform.scale(pygame.image.load("images/mushu.jpg"), (360, 260))
    olaf = pygame.transform.scale(pygame.image.load("images/olaf.jfif"), (380, 280))
    pumbaa = pygame.transform.scale(pygame.image.load("images/pumbaa.jpg"), (360, 260))
    timon = pygame.transform.scale(pygame.image.load("images/timon.png"), (300, 320))
    winnie = pygame.transform.scale(pygame.image.load("images/winnie.png"), (360, 260))
    rafiki = pygame.transform.scale(pygame.image.load("images/rafiki.jpg"), (360, 260))
    sebastian = pygame.transform.scale(pygame.image.load(
        "images/sebastian.jpeg"), (360, 260))
    flounder = pygame.transform.scale(pygame.image.load(
        "images/flounder.jpg"), (380, 280))
    sven = pygame.transform.scale(pygame.image.load("images/sven.jpg"), (380, 280))
    tigger = pygame.transform.scale(pygame.image.load("images/tigger.jpg"), (360, 260))
    tinkerBell = pygame.transform.scale(pygame.image.load(
        "images/tinkerbell.jpeg"), (360, 260))
    tramp = pygame.transform.scale(pygame.image.load("images/tramp.jpg"), (360, 260))
    ursula = pygame.transform.scale(pygame.image.load("images/ursula.jpg"), (380, 280))
    wreck = pygame.transform.scale(pygame.image.load(
        "images/wreckitRalph.jpg"), (360, 260))
    buzz = pygame.transform.scale(pygame.image.load("images/buzz.jfif"), (360, 260))
    woody = pygame.transform.scale(pygame.image.load("images/woody.jpg"), (360, 260))
    aladdin = pygame.transform.scale(pygame.image.load("images/aladdin.jpg"), (360, 260))
    dory = pygame.transform.scale(pygame.image.load("images/dori.jpg"), (380, 260))
    walle = pygame.transform.scale(pygame.image.load("images/walle.jpg"), (360, 260))
    mike = pygame.transform.scale(pygame.image.load("images/mike.png"), (360, 280))
    yoda = pygame.transform.scale(pygame.image.load("images/yoda.jpg"), (360, 260))
    joy = pygame.transform.scale(pygame.image.load("images/joy.png"), (380, 280))
    sadness = pygame.transform.scale(pygame.image.load("images/sadness.jpg"), (360, 260))
    minnie = pygame.transform.scale(pygame.image.load("images/minnie.jpg"), (360, 260))
    merida = pygame.transform.scale(pygame.image.load("images/merida.jpg"), (360, 260))
    maui = pygame.transform.scale(pygame.image.load("images/maui.jpg"), (320, 310))
    mcqueen = pygame.transform.scale(pygame.image.load("images/mcqueen.jpg"), (360, 260))
    mater = pygame.transform.scale(pygame.image.load("images/mater.jpg"), (360, 260))
    chewbacca = pygame.transform.scale(pygame.image.load(
        "images/chewbacca.jpg"), (360, 260))
    chip = pygame.transform.scale(pygame.image.load("images/chip.jpg"), (360, 260))
    forky = pygame.transform.scale(pygame.image.load("images/forky.jpg"), (380, 280))
    hercules = pygame.transform.scale(pygame.image.load(
        "images/hercules.png"), (380, 260))

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
        "images/stitchAnswer.png"), (300, 350))
    cinderella = pygame.transform.scale(pygame.image.load(
        "images/cinderellaAnswer.jpg"), (460, 280))
    ariel = pygame.transform.scale(pygame.image.load(
        "images/arielAnswer.jpg"), (290, 330))
    beast = pygame.transform.scale(pygame.image.load(
        "images/beastAnswer.png"), (410, 320))
    genie = pygame.transform.scale(pygame.image.load(
        "images/genieAnswer.jpg"), (380, 280))
    abu = pygame.transform.scale(pygame.image.load("images/abuAnswer.jpg"), (470, 280))
    anna = pygame.transform.scale(pygame.image.load("images/annaAnswer.jpg"), (320, 340))
    elsa = pygame.transform.scale(pygame.image.load("images/elsaAnswer.jpg"), (350, 330))
    bambi = pygame.transform.scale(pygame.image.load(
        "images/bambiAnswer.jpg"), (390, 290))
    pinocchio = pygame.transform.scale(pygame.image.load(
        "images/pinocchioAnswer.png"), (350, 310))
    peterPan = pygame.transform.scale(pygame.image.load(
        "images/peterPanAnswer.jfif"), (420, 290))
    captainHook = pygame.transform.scale(pygame.image.load(
        "images/captainHookAnswer.jpg"), (380, 280))
    dumbo = pygame.transform.scale(pygame.image.load(
        "images/dumboAnswer.jpg"), (340, 340))
    cheshire = pygame.transform.scale(pygame.image.load(
        "images/cheshireCatAnswer.jpg"), (380, 280))
    mulan = pygame.transform.scale(pygame.image.load(
        "images/mulanAnswer.jpg"), (390, 310))
    belle = pygame.transform.scale(pygame.image.load(
        "images/belleAnswer.png"), (300, 350))
    tarzan = pygame.transform.scale(pygame.image.load(
        "images/tarzanAnswer.jpg"), (370, 300))
    mickey = pygame.transform.scale(pygame.image.load(
        "images/mickeyMouseAnswer.jfif"), (500, 310))
    goofy = pygame.transform.scale(pygame.image.load(
        "images/goofyAnswer.png"), (340, 310))
    pluto = pygame.transform.scale(pygame.image.load(
        "images/plutoAnswer.jpg"), (390, 280))
    rapunzel = pygame.transform.scale(pygame.image.load(
        "images/rapunzelAnswer.jpg"), (390, 320))
    gus = pygame.transform.scale(pygame.image.load("images/gusAnswer.jpg"), (300, 330))
    hades = pygame.transform.scale(pygame.image.load(
        "images/hadesAnswer.jpg"), (400, 280))
    nemo = pygame.transform.scale(pygame.image.load("images/nemoAnswer.png"), (390, 290))
    baymax = pygame.transform.scale(pygame.image.load(
        "images/baymaxAnswer.jpg"), (330, 330))
    jafar = pygame.transform.scale(pygame.image.load(
        "images/jafarAnswer.jpg"), (440, 280))
    lady = pygame.transform.scale(pygame.image.load("images/ladyAnswer.jpg"), (350, 290))
    ladyTremaine = pygame.transform.scale(pygame.image.load(
        "images/ladyTremaineAnswer.jpg"), (410, 290))
    lumiere = pygame.transform.scale(pygame.image.load(
        "images/lumiereAnswer.jpg"), (460, 260))
    carpet = pygame.transform.scale(pygame.image.load(
        "images/magicCarpetAnswer.jpg"), (360, 300))
    maleficent = pygame.transform.scale(pygame.image.load(
        "images/maleficentAnswer.jpg"), (370, 320))
    maryPoppins = pygame.transform.scale(pygame.image.load(
        "images/marryPoppinsAnswer.jpg"), (380, 280))
    moana = pygame.transform.scale(pygame.image.load(
        "images/moanaAnswer.jpg"), (320, 330))
    mushu = pygame.transform.scale(pygame.image.load(
        "images/mushuAnswer.png"), (380, 280))
    olaf = pygame.transform.scale(pygame.image.load("images/olafAnswer.jpg"), (380, 280))
    pumbaa = pygame.transform.scale(pygame.image.load(
        "images/pumbaaAnswer.jpg"), (360, 350))
    timon = pygame.transform.scale(pygame.image.load(
        "images/timonAnswer.jpg"), (260, 330))
    winnie = pygame.transform.scale(pygame.image.load(
        "images/winnieAnswer.jpg"), (380, 280))
    rafiki = pygame.transform.scale(pygame.image.load(
        "images/rafikiAnswer.jpg"), (380, 280))
    sebastian = pygame.transform.scale(pygame.image.load(
        "images/sebastianAnswer.png"), (380, 280))
    flounder = pygame.transform.scale(pygame.image.load(
        "images/flounderAnswer.jpg"), (370, 290))
    sven = pygame.transform.scale(pygame.image.load("images/svenAnswer.jpg"), (390, 290))
    tigger = pygame.transform.scale(pygame.image.load(
        "images/tiggerAnswer.jpg"), (380, 280))
    tinkerBell = pygame.transform.scale(pygame.image.load(
        "images/tinkerbellAnswer.png"), (380, 350))
    tramp = pygame.transform.scale(pygame.image.load(
        "images/trampAnswer.png"), (320, 340))
    ursula = pygame.transform.scale(pygame.image.load(
        "images/ursulaAnswer.png"), (380, 280))
    wreck = pygame.transform.scale(pygame.image.load(
        "images/wreckitRalphAnswer.png"), (360, 280))
    buzz = pygame.transform.scale(pygame.image.load("images/buzzAnswer.jpg"), (390, 330))
    woody = pygame.transform.scale(pygame.image.load(
        "images/woodyAnswer.jpg"), (380, 280))
    aladdin = pygame.transform.scale(pygame.image.load(
        "images/aladdinAnswer.jpg"), (350, 310))
    dory = pygame.transform.scale(pygame.image.load("images/doriAnswer.jpg"), (420, 290))
    walle = pygame.transform.scale(pygame.image.load(
        "images/walleAnswer.jpg"), (380, 280))
    mike = pygame.transform.scale(pygame.image.load("images/mikeAnswer.jpg"), (370, 270))
    yoda = pygame.transform.scale(pygame.image.load("images/yodaAnswer.jpg"), (340, 350))
    joy = pygame.transform.scale(pygame.image.load("images/joyAnswer.jpg"), (390, 290))
    sadness = pygame.transform.scale(pygame.image.load(
        "images/sadnessAnswer.jpg"), (380, 290))
    minnie = pygame.transform.scale(pygame.image.load(
        "images/minnieAnswer.jpg"), (360, 290))
    merida = pygame.transform.scale(pygame.image.load(
        "images/meridaAnswer.jfif"), (360, 290))
    maui = pygame.transform.scale(pygame.image.load("images/mauiAnswer.jpg"), (300, 320))
    mcqueen = pygame.transform.scale(pygame.image.load(
        "images/mcqueenAnswer.jpg"), (430, 290))
    mater = pygame.transform.scale(pygame.image.load(
        "images/materAnswer.jpg"), (400, 300))
    chewbacca = pygame.transform.scale(pygame.image.load(
        "images/chewbaccaAnswer.jpg"), (430, 280))
    chip = pygame.transform.scale(pygame.image.load("images/chipAnswer.jpg"), (390, 290))
    forky = pygame.transform.scale(pygame.image.load(
        "images/forkyAnswer.jpg"), (390, 300))
    hercules = pygame.transform.scale(pygame.image.load(
        "images/herculesAnswer.png"), (330, 350))

    images = [stitch, cinderella, ariel, beast, genie, abu, anna, elsa, bambi, pinocchio, peterPan, captainHook, dumbo,
              cheshire, mulan, belle, tarzan, mickey, goofy, pluto, rapunzel, gus, hades, nemo, baymax, jafar, lady,
              ladyTremaine, lumiere, carpet, maleficent, maryPoppins, moana, mushu, olaf, pumbaa, timon, winnie, rafiki,
              sebastian, flounder, sven, tigger, tinkerBell, tramp, ursula, wreck, buzz, woody, aladdin, dory, walle,
              mike, yoda, joy, sadness, minnie, merida, maui, mcqueen, mater, chewbacca, chip, forky, hercules]
    return images
# End of disneyImageAnswers()

# Function that returns a list of Character/Player images
def flappyImages():
    bird = pygame.transform.scale(pygame.image.load("images/b1.png"), (80, 80))
    angryBird = pygame.transform.scale(pygame.image.load(
        "images/angryBird.png"), (60, 60))
    whale = pygame.transform.scale(pygame.image.load("images/whale.png"), (120, 80))
    snake = pygame.transform.scale(pygame.image.load(
        "images/flappySnake.png"), (80, 80))
    flappyBird = pygame.transform.scale(pygame.image.load(
        "images/flappyBird.png"), (120, 60))
    sheep = pygame.transform.scale(pygame.image.load("images/sheep.png"), (100, 70))
    seal = pygame.transform.scale(pygame.image.load("images/seal.png"), (70, 70))
    hedgehog = pygame.transform.scale(pygame.image.load(
        "images/flappyHedgehog.png"), (120, 100))
    parrot = pygame.transform.scale(pygame.image.load("images/parrot.png"), (80, 80))
    hen = pygame.transform.scale(pygame.image.load("images/flappyHen.png"), (90, 90))
    fly = pygame.transform.scale(pygame.image.load("images/flappyFly.png"), (90, 90))
    star = pygame.transform.scale(pygame.image.load("images/star.png"), (100, 100))
    pinkBird = pygame.transform.scale(pygame.image.load(
        "images/pinkBird.png"), (100, 100))
    bee = pygame.transform.scale(pygame.image.load("images/bee.jpg"), (100, 100))
    cat = pygame.transform.scale(pygame.image.load("images/flappyCat.png"), (100, 100))
    penguin = pygame.transform.scale(pygame.image.load(
        "images/flappyPing.jpg"), (100, 100))
    pig = pygame.transform.scale(pygame.image.load("images/flyingPig.png"), (100, 100))

    images = [bird, angryBird, whale, snake, flappyBird, sheep, seal, hedgehog, parrot, hen, fly, star,
              pinkBird, bee, cat, penguin, pig]
    return images
# End of flappyImages()
