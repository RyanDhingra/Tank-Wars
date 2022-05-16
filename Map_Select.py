import pygame
pygame.font.init()
pygame.mixer.init()





WIDTH, HEIGHT = 900, 500
WHITE = (255,255,255)
GREY = (100,100,100)
BG = pygame.transform.scale(pygame.image.load("Backgrounds/MainMenuBG.jpg"), (WIDTH, HEIGHT))
TITLE_PANEL = pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (300, 60))
TITLE_FONT = pygame.font.Font('Fonts/Stencil Regular.ttf', 40)
MAP_FONT = pygame.font.Font('Fonts/Stencil Regular.ttf', 20)

#Sounds
click_sound = pygame.mixer.Sound('Sounds/Click.wav')
click_sound.set_volume(0.07)





map1_vid = []
map2_vid = []
map3_vid = []
map4_vid = []

for x in range(1,144):
    if x < 10:
        filenum = f"00{x}.jpg"
    elif x >= 10 and x < 100:
        filenum = f"0{x}.jpg"
    elif x >= 100:
        filenum = f"{x}.jpg"
    map1_vid.append(pygame.transform.scale(pygame.image.load(f"Map 1 Frames/ezgif-frame-{filenum}"), (300, 165)))

for x in range(1,276):
    if x < 10:
        filenum = f"00{x}.jpg"
    elif x >= 10 and x < 100:
        filenum = f"0{x}.jpg"
    elif x >= 100:
        filenum = f"{x}.jpg"
    map2_vid.append(pygame.transform.scale(pygame.image.load(f"Map 2 Frames/ezgif-frame-{filenum}"), (300, 165)))

for x in range(1,199):
    if x < 10:
        filenum = f"00{x}.jpg"
    elif x >= 10 and x < 100:
        filenum = f"0{x}.jpg"
    elif x >= 100:
        filenum = f"{x}.jpg"
    map3_vid.append(pygame.transform.scale(pygame.image.load(f"Map 3 Frames/ezgif-frame-{filenum}"), (300, 165)))

for x in range(1,166):
    if x < 10:
        filenum = f"00{x}.jpg"
    elif x >= 10 and x < 100:
        filenum = f"0{x}.jpg"
    elif x >= 100:
        filenum = f"{x}.jpg"
    map4_vid.append(pygame.transform.scale(pygame.image.load(f"Map 4 Frames/ezgif-frame-{filenum}"), (300, 165)))





class Map_Element:

    def __init__(self, name, rect, image):
        self.name = name
        self.rect = rect
        self.image = image
    
    def getName(self):
        return self.name

    def getRect(self):
        return self.rect

    def getImage(self):
        return self.image
    




class Power_Up:

    def __init__(self, name, rect, image, duration):
        self.name = name
        self.rect = rect
        self.image = image
        self.duration = duration
    
    def getName(self):
        return self.name

    def getRect(self):
        return self.rect

    def getImage(self):
        return self.image

    def getDuration(self):
        return self.duration





def vid_player(WIN, map1_frame, map2_frame, map3_frame, map4_frame, map1, map2, map3, map4):

    WIN.blit(map1_vid[map1_frame], map1)
    WIN.blit(map2_vid[map2_frame], map2)
    WIN.blit(map3_vid[map3_frame], map3)
    WIN.blit(map4_vid[map4_frame], map4)
    pygame.time.delay(60)





