import pygame
import functions as f

NUMPROFILES = 2
WIDTH, HEIGHT = 360, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def showProfileBasic(profiles, i, userData):
    # display single profile and get swipe
    lastPress = 0
    imageIndex = 0
    pf = profiles[i]
    blurIndexLess = 1
    blurIndexMore = len(pf.images) - 1
    while(True):
        clock.tick(20)
        lastPress += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and lastPress >= 10:
            lastPress = 0
            userData[i] ='Y'
            break
        if keys[pygame.K_LEFT] and lastPress >= 10:
            lastPress = 0
            userData[i] = 'N'
            break
        if keys[pygame.K_SPACE] and lastPress >= 10:
            lastPress = 0
            blurIndexMore = imageIndex
            blurIndexLess = imageIndex + 2
            imageIndex += 1
            if imageIndex >= len(pf.images):
                blurIndexLess = 1
                imageIndex = 0
            elif imageIndex >= len(pf.images) - 1:
                blurIndexLess = 0
                
        pic = pf.images[imageIndex]
        picBlurLess = pf.blur[blurIndexLess]
        picBlurMore = pf.blur[blurIndexMore]
        WIN.fill((0,0,0))
        text = pf.name + " " + pf.age
        name = textFont.render(text, False, (255,255,255))
        pronouns = textFontSub.render(pf.pronouns, False, (200,200,200))
        WIN.blit(name, (pf.namex, pf.namey))
        WIN.blit(pronouns, (pf.namex, pf.namey+30))
        #WIN.blit(picBlurLess, (pf.picturex - 20, pf.picturey))
        #WIN.blit(picBlurMore, (pf.picturex +20, pf.picturey))
        WIN.blit(pic, (pf.picturex, pf.picturey))
        pygame.display.update()
    return 1

# Main loop
count = 0
lastPress = 0

pygame.display.set_caption("Game Window")
clock = pygame.time.Clock()

pygame.font.init()
textFont = pygame.font.SysFont('Times New Roman', 30)
textFontSub = pygame.font.SysFont('Times New Roman', 20)

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
    
    if not showProfileBasic(profiles, profNum, userData):
        break
    profNum += 1
    if(profNum >= len(profiles)):
        break

                            
    


