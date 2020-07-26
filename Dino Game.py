# import pygame

import pygame
from pygame.locals import *

# module initialized
pygame.init()
# Screen height and width , (length,width) in form of tuple
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dino T-rex jump game by Abantika")  # Giving title of the game
# variables
backx = 0
backy = 0
treex = 450
treey = 282
back_velocity = 0
while True:
    # colours
    sky_blue = (170, 255, 255)
    # variables

    # image
    dragon = pygame.image.load("dra1.png")  # import dragon
    dragon = pygame.transform.scale(dragon, (70, 80))
    tree = pygame.image.load("tree.png")  # import tree
    tree = pygame.transform.scale(tree, (70, 50))
    tree1 = pygame.image.load("tree1.png")  # import tree1
    tree1 = pygame.transform.scale(tree1, (100, 60))
    tree2 = pygame.image.load("tree2.png")  # import tree2
    tree2 = pygame.transform.scale(tree2, (90, 60))
    tree3 = pygame.image.load("tree3.png")  # import tree3
    tree3 = pygame.transform.scale(tree3, (45, 60))
    tree4 = pygame.image.load("tree4.png")  # import tree4
    tree4 = pygame.transform.scale(tree4, (70, 60))
    background = pygame.image.load("background.png")  # import background
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                back_velocity = 6
    if backx == -600:  # To restart the background
        backx = 0
    if treex < -1600:
        treex = 550
    backx -= back_velocity  # To move background
    treex -= back_velocity  # To move all trees
    screen.fill(sky_blue)  #
    screen.blit(background, [backx, backy])  # to insert background and the index of background
    screen.blit(background, [backx + 600, backy])  # To add another background to the previous one
    screen.blit(tree, [treex, treey])
    screen.blit(tree1, [treex + 400, treey])
    screen.blit(tree2, [treex + 800, treey - 8])
    screen.blit(tree3, [treex + 1200, treey - 8])
    screen.blit(tree4, [treex + 1600, treey - 2])
    screen.blit(dragon, [50, 250])
    pygame.display.update()  # update te entry