def draw_items(WIN, map1, map2, map3, map4, title_panel, title_text, classic_label, space_label, marine_label, cyber_label, classic_colour, space_colour, marine_colour, cyber_colour):
    
    WIN.blit(BG, (0,0))

    WIN.blit(TITLE_PANEL, title_panel)
    title_text = TITLE_FONT.render(title_text, True, WHITE)
    WIN.blit(title_text, (450 - title_text.get_width()/2, 35))

    WIN.blit(classic_label.getImage(), classic_label.getRect())
    classic_text = MAP_FONT.render(classic_label.getName(), True, classic_colour)
    WIN.blit(classic_text, (classic_label.getRect().x + 15, classic_label.getRect().y + 10))

    WIN.blit(marine_label.getImage(), marine_label.getRect())
    marine_text = MAP_FONT.render(marine_label.getName(), True, marine_colour)
    WIN.blit(marine_text, (marine_label.getRect().x + 15, marine_label.getRect().y + 10))
    
    WIN.blit(space_label.getImage(),space_label.getRect())
    space_text = MAP_FONT.render(space_label.getName(), True, space_colour)
    WIN.blit(space_text, (space_label.getRect().x + 20, space_label.getRect().y + 10))

    WIN.blit(cyber_label.getImage(), cyber_label.getRect())
    cyber_text = MAP_FONT.render(cyber_label.getName(), True, cyber_colour)
    WIN.blit(cyber_text, (cyber_label.getRect().x + 20, cyber_label.getRect().y + 10))

    pygame.draw.rect(WIN, WHITE, map1)
    pygame.draw.rect(WIN, WHITE, map2)
    pygame.draw.rect(WIN, WHITE, map3)
    pygame.draw.rect(WIN, WHITE, map4)





