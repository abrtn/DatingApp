import pygame

PICWIDTH = 300
PICHEIGHT = 400

class Profile:

    picturex = 60
    picturey = 20
    namex = 20
    namey = 450

    def __init__(self, name, age, pronouns, orientation, bio, images, blur):
        self.name = name
        self.age = age
        self.pronouns = pronouns
        self.orientation = orientation
        self.bio = bio
        self.images = images
        self.blur = blur
        self.interests = []


def importProfileData(profiles):
    # Compile all profiles
    file = open("profiles.txt")
    i = 0
    for line in file:
        if line == '' or line[0] == '_':
            i += 1
            continue
        prof = "profile" + str(i+1)
        profile = line.split(',')
        images = []
        blur = []
        # Needs tailing value in profiles
        for j in range(5, len(profile)-1):
            pic = pygame.image.load("profilePics/" + prof + "/" + profile[j])
            pic = pygame.transform.scale(pic, (PICWIDTH,PICHEIGHT))
            images.append(pic)
            picblur = pygame.image.load("profilePics/" + prof + "/blur" + profile[j])
            picblur = pygame.transform.scale(picblur, (PICWIDTH,PICHEIGHT))
            blur.append(picblur)
        profiles.append(Profile(profile[0], profile[1], profile[2], profile[3], profile[4], images, blur))
        i += 1
        
            



def closeApp():
    # save matrix and other data
    pass

def loadApp(swipeMatrix):
    # reload matrix and other data
    pass