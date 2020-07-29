
# CBSE Class 12
# Computer Science Project
# Student Name - Abantika Jena
# Class/Sec - 12A

# Project Name :-  " Dino T-rex Google game ".

# Make the Dragon jump or bow.
# So that it won't get hit with obstacles.
# Game starts with basic information and initial score and high score as '0'.
# It gets updated automaticaly as we reach hich score
# After games get over, it can be again started with new high score

# import pygame

import pygame
from pygame.locals import *

# module initialized
pygame.init()

# variables
# Highest Score
score = 0  # score calculating
High_Score = [-1]  # List of scores
high_score = 0  # initial high score

# Screen height and width , (length,width) in form of tuple
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dino T-rex jump game by Abantika 12A")  # Giving title of the game

# font
font = pygame.font.Font("freesansbold.ttf", 20)  # font type1
font1 = pygame.font.Font("freesansbold.ttf", 25)  # font type1
font2 = pygame.font.Font("freesansbold.ttf", 30)  # font type2
font3 = pygame.font.Font("freesansbold.ttf", 40)  # font type3

# colours
#           R   G   B
sky_blue = (170, 255, 255)  # Sky_blue
black =    (  0,   0,   0)  # Black
red =      (255,   0,   0)  # Red
blue =     (  0,   0, 255)  # Blue
dark_blue =(  0,   0, 128)  # Dark Blue

# Sound effect dictionary
GAME_SOUNDS = {}
# Value of GAME_SOUNDS
GAME_SOUNDS["Dino_die"] = pygame.mixer.Sound('C:\\Users\\admin\\PycharmProjects\\Dino game\\Dino_die.wav')   # Check again
GAME_SOUNDS["Dino_jump"] = pygame.mixer.Sound('C:\\Users\\admin\\PycharmProjects\\Dino game\\Dino_jump.wav')
GAME_SOUNDS["CheckPoint"] = pygame.mixer.Sound('C:\\Users\\admin\\PycharmProjects\\Dino game\\CheckPoint.wav')

# Background_music
music = pygame.mixer.music.load("C:\\Users\\admin\\PycharmProjects\\Dino game\\Background music_Warm Light.mp3")