def map_one():

    #Background
    BG = pygame.transform.scale(pygame.image.load('Backgrounds/ClassicBG.png'), (WIDTH, HEIGHT))

    #Map Elements
    shelters = []
    obstacles = []
    powerups = []
    tanks = []
    bullets = []

    shelters.append(Map_Element("top_shelter", pygame.Rect(400, 75, 100, 100), pygame.transform.scale(pygame.image.load('Obstacles/Shelter.jpg'), (100, 100))))
    shelters.append(Map_Element("bot_shelter", pygame.Rect(400, 325, 100, 100), pygame.transform.scale(pygame.image.load('Obstacles/Shelter.jpg'), (100, 100))))

    obstacles.append(Map_Element("L_barrierTL_H", pygame.Rect(75, 50, 100, 50), pygame.transform.scale(pygame.image.load('Obstacles/L_Obstacle.jpg'), (100, 50))))
    obstacles.append(Map_Element("L_barrierTR_H", pygame.Rect(725, 50, 100, 50), pygame.transform.scale(pygame.image.load('Obstacles/L_Obstacle.jpg'), (100, 50))))
    obstacles.append(Map_Element("L_barrierBL_H", pygame.Rect(75, 400, 100, 50), pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Obstacles/L_Obstacle.jpg'), (100, 50)), 180)))
    obstacles.append(Map_Element("L_barrierBR_H", pygame.Rect(725, 400, 100, 50), pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Obstacles/L_Obstacle.jpg'), (100, 50)), 180)))
    obstacles.append(Map_Element("L_barrierTL_V", pygame.Rect(75, 50, 50, 100), pygame.transform.scale(pygame.image.load('Obstacles/L_Obstacle_Extension.jpg'), (50, 50))))
    obstacles.append(Map_Element("L_barrierTR_V", pygame.Rect(775, 50, 50, 100), pygame.transform.scale(pygame.image.load('Obstacles/L_Obstacle_Extension.jpg'), (50, 50))))
    obstacles.append(Map_Element("L_barrierBL_V", pygame.Rect(75, 350, 50, 100), pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Obstacles/L_Obstacle_Extension.jpg'), (50, 50)), 180)))
    obstacles.append(Map_Element("L_barrierBR_V", pygame.Rect(775, 350, 50, 100), pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Obstacles/L_Obstacle_Extension.jpg'), (50, 50)), 180)))

    #Tank Images
    tanks.append(pygame.transform.scale(pygame.image.load('Tanks/ClassicTank1.png'), (40, 30)))
    tanks.append(pygame.transform.scale(pygame.image.load('Tanks/ClassicTank2.png'), (40, 30)))

    #Power-Ups
    powerups.append(Power_Up("Speed Boost", pygame.Rect(440, 450, 25, 25), pygame.transform.scale(pygame.image.load('Power-Ups/Speed Power Up.png'), (25, 25)), 10000))
    powerups.append(Power_Up("Shield", pygame.Rect(440, 25, 25, 25), pygame.transform.scale(pygame.image.load('Power-Ups/Shield Power Up.png'), (25, 25)), 10000))

    bullets.append(pygame.transform.scale(pygame.image.load('Bullets/ClassicBullet1.png'), (25, 35)))
    bullets.append(pygame.transform.scale(pygame.image.load('Bullets/ClassicBullet2.png'), (25, 35)))

    return [True, "map1", BG, obstacles, shelters, powerups, tanks, bullets]





def map_two():
    
    #Background
    BG = pygame.transform.scale(pygame.image.load('Backgrounds/SpaceBG.jpg'), (WIDTH, HEIGHT))

    #Map Elements
    shelters = []
    obstacles = []
    powerups = []
    tanks = []
    bullets = []

    shelters.append(Map_Element("space station", pygame.Rect(375, 175, 200, 200), pygame.transform.scale(pygame.image.load('Obstacles/Space Station.png'), (150, 150))))

    SHIPYARD = pygame.transform.scale(pygame.image.load('Obstacles/ShipyardLS.png'), (125, 250))
    
    obstacles.append(Map_Element(None, pygame.Rect(123, 125, 80, 35), None))
    obstacles.append(Map_Element(None, pygame.Rect(123, 339, 80, 35), None))
    obstacles.append(Map_Element(None, pygame.Rect(105, 155, 115, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(109, 150, 108, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(114, 145, 96, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(105, 343, 115, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(109, 348, 108, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(114, 353, 96, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(102, 160, 122, 66), None))
    obstacles.append(Map_Element(None, pygame.Rect(106, 226, 114, 51), None))
    obstacles.append(Map_Element(None, pygame.Rect(102, 277, 122, 66), None))

    obstacles.append(Map_Element(None, pygame.Rect(698, 125, 80, 35), None))
    obstacles.append(Map_Element(None, pygame.Rect(698, 339, 80, 35), None))
    obstacles.append(Map_Element(None, pygame.Rect(680, 155, 115, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(684, 150, 108, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(689, 145, 96, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(680, 343, 115, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(684, 348, 108, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(689, 353, 96, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(677, 160, 122, 66), None))
    obstacles.append(Map_Element(None, pygame.Rect(681, 226, 114, 51), None))
    obstacles.append(Map_Element(None, pygame.Rect(677, 277, 122, 66), None))

    #Tank Images
    tanks.append(pygame.transform.scale(pygame.image.load('Tanks/SpaceTank1.png'), (40, 60)))
    tanks.append(pygame.transform.scale(pygame.image.load('Tanks/SpaceTank2.png'), (40, 60)))

    #Power-Ups
    powerups.append(Power_Up("Radiation", pygame.Rect(440, 25, 25, 25), pygame.transform.scale(pygame.image.load('Power-Ups/Radiation Power Up.png'), (25, 25)), 15000))
    powerups.append(Power_Up("Breakdown", pygame.Rect(440, 450, 25, 25), pygame.transform.scale(pygame.image.load('Power-Ups/Breakdown Power Up.png'), (25, 25)), 2500))

    #Bullets
    bullets.append(pygame.transform.scale(pygame.image.load('Bullets/SpaceBullet1.png'), (23, 9)))
    bullets.append(pygame.transform.scale(pygame.image.load('Bullets/SpaceBullet2.png'), (23, 8)))

    return [True, "map2", BG, obstacles, shelters, powerups, tanks, SHIPYARD, bullets]





def map_three():
    
    #Background
    BG = []

    for x in range(1, 101): #101
        if x < 10:
            filename = f"000{x}"
        elif x >= 10 and x < 100:
            filename = f"00{x}"
        elif x >= 100:
            filename = f"0{x}" #for line below switch to color 1 and 079
        
        for x in range(4):
            BG.append(pygame.transform.scale(pygame.image.load(f"Backgrounds/MarineBG/water_079_c_{filename}.jpg"), (900, 500)))

    #Map Elements
    islands = []
    obstacles = []
    powerups = []
    tanks = []
    bullets = []

    SHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Obstacles/Ship.png'), (62, 305)), 90)
    
    obstacles.append(Map_Element(None, pygame.Rect(302, 73, 3, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(305, 71, 3, 9), None))
    obstacles.append(Map_Element(None, pygame.Rect(308, 69, 5, 12 ), None))
    obstacles.append(Map_Element(None, pygame.Rect(313, 67, 3, 16), None))
    obstacles.append(Map_Element(None, pygame.Rect(316, 66, 9, 19), None))
    obstacles.append(Map_Element(None, pygame.Rect(325, 62, 7, 26), None))
    obstacles.append(Map_Element(None, pygame.Rect(332, 61, 11, 29), None))
    obstacles.append(Map_Element(None, pygame.Rect(343, 59, 10, 33), None))
    obstacles.append(Map_Element(None, pygame.Rect(353, 57, 18, 36), None))
    obstacles.append(Map_Element(None, pygame.Rect(371, 55, 20, 40), None))
    obstacles.append(Map_Element(None, pygame.Rect(391, 54, 40, 43), None))
    obstacles.append(Map_Element(None, pygame.Rect(431, 52, 7, 46), None))
    obstacles.append(Map_Element(None, pygame.Rect(438, 50, 47, 50), None))
    obstacles.append(Map_Element(None, pygame.Rect(485, 52, 29, 46), None))
    obstacles.append(Map_Element(None, pygame.Rect(514, 54, 42, 43), None))
    obstacles.append(Map_Element(None, pygame.Rect(556, 55, 17, 40), None))
    obstacles.append(Map_Element(None, pygame.Rect(573, 57, 9, 36), None))
    obstacles.append(Map_Element(None, pygame.Rect(582, 59, 4, 32), None))
    obstacles.append(Map_Element(None, pygame.Rect(586, 62, 6, 26), None))
    obstacles.append(Map_Element(None, pygame.Rect(592, 64, 6, 22), None))

    obstacles.append(Map_Element(None, pygame.Rect(595, 422, 3, 5), None))
    obstacles.append(Map_Element(None, pygame.Rect(592, 420, 3, 9), None))
    obstacles.append(Map_Element(None, pygame.Rect(587, 419, 5, 12 ), None))
    obstacles.append(Map_Element(None, pygame.Rect(584, 417, 3, 16), None))
    obstacles.append(Map_Element(None, pygame.Rect(575, 415, 9, 19), None))
    obstacles.append(Map_Element(None, pygame.Rect(568, 412, 7, 26), None))
    obstacles.append(Map_Element(None, pygame.Rect(557, 410, 11, 29), None))
    obstacles.append(Map_Element(None, pygame.Rect(547, 408, 10, 33), None))
    obstacles.append(Map_Element(None, pygame.Rect(529, 407, 18, 36), None))
    obstacles.append(Map_Element(None, pygame.Rect(509, 405, 20, 40), None))
    obstacles.append(Map_Element(None, pygame.Rect(469, 403, 40, 43), None))
    obstacles.append(Map_Element(None, pygame.Rect(462, 402, 7, 46), None))
    obstacles.append(Map_Element(None, pygame.Rect(415, 400, 47, 50), None))
    obstacles.append(Map_Element(None, pygame.Rect(386, 402, 29, 46), None))
    obstacles.append(Map_Element(None, pygame.Rect(344, 403, 42, 43), None))
    obstacles.append(Map_Element(None, pygame.Rect(327, 405, 17, 40), None))
    obstacles.append(Map_Element(None, pygame.Rect(318, 407, 9, 36), None))
    obstacles.append(Map_Element(None, pygame.Rect(314, 409, 4, 32), None))
    obstacles.append(Map_Element(None, pygame.Rect(308, 412, 6, 26), None))
    obstacles.append(Map_Element(None, pygame.Rect(302, 414, 6, 22), None))
    
    obstacles.append(Map_Element("left_island", pygame.Rect(140, 190, 120, 120), None))
    obstacles.append(Map_Element("right_island", pygame.Rect(640, 190, 120, 120), None))

    #Islands
    islands.append(pygame.transform.scale(pygame.image.load('Obstacles/Sand.png'), (200, 200)))
    islands.append(pygame.transform.scale(pygame.image.load('Obstacles/Sand.png'), (200, 200)))

    #Tank Images
    tanks.append(pygame.transform.scale(pygame.image.load('Tanks/HoverTank1.png'), (36, 33)))
    tanks.append(pygame.transform.scale(pygame.image.load('Tanks/HoverTank2.png'), (36, 33)))

    #Power-Ups
    powerups.append(Power_Up("Infinite Ammo", pygame.Rect(440, 25, 25, 25), pygame.transform.scale(pygame.image.load('Power-Ups/Infinite Ammo Power Up.png'), (25, 25)), 5000))
    powerups.append(Power_Up("Speed Bullets", pygame.Rect(440, 450, 25, 25), pygame.transform.scale(pygame.image.load('Power-Ups/Bullet Speedup Power Up.png'), (25, 25)), 5000))

    #Bullets
    bullets.append(pygame.transform.scale(pygame.image.load('Bullets/WaterBullet1.png'), (23, 10)))
    bullets.append(pygame.transform.scale(pygame.image.load('Bullets/WaterBullet2.png'), (24, 10)))

    return [True, "map3", BG, obstacles, islands, powerups, tanks, bullets, SHIP]




def map_four():
    
    #Background
    BG = pygame.transform.scale(pygame.image.load('Backgrounds/GridBG.png'), (WIDTH, HEIGHT))

    #Map Elements
    shelters = []
    obstacles = []
    powerups = []
    tanks = []
    bullets = []

    #Obstacles
    obstacles.append(Map_Element("CircuitBoard1", pygame.Rect(120, 45, 186, 100), pygame.transform.scale(pygame.image.load('Obstacles/CircuitBoard.png'), (200, 100))))
    obstacles.append(Map_Element(None, pygame.Rect(306, 45, 14, 92), None))
    obstacles.append(Map_Element("CircuitBoard2", pygame.Rect(582, 45, 186, 100), pygame.transform.scale(pygame.image.load('Obstacles/CircuitBoard.png'), (200, 100))))
    obstacles.append(Map_Element(None, pygame.Rect(768, 45, 14, 92), None))
    obstacles.append(Map_Element("CircuitBoard3", pygame.Rect(120, 353, 186, 100), pygame.transform.scale(pygame.image.load('Obstacles/CircuitBoard.png'), (200, 100))))
    obstacles.append(Map_Element(None, pygame.Rect(306, 353, 14, 92), None))
    obstacles.append(Map_Element("CircuitBoard4", pygame.Rect(582, 353, 186, 100), pygame.transform.scale(pygame.image.load('Obstacles/CircuitBoard.png'), (200, 100))))
    obstacles.append(Map_Element(None, pygame.Rect(768, 353, 14, 92), None))
    obstacles.append(Map_Element("Chip", pygame.Rect(275, 200, 100, 100), pygame.transform.scale(pygame.image.load('Obstacles/Chip.jpg'), (100, 100))))
    obstacles.append(Map_Element("Chip", pygame.Rect(525, 200, 100, 100), pygame.transform.scale(pygame.image.load('Obstacles/Chip.jpg'), (100, 100))))

    #Tank Images
    tanks.append(pygame.transform.scale(pygame.image.load('Tanks/GridTank1.png'), (40, 30)))
    tanks.append(pygame.transform.scale(pygame.image.load('Tanks/GridTank2.png'), (40, 30)))

    #Power-Ups
    powerups.append(Power_Up("Hijack", pygame.Rect(440, 25, 25, 25), pygame.transform.scale(pygame.image.load('Power-Ups/Hijack Power Up.png'), (25, 25)), 10000))
    powerups.append(Power_Up("Virus", pygame.Rect(440, 450, 25, 25), pygame.transform.scale(pygame.image.load('Power-Ups/Virus Power Up.png'), (25, 25)), 5000))

    #Bullets
    bullets.append(pygame.transform.scale(pygame.image.load('Bullets/GridBullet1.png'), (36, 27)))
    bullets.append(pygame.transform.scale(pygame.image.load('Bullets/GridBullet2.png'), (36, 27)))

    return [True, "map4", BG, obstacles, shelters, powerups, tanks, bullets]





def map_select(WIN):

    pygame.display.set_caption("Select Map")

    #Rects
    title = pygame.Rect(300, 20, 400, 40)
    title_text = "Map Select"
    topleft = pygame.Rect(100, 100, 300, 165)
    topright = pygame.Rect(500, 100, 300, 165)
    botleft = pygame.Rect(100, 310, 300, 165)
    botright = pygame.Rect(500, 310, 300, 165)

    classic_label = Map_Element("Classic", pygame.Rect(100, 70, 100, 30), pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (100, 30)))
    space_label = Map_Element("Space", pygame.Rect(700, 70, 100, 30), pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (100, 30)))
    marine_label = Map_Element("Marine", pygame.Rect(100, 280, 100, 30), pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (100, 30)))
    cyber_label = Map_Element("Cyber", pygame.Rect(700, 280, 100, 30), pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (100, 30)))

    map1_frame = 0
    map2_frame = 0
    map3_frame = 0
    map4_frame = 0

    classic_colour = WHITE
    space_colour = WHITE
    marine_colour = WHITE
    cyber_colour = WHITE
    
    run = True
    while run:

        #Mouse
        mouse = pygame.mouse.get_pos()

        #Event Handler
        for event in pygame.event.get():

            if classic_label.getRect().collidepoint(mouse[0], mouse[1]):
                classic_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    print("Map 1 Selected")
                    click_sound.play()
                    return map_one()
            else:
                classic_colour = WHITE 

            if space_label.getRect().collidepoint(mouse[0], mouse[1]):
                space_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    print("Map 2 Selected")
                    click_sound.play()
                    return map_two()
            else:
                space_colour = WHITE

            if marine_label.getRect().collidepoint(mouse[0], mouse[1]):
                marine_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    print("Map 3 Selected")
                    click_sound.play()
                    return map_three()
            else:
                marine_colour = WHITE

            if cyber_label.getRect().collidepoint(mouse[0], mouse[1]):
                cyber_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    print("Map 4 Selected")
                    click_sound.play()
                    return map_four()
            else:
                cyber_colour = WHITE

        draw_items(WIN, topleft, topright, botleft, botright, title, title_text, classic_label, space_label, marine_label, cyber_label, classic_colour, space_colour, marine_colour, cyber_colour)
        vid_player(WIN, map1_frame, map2_frame, map3_frame, map4_frame, topleft, topright, botleft, botright)
        
        if map1_frame >= len(map1_vid) - 1:
            map1_frame = 0
        else:
            map1_frame += 1

        if map2_frame >= len(map2_vid) - 1:
            map2_frame = 0
        else:
            map2_frame += 1
        
        if map3_frame >= len(map3_vid) - 1:
            map3_frame = 0
        else:
            map3_frame += 1

        if map4_frame >= len(map4_vid) - 1:
            map4_frame = 0
        else:
            map4_frame += 1

        pygame.display.update()

