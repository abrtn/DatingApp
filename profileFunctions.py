import pygame

WIDTH, HEIGHT = 360, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
textFont = pygame.font.SysFont('Times New Roman', 30)
textFontSub = pygame.font.SysFont('Times New Roman', 20)

clock = pygame.time.Clock()

def showOverlay(pf, x, y):
    text = pf.name + " " + pf.age
    name = textFont.render(text, False, (255,255,255))
    pronouns = textFontSub.render(pf.pronouns, False, (200,200,200))
    WIN.blit(name, (x, y))
    WIN.blit(pronouns, (x, y+30))
    
def nextImage(pf):
    blurIndexMore = pf.imageIndex
    blurIndexLess = pf.imageIndex + 2
    pf.imageIndex += 1
    if pf.imageIndex >= len(pf.images):
        pf.imageIndex = 0
    elif pf.imageIndex >= len(pf.images) - 1:
        blurIndexLess = 0

def showProfileBasic(pf):
    WIN.fill((0,0,0))        
    pic = pf.images[pf.imageIndex]
    WIN.blit(pic, (pf.picturex, pf.picturey))
    showOverlay(pf, pf.namex, pf.namey)
    pygame.display.update()

def showProfileFull(pf):
    pass

def showProfile(pf, version):
    # display single profile and get swipe
    lastPress = 0
    while(True):
        clock.tick(20)
        lastPress += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and lastPress >= 10:
            return 'Y'
        if keys[pygame.K_LEFT] and lastPress >= 10:
            return 'N'
        if keys[pygame.K_SPACE] and lastPress >= 10:
            lastPress = 0
            nextImage(pf)
        showProfileBasic(pf)
    return None