# Real game loop to start game
def gamestarts(high_score):

    # Play background music
    pygame.mixer.music.play(-1)
    def Find_High_Score(score_got):  # Function for Find_High_Score
        High_Score.append(score_got)  # Appending new scores into it
        for i in range(0, len(High_Score)):  # Performing insertion sorting
            key = High_Score[i]
            j = i - 1
            while j >= 0 and key < High_Score[j]:  # Sorting in Accending Order
                High_Score[j + 1] = High_Score[j]
                j = j - 1
            else:
                High_Score[j + 1] = key
        highest_score = High_Score[-1]
        return highest_score  # Return the output of function Find_High_Score

    # variables in function Find_High_Score

    # co-ordinate of background
    backx = 0  # x co-ordinate of background
    backy = 0  # y co-ordinate of background

    # co-ordinate of Dinasore
    drax = 50  # x co-ordinate of Dinasore
    dray = 275  # y co-ordinate of Dinasore

    # co-ordinate of tree
    treex = 1450  # x co-ordinate of obstacles
    treey = 282  # y co-ordinate of obstacles

    # co-ordinate of sun
    sunx = 100  # x co-ordinate of sun
    suny = 50  # y co-ordinate of sun

    # velocity
    in_velocity = 0  # initial increase in velocity
    back_velocity = 0  # velocity of background

    #index of diff. image
    walkpoint = 0  # index of diff. image of dragon of walking
    flypoint = 0  # index of diff. image of bird
    bowpoint = 0  # index of diff. image of dragon of bow
    firepoint = 0  # index of diff. image of fire
    zombiespoint = 0  # index of diff. image of zombie
    gravity = 5  # amount of up-down
    score = 0  # initial score

    # Sound effect point
    GAME_SOUNDS_Dino_die = 0

    # Boolean variable
    game = False  # Boolean for starting point for diff img & make dino move
    jump = False  # Boolean to start jumping
    gameover = False  # Boolean to know when game gets over
    bow = False  # Boolean to bow

    while True:

        # Sound Effect point
        GAME_SOUNDS_CheckPoint = 0

        # image requried in this loop

        # Dragon  # Walking
        dragon = pygame.image.load("dra1.png")  # import dragon
        dragon = pygame.transform.scale(dragon, (50, 50))  # Scale dragon
        dragon2 = pygame.image.load("dra2.png")  # import dragon2
        dragon2 = pygame.transform.scale(dragon2, (50, 50))  # Scale dragon2
        dragon3 = pygame.image.load("dra3.png")  # import dragon3
        dragon3 = pygame.transform.scale(dragon3, (50, 50))  # Scale dragon3
        dragon4 = pygame.image.load("dra4.png")  # import dragon4
        dragon4 = pygame.transform.scale(dragon4, (50, 50))  # Scale dragon4
        dragon5 = pygame.image.load("dra4.png")  # import dragon5
        dragon5 = pygame.transform.scale(dragon5, (50, 50))  # Scale dragon5

        # Dragon  # Walking
        dragon_down1 = pygame.image.load("dra_down1.png")  # import dragon bow 1
        dragon_down1 = pygame.transform.scale(dragon_down1, (50, 50))  # Scale dragon bow 1
        dragon_down2 = pygame.image.load("dra_down2.png")  # import dragon bow 2
        dragon_down2 = pygame.transform.scale(dragon_down2, (50, 50))  # Scale dragon bow 2

        # Tree
        tree = pygame.image.load("tree.png")  # import tree
        tree = pygame.transform.scale(tree, (70, 50))  # Scale tree
        tree1 = pygame.image.load("tree1.png")  # import tree1
        tree1 = pygame.transform.scale(tree1, (100, 60))  # Scale tree1
        tree2 = pygame.image.load("tree2.png")  # import tree2
        tree2 = pygame.transform.scale(tree2, (90, 60))  # Scale tree2
        tree3 = pygame.image.load("tree3.png")  # import tree3
        tree3 = pygame.transform.scale(tree3, (45, 60))  # Scale tree3
        tree4 = pygame.image.load("tree4.png")  # import tree4
        tree4 = pygame.transform.scale(tree4, (70, 60))  # Scale tree4

        # Bird
        bird_up = pygame.image.load("bird up.png")  # import bird_up
        bird_up = pygame.transform.scale(bird_up, (50, 50))  # Scale bird_up
        bird_down = pygame.image.load("bird down.png")  # import bird_up
        bird_down = pygame.transform.scale(bird_down, (50, 50))  # Scale bird_up

        # Fire
        fire1 = pygame.image.load("fire1.png")  # import fire1
        fire1 = pygame.transform.scale(fire1, (50, 50))  # Scale fire1
        fire2 = pygame.image.load("fire2.jpg")  # import fire2
        fire2 = pygame.transform.scale(fire2, (50, 50))  # Scale fire2

        # Zombies
        Zombie1 = pygame.image.load("z1.jpg")  # import Zombie1
        Zombie1 = pygame.transform.scale(Zombie1, (50, 90))  # Scale Zombie1
        Zombie2 = pygame.image.load("z2.jpg")  # import Zombie2
        Zombie2 = pygame.transform.scale(Zombie2, (70, 90))  # Scale Zombie2

        # Background
        background = pygame.image.load("background.png")  # import background

        # Sun
        sun = pygame.image.load("sun.png")  # import bird_up
        sun = pygame.transform.scale(sun, (100, 100))  # Scale bird_up

        # gameover_restart
        gameover_restart = pygame.image.load("gameover.png")  # import gameover_reply
        gameover_restart = pygame.transform.scale(gameover_restart, (40, 40))  # scale gameover_reply

        # list of different posture

        # Dragon
        # Walk
        walk = [dragon, dragon, dragon, dragon,
                dragon2, dragon2, dragon2, dragon2,
                dragon3, dragon3, dragon3, dragon3, dragon3, dragon3, dragon3, dragon3,
                dragon5, dragon5, dragon5, dragon5, dragon5, dragon5, dragon5, dragon5,
                dragon4, dragon4, dragon4, dragon4, dragon4, dragon4, dragon4, dragon4]
        # Bow
        bow_list = [dragon_down1, dragon_down1, dragon_down1, dragon_down1, dragon_down1, dragon_down1,
                    dragon_down2, dragon_down2, dragon_down2, dragon_down2, dragon_down2, dragon_down2, ]

        # Bird
        bird_fly = [bird_up, bird_up, bird_up, bird_up, bird_up,bird_up, bird_up, bird_up,
                   bird_down, bird_down, bird_down, bird_down, bird_down, bird_down]

        # Fire
        fire_list = [fire1, fire1, fire1, fire1, fire1, fire1,
                     fire2, fire2, fire2, fire2, fire2, fire2 ]

        # Zombie1
        zombie_list = [Zombie1, Zombie1, Zombie1, Zombie1,
                       Zombie1, Zombie1, Zombie1, Zombie1,
                       Zombie2, Zombie2, Zombie2, Zombie2,
                       Zombie2, Zombie2, Zombie2, Zombie2,]

        # Main starting of event
        for event in pygame.event.get():
            # From the total event taking place abstract some to mach with our use
            if event.type == QUIT:  # To make the screen stay till not quit
                pygame.quit()  # Quite the Screen
            if event.type == KEYDOWN:  # When any key is pressed
                if event.key == K_UP:  # To start the movement when called
                    # Loop activate when up key is pressed
                    if dray == 275:
                        jump = True
                        back_velocity = 4
                        game = True
                        bow = False
                if event.key == K_SPACE:  # To restart the game but with same high score
                    # Loop activate when spacebar key is pressed
                    gamestarts(score)
                if event.key == K_DOWN:  # To bow by Dino
                    # Loop activate when down key is pressed
                    if dray == 275:
                        bow = True
                        jump = False
                        game = True

        # To restart
        # background
        if backx == -600:
            backx = 0
        # obstacles
        if treex < -3400:
            treex = 550

        # Rules for collision & stop
        # for tree
        if (treex < drax + 50 < treex + 70) and (treey < dray + 50 < treey + 50):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()


        # for tree1
        if (treex + 400 < drax + 50 < treex + 400 + 10) and (treey < dray + 50 < treey + 60):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()

        # for tree2
        if (treex + 800 < drax + 50 < treex + 800 + 90) and (treey - 8 < dray + 50 < treey - 8 + 60):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()

        # for tree3
        if (treex + 1200 < drax + 50 < treex + 1200 + 45) and (treey - 8 < dray + 50 < treey - 8 + 60):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()

        # for tree4
        if (treex + 1600 < drax + 50 < treex + 1600 + 75) and (treey - 2 < dray + 50 < treey - 2 + 60):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()

        # for bird ground level
        if (treex + 2000 < drax + 50 < treex + 2000 + 50) and (treey < dray + 50 < treey + 50):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()

        # for bird sky level
        if bow == False:
            if (treex + 2400 < drax + 50 < treex + 2400 + 50) and (treey - 25 < dray + 50 < treey - 5 + 50):
                back_velocity = 0  # Background will stop
                walkpoint = 0  # Dino won't walk
                flypoint = 0  # Bird won't fly
                bowpoint = 0  # Dino won't bow
                game = False
                gameover = True  # Game will gets over
                for i in range(1):  # Sound effect - Dino Die
                    GAME_SOUNDS_Dino_die += 1
                    if GAME_SOUNDS_Dino_die <= 2:
                        GAME_SOUNDS["Dino_die"].play()

        # for bird ground level from bow
        if (treex + 3000 < drax + 50 < treex + 3000 + 50) and (treey < dray + 50 < treey + 50):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()

        # for fire
        if (treex + 3400 < drax + 50 < treex + 3400 + 50) and (treey < dray + 50 < treey + 50):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()

        # For zombies
        if (treex + 3400 < drax + 50 < treex + 3400 + 50) and (treey < dray + 50 < treey + 90):
            back_velocity = 0  # Background will stop
            walkpoint = 0  # Dino won't walk
            flypoint = 0  # Bird won't fly
            bowpoint = 0  # Dino won't bow
            game = False
            gameover = True  # Game will gets over
            for i in range(1):  # Sound effect - Dino Die
                GAME_SOUNDS_Dino_die += 1
                if GAME_SOUNDS_Dino_die <= 2:
                    GAME_SOUNDS["Dino_die"].play()

        # Score counting
        if game == True:
            score += 1

        # Score count checking
        if game == True:
            if score % 1000 == 0:
                for i in range(1):  # Sound effect - Dino Score Count checking
                    GAME_SOUNDS_CheckPoint += 1
                    if GAME_SOUNDS_CheckPoint <= 3:
                        GAME_SOUNDS["CheckPoint"].play()

        # Text formating

        text = font1.render("Score : " + str(score), True, black)  # Score
        text1 = font1.render("Game Over", True, red )  # Game Over
        text2 = font.render("Press Space To Continue", True, black)  # Press Space To Continue
        text3 = font3.render(" To Strat ", True, dark_blue) # To start
        text4 = font2.render(" Press Up Button ", True, blue)  # Press Up Button
        text_high_score = font1.render(" High Score : " + str(Find_High_Score(score)), True, black)  # High Score

        # increasing velocity
        if game == True:
            if score % 2000 == 0 :
                in_velocity += 1

        # Velocity
        backx -= back_velocity  # To move background
        treex -= back_velocity  # To move all trees

        # Front Screen
        Front_Screen = [
        # act as a gap filler of Screen
        screen.fill(sky_blue),
        # to insert background and the index of background
        screen.blit(background, [backx, backy]),
        # To add another background to the previous one
        screen.blit(background, [backx + 600, backy]),
        # Sun on screen
        screen.blit(sun, [sunx, suny]),
        # Score showing on screen
        screen.blit(text, [300, 100]),
        # High Score showing on screen
        screen.blit(text_high_score, [300, 50]) ]  # List of Front Screen

        # Call Front_Screen
        for i in range(len(Front_Screen)):
            Front_Screen[i]

        # Screen when games get over
        if gameover == True :
            screen.blit(text1, [225, 150])  # Game Over
            screen.blit(text2, [175, 180])  # Press Space To Continue
            screen.blit(gameover_restart, [250, 210])  # Replay image

        # Jump
        if 276 > dray > 125:
            if jump == True:
                if dray >= 265:
                    GAME_SOUNDS["Dino_jump"].play()
                dray -= gravity
                screen.blit(walk[walkpoint], [drax, dray])

        else:
            jump = False
            screen.blit(walk[walkpoint], [drax, dray])

        # Comedown
        if dray < 275:
            if jump == False:
                dray += gravity
                screen.blit(walk[walkpoint], [drax, dray])

        # moving legs of dragon
        if dray == 275:
            if bow == True:
                screen.blit(bow_list[bowpoint], [drax, dray])
                if game == True:
                    bowpoint += 1
                    if bowpoint > 11:
                        bowpoint = 0
            else:
                screen.blit(walk[walkpoint], [drax, dray])
                if game == True :
                    walkpoint += 1
                    if walkpoint > 15:
                        walkpoint = 0

        # Moving birds wings
        if game == True :
            flypoint += 1
            if flypoint > 11:
                flypoint = 0

        # Burning Fire
        if game == True :
            firepoint += 1
            if firepoint > 11:
                firepoint = 0

        # Zompie
        if game == True:
            zombiespoint += 1
            if zombiespoint > 11:
                zombiespoint = 0

        # Information Screen
        if score == 0:
            screen.blit(text3, [200, 150])
            screen.blit(text4, [150, 210])

        # Position of Obstacles
        Position_Obstacles =[
            # Tree position
            # for tree
            screen.blit(tree, [treex, treey]),
            # for tree1
            screen.blit(tree1, [treex + 400, treey]),
            # for tree2
            screen.blit(tree2, [treex + 800, treey - 8]),
            # for tree3
            screen.blit(tree3, [treex + 1200, treey - 8]),
            # for tree4
            screen.blit(tree4, [treex + 1600, treey - 2]),

            # Bird position
            # for bird ground level
            screen.blit(bird_fly[flypoint], [treex + 2000, treey]),
            # for bird sky level
            screen.blit(bird_fly[flypoint], [treex + 2400, treey - 25]),

            # Fire
            screen.blit(fire_list[firepoint], [treex + 3000, treey]),

            # Zombie
            screen.blit(zombie_list[zombiespoint], [treex + 3400, treey -35])]  # List of position of Obstacles

        # Call obstacles
        for i in range(len(Position_Obstacles)):
            Position_Obstacles[i]

        # Update every entry
        pygame.display.update()  # update te entry

gamestarts(high_score)
