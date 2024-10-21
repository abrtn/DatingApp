import pygame
import functions as f
import profileFunctions as pFunc

NUMPROFILES = 2

# Main loop
count = 0
lastPress = 0

pygame.display.set_caption("Game Window")
clock = pygame.time.Clock()

# get profile data
run = True
profiles = []#*NUMPROFILES
f.importProfileData(profiles)

# get saved data if exists and initialize matrix
swipeMatrix = []
f.loadApp(swipeMatrix)

imageIndex = 0
userData = ['N']*NUMPROFILES
profNum = 0
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    choice = pFunc.showProfile(profiles[profNum], 0)
    if choice is None:
        break
    else:
        userData[profNum] = choice
    profNum += 1
    if(profNum >= len(profiles)):
        swipeMatrix.append(userData)
        break
