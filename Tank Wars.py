import pygame
import time
from Main_Menu import main_menu
from Play_Again import play_again
pygame.init()
pygame.mixer.init()


#Window Configuration
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
FPS = 60
w,h = 30, 40
bullet_w, bullet_h = 35, 25

#Sounds
explosion = pygame.mixer.Sound('Sounds/Explosion.mp3')
explosion.set_volume(0.5)
powerup_sound = pygame.mixer.Sound('Sounds/Powerup.wav')
powerup_sound.set_volume(0.07)
classic_bullet_sound = pygame.mixer.Sound('Sounds/Classic Bullet.ogg')
classic_bullet_sound.set_volume(0.07)
space_bullet_sound = pygame.mixer.Sound('Sounds/Space Bullet.wav')
space_bullet_sound.set_volume(0.07)
marine_bullet_sound = pygame.mixer.Sound('Sounds/Marine Bullet.wav')
marine_bullet_sound.set_volume(0.07)
cyber_bullet_sound = pygame.mixer.Sound('Sounds/Cyber Bullet.wav')
cyber_bullet_sound.set_volume(0.07)
rebound_sound = pygame.mixer.Sound('Sounds/Rebound.wav')
rebound_sound.set_volume(0.07)

#Events
t2_hit = pygame.USEREVENT + 1
t1_hit = pygame.USEREVENT + 2

#Powerup Events
t1_speed_up_hit = pygame.USEREVENT + 3
t2_speed_up_hit = pygame.USEREVENT + 4
t1_shield_hit = pygame.USEREVENT + 5
t2_shield_hit = pygame.USEREVENT + 6
t1_radiation_hit = pygame.USEREVENT + 7
t2_radiation_hit = pygame.USEREVENT + 8
t1_breakdown_hit = pygame.USEREVENT + 9
t2_breakdown_hit = pygame.USEREVENT + 10
t1_virus_hit = pygame.USEREVENT + 11
t2_virus_hit = pygame.USEREVENT + 12
t1_hijack_hit = pygame.USEREVENT + 13
t2_hijack_hit = pygame.USEREVENT + 14
t1_infiniteammo_hit = pygame.USEREVENT + 15
t2_infiniteammo_hit = pygame.USEREVENT + 16
t1_speedbullets_hit = pygame.USEREVENT + 17
t2_speedbullets_hit = pygame.USEREVENT + 18

t1_total_wins = 0
t2_total_wins = 0

#Explosion Animation Images
exp_list = []
row = 1
column = 1

while row < 9:
    if row > 1 and column < 9:
        exp_list.append(pygame.transform.scale(pygame.image.load(f'Explosion Animation/row-{row}-column-{column}.png'), (100, 100)))
        column += 1
        if column > 8:
            column = 1
            row += 1
    elif row == 1 and column + 2 < 9:
        exp_list.append(pygame.transform.scale(pygame.image.load(f'Explosion Animation/row-{row}-column-{column + 2}.png'), (100, 100)))
        column += 1
        if column + 2 == 9:
            row += 1
            column = 1

#Rebounds
t1_rebounded = []
t2_rebounded = []





def powerup_infiniteammo(infinite_ammo, timer, current_time, duration):
    if timer <= current_time:
        infinite_ammo.y = 125
    
    if duration <= current_time:
        infinite_ammo_status = False
    else:
        infinite_ammo_status = True
    
    return infinite_ammo_status





def powerup_hijack(hijack, timer, current_time, duration):
    if timer <= current_time:
        hijack.y = 50
    
    if duration <= current_time:
        hijack_status = False
    else:
        hijack_status = True
    
    return hijack_status





def powerup_virus(virus, timer, current_time, duration):
    if timer <= current_time:
        virus.y = 430
    
    if duration <= current_time:
        virus_status = False
    else:
        virus_status = True
    
    return virus_status





def powerup_breakdown(breakdown, timer, current_time, duration):
    if timer <= current_time:
        breakdown.y = 430
    
    if duration <= current_time:
        breakdown_status = False
    else:
        breakdown_status = True
    
    return breakdown_status





def powerup_radiation(radiation, timer, current_time, duration):
    if timer <= current_time:
        radiation.y = 50
    
    if duration <= current_time:
        radiation_status = False
    else:
        radiation_status = True
    
    return radiation_status





def powerup_speed(speedup, timer, current_time, duration):
    if timer <= current_time:
        speedup.y = 452.5
    
    if duration <= current_time:
        vel = 1
    else:
        vel = 2
    
    return vel





def powerup_speedbullet(bullet_speed, timer, current_time, duration):
    if timer <= current_time:
        bullet_speed.y = 350
    
    if duration <= current_time:
        bullet_vel = 10
    else:
        bullet_vel = 15
    
    return bullet_vel





def powerup_shield(shield, timer, current_time, duration):
    if timer <= current_time:
        shield.y = 27.5
    
    if duration <= current_time:
        shield_status = False
    else:
        shield_status = True
    
    return shield_status





def t1_movement(map, keys_pressed, t1, obstacle_list, powerup_list, vel, t2, radiation_status, breakdown_status, hijack_status):

    #Power-Ups
    for powerup in powerup_list:
        if t1.colliderect(powerup.getRect()) and powerup.getName() == "Speed Boost":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t1_speed_up_hit))
        elif t1.colliderect(powerup.getRect()) and powerup.getName() == "Shield":
            powerup.getRect().y = -50
            pygame.event.post(pygame.event.Event(t1_shield_hit))
        elif t1.colliderect(powerup.getRect()) and powerup.getName() == "Radiation":
            powerup.getRect().y = -50
            pygame.event.post(pygame.event.Event(t1_radiation_hit))
        elif t1.colliderect(powerup.getRect()) and powerup.getName() == "Breakdown":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t1_breakdown_hit))
        elif t1.colliderect(powerup.getRect()) and powerup.getName() == "Hijack":
            powerup.getRect().y = -50
            pygame.event.post(pygame.event.Event(t1_hijack_hit))
        elif t1.colliderect(powerup.getRect()) and powerup.getName() == "Virus":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t1_virus_hit))
        elif t1.colliderect(powerup.getRect()) and powerup.getName() == "Infinite Ammo":
            powerup.getRect().y = -50
            pygame.event.post(pygame.event.Event(t1_infiniteammo_hit))
        elif t1.colliderect(powerup.getRect()) and powerup.getName() == "Speed Bullets":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t1_speedbullets_hit))

    #Movement
    if not hijack_status:
        if not breakdown_status:
            if keys_pressed[pygame.K_a] and (t1.x > 0):
                t1.x -= vel
                for obstacle in obstacle_list:
                    if t1.colliderect(obstacle.getRect()):
                        t1.x += vel
            if keys_pressed[pygame.K_d] and (t1.x + 40 < 900):
                t1.x += vel
                for obstacle in obstacle_list:
                    if t1.colliderect(obstacle.getRect()):
                        t1.x -= vel
            if keys_pressed[pygame.K_w] and (t1.y > 0):
                t1.y -= vel
                for obstacle in obstacle_list:
                    if t1.colliderect(obstacle.getRect()):
                        t1.y += vel
            if keys_pressed[pygame.K_s] and (t1.y + 30 < 500):
                t1.y += vel
                for obstacle in obstacle_list:
                    if t1.colliderect(obstacle.getRect()):
                        t1.y -= vel
    else:
        if keys_pressed[pygame.K_d] and (t1.x > 0):
            t1.x -= vel
            for obstacle in obstacle_list:
                if t1.colliderect(obstacle.getRect()):
                    t1.x += vel
        if keys_pressed[pygame.K_a] and (t1.x + 40 < 900):
            t1.x += vel
            for obstacle in obstacle_list:
                if t1.colliderect(obstacle.getRect()):
                    t1.x -= vel
        if keys_pressed[pygame.K_s] and (t1.y > 0):
            t1.y -= vel
            for obstacle in obstacle_list:
                if t1.colliderect(obstacle.getRect()):
                    t1.y += vel
        if keys_pressed[pygame.K_w] and (t1.y + 30 < 500):
            t1.y += vel
            for obstacle in obstacle_list:
                if t1.colliderect(obstacle.getRect()):
                    t1.y -= vel

    if map == "map2" and t1.colliderect(t2) and radiation_status:
        pygame.event.post(pygame.event.Event(t2_hit))





def t2_movement(map, keys_pressed, t2, obstacle_list, powerup_list, vel, t1, radiation_status, breakdown_status, hijack_status):

    #Power-Ups
    for powerup in powerup_list:
        if t2.colliderect(powerup.getRect()) and powerup.getName() == "Speed Boost":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t2_speed_up_hit))
        elif t2.colliderect(powerup.getRect()) and powerup.getName() == "Shield":
            powerup.getRect().y = -50
            pygame.event.post(pygame.event.Event(t2_shield_hit))
        elif t2.colliderect(powerup.getRect()) and powerup.getName() == "Radiation":
            powerup.getRect().y = -50
            pygame.event.post(pygame.event.Event(t2_radiation_hit))
        elif t2.colliderect(powerup.getRect()) and powerup.getName() == "Breakdown":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t2_breakdown_hit))
        elif t2.colliderect(powerup.getRect()) and powerup.getName() == "Hijack":
            powerup.getRect().y = -50
            pygame.event.post(pygame.event.Event(t2_hijack_hit))
        elif t2.colliderect(powerup.getRect()) and powerup.getName() == "Virus":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t2_virus_hit))
        elif t2.colliderect(powerup.getRect()) and powerup.getName() == "Infinite Ammo":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t2_infiniteammo_hit))
        elif t2.colliderect(powerup.getRect()) and powerup.getName() == "Speed Bullets":
            powerup.getRect().y = 550
            pygame.event.post(pygame.event.Event(t2_speedbullets_hit))

    #Movement
    if not hijack_status:
        if not breakdown_status:
            if keys_pressed[pygame.K_LEFT] and (t2.x > 0):
                t2.x -= vel
                for obstacle in obstacle_list:
                    if t2.colliderect(obstacle.getRect()):
                        t2.x += vel
            if keys_pressed[pygame.K_RIGHT] and (t2.x + 40 < 900):
                t2.x += vel
                for obstacle in obstacle_list:
                    if t2.colliderect(obstacle.getRect()):
                        t2.x -= vel
            if keys_pressed[pygame.K_UP] and (t2.y > 0):
                t2.y -= vel
                for obstacle in obstacle_list:
                    if t2.colliderect(obstacle.getRect()):
                        t2.y += vel
            if keys_pressed[pygame.K_DOWN] and (t2.y + 30 < 500):
                t2.y += vel
                for obstacle in obstacle_list:
                    if t2.colliderect(obstacle.getRect()):
                        t2.y -= vel
    else:
        if keys_pressed[pygame.K_RIGHT] and (t2.x > 0):
            t2.x -= vel
            for obstacle in obstacle_list:
                if t2.colliderect(obstacle.getRect()):
                    t2.x += vel
        if keys_pressed[pygame.K_LEFT] and (t2.x + 40 < 900):
            t2.x += vel
            for obstacle in obstacle_list:
                if t2.colliderect(obstacle.getRect()):
                    t2.x -= vel
        if keys_pressed[pygame.K_DOWN] and (t2.y > 0):
            t2.y -= vel
            for obstacle in obstacle_list:
                if t2.colliderect(obstacle.getRect()):
                    t2.y += vel
        if keys_pressed[pygame.K_UP] and (t2.y + 30 < 500):
            t2.y += vel
            for obstacle in obstacle_list:
                if t2.colliderect(obstacle.getRect()):
                    t2.y -= vel

    if map == "map2" and t2.colliderect(t1) and radiation_status:
        pygame.event.post(pygame.event.Event(t1_hit))





def map1_powerups(t1, t2, speed_boost, shield, t1_shield_status, t2_shield_status, t1_speed_status, t2_speed_status, t1_speed_duration, t1_shield_duration, t2_speed_duration, t2_shield_duration):

    if t1_shield_status and t1_shield_duration >= t1_speed_duration:
        WIN.blit(pygame.transform.scale(shield.getImage(), (20, 20)), (t1.x + 5, t1.y + 1))

    if t1_speed_status == 2 and t1_speed_duration >= t1_shield_duration:
        WIN.blit(pygame.transform.scale(speed_boost.getImage(), (20, 20)), (t1.x + 5, t1.y + 1))

    if t2_shield_status and t2_shield_duration >= t2_speed_duration:
        WIN.blit(pygame.transform.scale(shield.getImage(), (20, 20)), (t2.x + 7, t2.y + 1))

    if t2_speed_status == 2 and t2_speed_duration >= t2_shield_duration:
        WIN.blit(pygame.transform.scale(speed_boost.getImage(), (20, 20)), (t2.x + 7, t2.y + 1))    
    




def map2_powerups(t1, t2, radiation, t1_radiation_status, t2_radiation_status, t1_radiation_duration, t2_radiation_duration, breakdown, t1_breakdown_status, t2_breakdown_status, t1_breakdown_duration, t2_breakdown_duration):

    if t1_radiation_status and t1_radiation_duration >= t1_breakdown_duration:
        WIN.blit(pygame.transform.scale(radiation.getImage(), (20, 20)), (t1.x + 3, t1.y - 1))

    if t2_radiation_status and t2_radiation_duration >= t2_breakdown_duration:
        WIN.blit(pygame.transform.scale(radiation.getImage(), (20, 20)), (t2.x + 7, t2.y - 1))

    if t1_breakdown_status and t1_breakdown_duration >= t1_radiation_duration:
        WIN.blit(pygame.transform.scale(breakdown.getImage(), (20, 20)), (t2.x + 7, t2.y - 1))

    if t2_breakdown_status and t2_breakdown_duration >= t2_radiation_duration:
        WIN.blit(pygame.transform.scale(breakdown.getImage(), (20, 20)), (t1.x + 3, t1.y - 1))





def map3_powerups(t1, t2, infinite_ammo, t1_infiniteammo_status, t2_infiniteammo_status, t1_infiniteammo_duration, t2_infiniteammo_duration, speed_bullets, t1_speedbullet_status, t2_speedbullet_status, t1_bulletspeedup_duration, t2_bulletspeedup_duration):
    
    if t1_infiniteammo_status and t1_infiniteammo_duration >= t1_bulletspeedup_duration:
        WIN.blit(pygame.transform.scale(infinite_ammo.getImage(), (20, 20)), (t1.x + 5, t1.y + 1))

    if t1_speedbullet_status == 15 and t1_bulletspeedup_duration >= t1_infiniteammo_duration:
        WIN.blit(pygame.transform.scale(speed_bullets.getImage(), (20, 20)), (t1.x + 5, t1.y + 1))

    if t2_infiniteammo_status and t2_infiniteammo_duration >= t2_bulletspeedup_duration:
        WIN.blit(pygame.transform.scale(infinite_ammo.getImage(), (20, 20)), (t2.x + 7, t2.y + 1))

    if t2_speedbullet_status == 15 and t2_bulletspeedup_duration >= t2_infiniteammo_duration:
        WIN.blit(pygame.transform.scale(speed_bullets.getImage(), (20, 20)), (t2.x + 7, t2.y + 1))  





def map4_powerups(t1, t2, hijack, t1_hijack_status, t2_hijack_status, t1_hijack_duration, t2_hijack_duration, virus, t1_virus_status, t2_virus_status, t1_virus_duration, t2_virus_duration):
    
    if t1_hijack_status and t1_hijack_duration >= t1_virus_duration:
        WIN.blit(pygame.transform.scale(hijack.getImage(), (20, 20)), (t2.x + 7, t2.y - 1))

    if t2_hijack_status and t2_hijack_duration >= t2_virus_duration:
        WIN.blit(pygame.transform.scale(hijack.getImage(), (20, 20)), (t1.x + 3, t1.y - 1))

    if t1_virus_status and t1_virus_duration >= t1_hijack_duration:
        WIN.blit(pygame.transform.scale(virus.getImage(), (20, 20)), (t2.x + 7, t2.y - 1))

    if t2_virus_status and t2_virus_duration >= t2_hijack_duration:
        WIN.blit(pygame.transform.scale(virus.getImage(), (20, 20)), (t1.x + 3, t1.y - 1))





def draw_map1_items(t1, t2, t1_bullets, t2_bullets, BG, obstacle_list, shelter_list, powerup_list, curr_time, shield_timer, speedup_timer, t1_shield_duration, t2_shield_duration, t1_speedup_duration, t2_speedup_duration, tank_images, bullet_images):
    
    #Tanks
    WIN.blit(BG, (0, 0))
    WIN.blit(tank_images[0], (t1.x, t1.y - 4))
    WIN.blit(tank_images[1], (t2.x - 9, t2.y - 4))

    #Powerups
    for powerup in powerup_list:
        WIN.blit(powerup.getImage(), powerup.getRect())
    map1_powerups(t1, t2, powerup_list[0], powerup_list[1], powerup_shield(powerup_list[1].getRect(), shield_timer, curr_time, t1_shield_duration), powerup_shield(powerup_list[1].getRect(), shield_timer, curr_time, t2_shield_duration), powerup_speed(powerup_list[0].getRect(), speedup_timer, curr_time, t1_speedup_duration), powerup_speed(powerup_list[0].getRect(), speedup_timer, curr_time, t2_speedup_duration), t1_speedup_duration, t1_shield_duration, t2_speedup_duration, t2_shield_duration)

    #Obstacles
    for obstacle in obstacle_list:
        if obstacle.getName() == "L_barrierTL_V" or obstacle.getName() == "L_barrierTR_V":
            WIN.blit(obstacle.getImage(), (obstacle.getRect().x, obstacle.getRect().y + 50))
        else:
            WIN.blit(obstacle.getImage(), obstacle.getRect())

    #Bullets
    for bullet in t1_bullets:
        WIN.blit(bullet_images[0], (bullet.x - 2, bullet.y - 14))

    for bullet in t2_bullets:
        WIN.blit(bullet_images[1], (bullet.x, bullet.y - 14))

    for bullet in t1_rebounded:
        WIN.blit(bullet_images[1], (bullet.x, bullet.y - 14))

    for bullet in t2_rebounded:
        WIN.blit(bullet_images[0], (bullet.x - 2, bullet.y - 14))
    
    #Shelters
    for shelter in shelter_list:
        WIN.blit(shelter.getImage(), shelter.getRect())





def draw_map2_items(t1, t2, t1_bullets, t2_bullets, BG, shelters, tanks, SHIPYARD, bullet_images, powerup_list, curr_time, radiation_timer, t1_radiation_duration, t2_radiation_duration, t1_breakdown_duration, t2_breakdown_duration, breakdown_timer):
    
    #Background
    WIN.blit(BG, (0, 0))
    
    #Tanks
    WIN.blit(tanks[0], (t1.x - 4, t1.y - 21))
    WIN.blit(tanks[1], (t2.x - 6, t2.y - 20))

    #Powerups
    for powerup in powerup_list:
        WIN.blit(powerup.getImage(), powerup.getRect())
    map2_powerups(t1, t2, powerup_list[0], powerup_radiation(powerup_list[0], radiation_timer, curr_time, t1_radiation_duration), powerup_radiation(powerup_list[0], radiation_timer, curr_time, t2_radiation_duration), t1_radiation_duration, t2_radiation_duration, powerup_list[1], powerup_breakdown(powerup_list[1], breakdown_timer, curr_time, t1_breakdown_duration), powerup_breakdown(powerup_list[1], breakdown_timer, curr_time, t2_breakdown_duration), t1_breakdown_duration, t2_breakdown_duration)

    #Obstacles
    WIN.blit(SHIPYARD, (100, 125))
    WIN.blit(SHIPYARD, (675, 125))

    #Bullets
    for bullet in t1_bullets:
        WIN.blit(bullet_images[0], (bullet.x, bullet.y - 1))

    for bullet in t2_bullets:
        WIN.blit(bullet_images[1], (bullet.x, bullet.y))

    for bullet in t1_rebounded:
        WIN.blit(bullet_images[1], (bullet.x, bullet.y))

    for bullet in t2_rebounded:
        WIN.blit(bullet_images[0], (bullet.x - 2, bullet.y - 1))
    
    #Shelters
    for shelter in shelters:
        WIN.blit(shelter.getImage(), shelter.getRect())
    




def draw_map3_items(t1, t2, t1_bullets, t2_bullets, BG, frame, SHIP, islands, powerup_list, tanks, bullet_images, curr_time, bullet_speedup_timer, t1_bulletspeedup_duration, t2_bulletspeedup_duration, infinite_ammo_timer, t1_infiniteammo_duration, t2_infiniteammo_duration):
    
    #Background
    WIN.blit(BG[frame], (0, 0))

    #Islands
    WIN.blit(islands[0], (100, 150))
    WIN.blit(islands[1], (600, 150))

    #Tanks
    WIN.blit(tanks[0], (t1.x - 2, t1.y - 7))
    WIN.blit(tanks[1], (t2.x - 5, t2.y - 7))

    #Powerups
    for powerup in powerup_list:
        WIN.blit(powerup.getImage(), powerup.getRect())
    map3_powerups(t1, t2, powerup_list[0], powerup_infiniteammo(powerup_list[0], infinite_ammo_timer, curr_time, t1_infiniteammo_duration), powerup_infiniteammo(powerup_list[0], infinite_ammo_timer, curr_time, t2_infiniteammo_duration), t1_infiniteammo_duration, t2_infiniteammo_duration, powerup_list[1], powerup_speedbullet(powerup_list[1], bullet_speedup_timer, curr_time, t1_bulletspeedup_duration), powerup_speedbullet(powerup_list[1], bullet_speedup_timer, curr_time, t2_bulletspeedup_duration), t1_bulletspeedup_duration, t2_bulletspeedup_duration)

    #Obstacles
    WIN.blit(SHIP, (297, 49))
    WIN.blit(pygame.transform.rotate(SHIP, 180), (298, 389))

    #Bullets
    for bullet in t1_bullets:
        WIN.blit(bullet_images[0], (bullet.x, bullet.y - 2))

    for bullet in t2_bullets:
        WIN.blit(bullet_images[1], (bullet.x - 2, bullet.y - 1))

    for bullet in t1_rebounded:
        WIN.blit(bullet_images[1], (bullet.x - 2, bullet.y - 1))

    for bullet in t2_rebounded:
        WIN.blit(bullet_images[0], (bullet.x, bullet.y - 2))





def draw_map4_items(t1, t2, t1_bullets, t2_bullets, BG, obstacles, shelters, powerup_list, tanks, bullet_images, curr_time, hijack_timer, t1_hijack_duration, t2_hijack_duration, virus_timer, t1_virus_duration, t2_virus_duration):
    
    #Background
    WIN.blit(BG, (0,0))

    #Shelters
    for shelter in shelters:
        WIN.blit(shelter.getImage(), shelter.getRect())

    #Tanks
    WIN.blit(tanks[0], (t1.x - 4, t1.y - 4))
    WIN.blit(tanks[1], (t2.x - 5, t2.y - 4))

    #Powerups
    for powerup in powerup_list:
        WIN.blit(powerup.getImage(), powerup.getRect())
    map4_powerups(t1, t2, powerup_list[0], powerup_hijack(powerup_list[0], hijack_timer, curr_time, t1_hijack_duration), powerup_hijack(powerup_list[0], hijack_timer, curr_time, t2_hijack_duration), t1_hijack_duration, t2_hijack_duration, powerup_list[1], powerup_virus(powerup_list[1], virus_timer, curr_time, t1_virus_duration), powerup_virus(powerup_list[1], virus_timer, curr_time, t2_virus_duration), t1_virus_duration, t2_virus_duration)

    #Obstacles
    for obstacle in obstacles:
        if obstacle.getName() != None:
            WIN.blit(obstacle.getImage(), obstacle.getRect())

    #Bullets
    for bullet in t1_bullets:
        WIN.blit(bullet_images[0], (bullet.x - 6, bullet.y - 10))

    for bullet in t2_bullets:
        WIN.blit(bullet_images[1], (bullet.x - 7, bullet.y - 10))

    for bullet in t1_rebounded:
        WIN.blit(bullet_images[1], (bullet.x - 7, bullet.y - 10))

    for bullet in t2_rebounded:
        WIN.blit(bullet_images[0], (bullet.x - 6, bullet.y - 10))





def map1_bullet_handler(t1_bullets, t2_bullets, t1, t2, obstacle_list, t1_shield, t2_shield):

    VEL = 10

    for bullet in t1_bullets:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x += VEL
            if t2.colliderect(bullet) and not t2_shield:
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet) and t2_shield:
                t1_bullets.remove(bullet)
            
            if bullet.x > 900:
                t1_bullets.remove(bullet)
        elif rebound:
            rebound_sound.play()
            bullet.x -= VEL
            t1_rebounded.append(bullet)
            t1_bullets.remove(bullet)

    for bullet in t1_rebounded:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x -= VEL
            if t1.colliderect(bullet) and not t1_shield:
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet) and t1_shield:
                t1_rebounded.remove(bullet)
            
            if t2.colliderect(bullet) and not t2_shield:
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet) and t2_shield:
                t1_rebounded.remove(bullet)
            
            if bullet.x < 0:
                t1_rebounded.remove(bullet)
        elif rebound:
            rebound_sound.play()
            t1_rebounded.remove(bullet)

    for bullet in t2_bullets:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x -= VEL
            if t1.colliderect(bullet) and not t1_shield:
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet) and t1_shield:
                t2_bullets.remove(bullet)
            
            if bullet.x < 0:
                t2_bullets.remove(bullet)
        elif rebound:
            rebound_sound.play()
            bullet.x += VEL
            t2_rebounded.append(bullet)
            t2_bullets.remove(bullet)

    for bullet in t2_rebounded:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x += VEL
            if t2.colliderect(bullet) and not t2_shield:
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet) and t2_shield:
                t2_rebounded.remove(bullet)
            
            if t1.colliderect(bullet) and not t1_shield:
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet) and t1_shield:
                t2_rebounded.remove(bullet)
            
            if bullet.x < 0:
                t2_rebounded.remove(bullet)
        elif rebound:
            rebound_sound.play()
            t2_rebounded.remove(bullet)





def map2_bullet_handler(t1_bullets, t2_bullets, t1, t2, obstacle_list):

    VEL = 10

    for bullet in t1_bullets:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x += VEL
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t1_bullets.remove(bullet)
            
            if bullet.x > 900:
                t1_bullets.remove(bullet)
        elif rebound:
            rebound_sound.play()
            bullet.x -= VEL
            t1_rebounded.append(bullet)
            t1_bullets.remove(bullet)

    for bullet in t1_rebounded:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x -= VEL
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t1_rebounded.remove(bullet)
            
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t1_rebounded.remove(bullet)
            
            if bullet.x < 0:
                t1_rebounded.remove(bullet)
        elif rebound:
            rebound_sound.play()
            t1_rebounded.remove(bullet)

    for bullet in t2_bullets:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x -= VEL
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t2_bullets.remove(bullet)
            
            if bullet.x < 0:
                t2_bullets.remove(bullet)
        elif rebound:
            rebound_sound.play()
            bullet.x += VEL
            t2_rebounded.append(bullet)
            t2_bullets.remove(bullet)

    for bullet in t2_rebounded:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x += VEL
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t2_rebounded.remove(bullet)
            
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t2_rebounded.remove(bullet)
            
            if bullet.x < 0:
                t2_rebounded.remove(bullet)
        elif rebound:
            rebound_sound.play()
            t2_rebounded.remove(bullet)





def map3_bullet_handler(t1_bullets, t2_bullets, t1, t2, obstacle_list, t1_bullet_vel, t2_bullet_vel):

    T1_VEL = t1_bullet_vel
    T2_VEL = t2_bullet_vel

    for bullet in t1_bullets:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()) and obstacle.getName() == None:
                rebound = True

        if not rebound:
            bullet.x += T1_VEL
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t1_bullets.remove(bullet)
            
            if bullet.x > 900:
                t1_bullets.remove(bullet)
        elif rebound:
            rebound_sound.play()
            bullet.x -= T1_VEL
            t1_rebounded.append(bullet)
            t1_bullets.remove(bullet)

    for bullet in t1_rebounded:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()) and obstacle.getName() == None:
                rebound = True

        if not rebound:
            bullet.x -= T1_VEL
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t1_rebounded.remove(bullet)
            
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t1_rebounded.remove(bullet)
            
            if bullet.x < 0:
                t1_rebounded.remove(bullet)
        elif rebound:
            rebound_sound.play()
            t1_rebounded.remove(bullet)

    for bullet in t2_bullets:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()) and obstacle.getName() == None:
                rebound = True

        if not rebound:
            bullet.x -= T2_VEL
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t2_bullets.remove(bullet)
            
            if bullet.x < 0:
                t2_bullets.remove(bullet)
        elif rebound:
            rebound_sound.play()
            bullet.x += T2_VEL
            t2_rebounded.append(bullet)
            t2_bullets.remove(bullet)

    for bullet in t2_rebounded:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()) and obstacle.getName() == None:
                rebound = True

        if not rebound:
            bullet.x += T2_VEL
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t2_rebounded.remove(bullet)
            
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t2_rebounded.remove(bullet)
            
            if bullet.x < 0:
                t2_rebounded.remove(bullet)
        elif rebound:
            rebound_sound.play()
            t2_rebounded.remove(bullet)





def map4_bullet_handler(t1_bullets, t2_bullets, t1, t2, obstacle_list):

    VEL = 10

    for bullet in t1_bullets:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x += VEL
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t1_bullets.remove(bullet)
            
            if bullet.x > 900:
                t1_bullets.remove(bullet)
        elif rebound:
            rebound_sound.play()
            bullet.x -= VEL
            t1_rebounded.append(bullet)
            t1_bullets.remove(bullet)

    for bullet in t1_rebounded:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x -= VEL
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t1_rebounded.remove(bullet)
            
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t1_rebounded.remove(bullet)
            
            if bullet.x < 0:
                t1_rebounded.remove(bullet)
        elif rebound:
            rebound_sound.play()
            t1_rebounded.remove(bullet)

    for bullet in t2_bullets:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x -= VEL
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t2_bullets.remove(bullet)
            
            if bullet.x < 0:
                t2_bullets.remove(bullet)
        elif rebound:
            rebound_sound.play()
            bullet.x += VEL
            t2_rebounded.append(bullet)
            t2_bullets.remove(bullet)

    for bullet in t2_rebounded:

        rebound = False

        for obstacle in obstacle_list:
            if bullet.colliderect(obstacle.getRect()):
                rebound = True

        if not rebound:
            bullet.x += VEL
            if t2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t2_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t2.colliderect(bullet):
                t2_rebounded.remove(bullet)
            
            if t1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(t1_hit))
                t1_bullets.clear()
                t2_bullets.clear()
                t1_rebounded.clear()
                t2_rebounded.clear()
            elif t1.colliderect(bullet):
                t2_rebounded.remove(bullet)
            
            if bullet.x < 0:
                t2_rebounded.remove(bullet)
        elif rebound:
            rebound_sound.play()
            t2_rebounded.remove(bullet)





def draw_winner(text, map):
    WINNER_FONT = pygame.font.Font('Fonts/Boxy-Bold.ttf', 50)
    if map == "map1":
        draw_text = WINNER_FONT.render(text, True, BLACK)
    elif map == "map2":
        draw_text = WINNER_FONT.render(text, True, WHITE)
    elif map == "map3":
        draw_text = WINNER_FONT.render(text, True, BLACK)
    elif map == "map4":
        draw_text = WINNER_FONT.render(text, True, WHITE)
    WIN.blit(draw_text, (450 - draw_text.get_width()/2, 250 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)






def game(run):
    global t1_total_wins, t2_total_wins
    
    pygame.display.set_caption("Tank Wars")

    #Tanks
    if run[1] == "map1":
        t1 = pygame.Rect(80, 235, h - 8, w - 7)
        t2 = pygame.Rect(800, 235, h - 8, w - 7)
    elif run[1] == "map2":
        t1 = pygame.Rect(50, 235, h - 9, w - 10)
        t2 = pygame.Rect(819, 235, h - 9, w - 10)
    elif run[1] == "map3":
        t1 = pygame.Rect(50, 235, h - 9, w - 10)
        t2 = pygame.Rect(830, 235, h - 9, w - 10)
    elif run[1] == "map4":
        t1 = pygame.Rect(80, 235, h - 8, w - 7)
        t2 = pygame.Rect(800, 235, h - 8, w - 7)

    #Bullets
    t1_bullets = []
    t2_bullets = []

    #Stats
    stats_list = []
    t1_bullets_fired = 0
    t2_bullets_fired = 0
    game_start = time.time()
    
    #Power-Up Timers
    speedup_timer = 0
    shield_timer = 0
    radiation_timer = 0
    breakdown_timer = 0
    hijack_timer = 0
    virus_timer = 0
    bullet_speedup_timer = 0
    infinite_ammo_timer = 0

    t1_speedup_duration = 0
    t2_speedup_duration = 0
    t1_shield_duration = 0
    t2_shield_duration = 0
    t1_radiation_duration = 0
    t2_radiation_duration = 0
    t1_breakdown_duration = 0
    t2_breakdown_duration = 0
    t1_hijack_duration = 0
    t2_hijack_duration = 0
    t1_virus_duration = 0
    t2_virus_duration = 0
    t1_bulletspeedup_duration = 0
    t2_bulletspeedup_duration = 0
    t1_infiniteammo_duration = 0
    t2_infiniteammo_duration = 0

    t1_virus_status = False
    t2_virus_status = False
    t1_infiniteammo_status = False
    t2_infiniteammo_status = False

    #Clock
    clock = pygame.time.Clock()
    frame = 0

    while run[0]:

        #Clock
        clock.tick(FPS)
        curr_time = pygame.time.get_ticks()
        
        #Event Handler
        for event in pygame.event.get():
            
            #Bullets
            if event.type == pygame.KEYDOWN:
                
                if not t2_infiniteammo_status:
                    if (event.key == pygame.K_RALT) and (len(t2_bullets) < 3) and not t1_virus_status:
                        if run[1] == "map1":
                            classic_bullet_sound.play()
                            bullet = pygame.Rect(t2.x - 30, t2.y + 7, 23, 8)
                        elif run[1] == "map2":
                            space_bullet_sound.play()
                            bullet = pygame.Rect(t2.x - 27, t2.y + 7, 23, 8)
                        elif run[1] == "map3":
                            marine_bullet_sound.play()
                            bullet = pygame.Rect(t2.x - 21, t2.y + 7, 23, 8)
                        elif run[1] == "map4":
                            cyber_bullet_sound.play()
                            bullet = pygame.Rect(t2.x - 21, t2.y + 8, 23, 8)
                        t2_bullets_fired += 1
                        t2_bullets.append(bullet)
                elif t2_infiniteammo_status:
                    if (event.key == pygame.K_RALT) and not t1_virus_status:
                        if run[1] == "map1":
                            classic_bullet_sound.play()
                            bullet = pygame.Rect(t2.x - 30, t2.y + 7, 23, 8)
                        elif run[1] == "map2":
                            space_bullet_sound.play()
                            bullet = pygame.Rect(t2.x - 27, t2.y + 7, 23, 8)
                        elif run[1] == "map3":
                            marine_bullet_sound.play()
                            bullet = pygame.Rect(t2.x - 21, t2.y + 7, 23, 8)
                        elif run[1] == "map4":
                            cyber_bullet_sound.play()
                            bullet = pygame.Rect(t2.x - 21, t2.y + 8, 23, 8)
                        t2_bullets_fired += 1
                        t2_bullets.append(bullet)

                if not t1_infiniteammo_status:
                    if (event.key == pygame.K_LALT) and (len(t1_bullets) < 3) and not t2_virus_status:
                        if run[1] == "map1":
                            classic_bullet_sound.play()
                            bullet = pygame.Rect(t1.x + 40, t1.y + 7, 23, 8)
                        elif run[1] == "map2":
                            space_bullet_sound.play()
                            bullet = pygame.Rect(t1.x + 37, t1.y + 6, 23, 8)
                        elif run[1] == "map3":
                            marine_bullet_sound.play()
                            bullet = pygame.Rect(t1.x + 31, t1.y + 6, 23, 8)
                        elif run[1] == "map4":
                            cyber_bullet_sound.play()
                            bullet = pygame.Rect(t1.x + 31, t1.y + 7, 23, 8)
                        t1_bullets_fired += 1
                        t1_bullets.append(bullet)
                elif t1_infiniteammo_status:
                    if (event.key == pygame.K_LALT) and not t2_virus_status:
                        if run[1] == "map1":
                            classic_bullet_sound.play()
                            bullet = pygame.Rect(t1.x + 40, t1.y + 7, 23, 8)
                        elif run[1] == "map2":
                            space_bullet_sound.play()
                            bullet = pygame.Rect(t1.x + 37, t1.y + 6, 23, 8)
                        elif run[1] == "map3":
                            marine_bullet_sound.play()
                            bullet = pygame.Rect(t1.x + 31, t1.y + 6, 23, 8)
                        elif run[1] == "map4":
                            cyber_bullet_sound.play()
                            bullet = pygame.Rect(t1.x + 31, t1.y + 7, 23, 8)
                        t1_bullets_fired += 1
                        t1_bullets.append(bullet)

            #Power-Ups
            if event.type == t1_speed_up_hit:
                powerup_sound.play()
                t1_speedup_duration = pygame.time.get_ticks() + run[5][0].getDuration()
                speedup_timer = pygame.time.get_ticks() + 20000

            if event.type == t2_speed_up_hit:
                powerup_sound.play()
                t2_speedup_duration = pygame.time.get_ticks() + run[5][0].getDuration()
                speedup_timer = pygame.time.get_ticks() + 20000

            if event.type == t1_shield_hit:
                powerup_sound.play()
                t1_shield_duration = pygame.time.get_ticks() + run[5][1].getDuration()
                shield_timer = pygame.time.get_ticks() + 20000

            if event.type == t2_shield_hit:
                powerup_sound.play()
                t2_shield_duration = pygame.time.get_ticks() + run[5][1].getDuration()
                shield_timer = pygame.time.get_ticks() + 20000

            if event.type == t1_radiation_hit:
                powerup_sound.play()
                t1_radiation_duration = pygame.time.get_ticks() + run[5][0].getDuration()
                radiation_timer = pygame.time.get_ticks() + 25000

            if event.type == t2_radiation_hit:
                powerup_sound.play()
                t2_radiation_duration = pygame.time.get_ticks() + run[5][0].getDuration()
                radiation_timer = pygame.time.get_ticks() + 25000

            if event.type == t1_breakdown_hit:
                powerup_sound.play()
                t1_breakdown_duration = pygame.time.get_ticks() + run[5][1].getDuration()
                breakdown_timer = pygame.time.get_ticks() + 15000
            
            if event.type == t2_breakdown_hit:
                powerup_sound.play()
                t2_breakdown_duration = pygame.time.get_ticks() + run[5][1].getDuration()
                breakdown_timer = pygame.time.get_ticks() + 15000

            if event.type == t1_hijack_hit:
                powerup_sound.play()
                t1_hijack_duration = pygame.time.get_ticks() + run[5][0].getDuration()
                hijack_timer = pygame.time.get_ticks() + 20000

            if event.type == t2_hijack_hit:
                powerup_sound.play()
                t2_hijack_duration = pygame.time.get_ticks() + run[5][0].getDuration()
                hijack_timer = pygame.time.get_ticks() + 20000
            
            if event.type == t1_virus_hit:
                powerup_sound.play()
                t1_virus_duration = pygame.time.get_ticks() + run[5][1].getDuration()
                virus_timer = pygame.time.get_ticks() + 15000

            if event.type == t2_virus_hit:
                powerup_sound.play()
                t2_virus_duration = pygame.time.get_ticks() + run[5][1].getDuration()
                virus_timer = pygame.time.get_ticks() + 15000
            
            if event.type == t1_infiniteammo_hit:
                powerup_sound.play()
                t1_infiniteammo_duration = pygame.time.get_ticks() + run[5][0].getDuration()
                infinite_ammo_timer = pygame.time.get_ticks() + 15000

            if event.type == t2_infiniteammo_hit:
                powerup_sound.play()
                t2_infiniteammo_duration = pygame.time.get_ticks() + run[5][0].getDuration()
                infinite_ammo_timer = pygame.time.get_ticks() + 15000
            
            if event.type == t1_speedbullets_hit:
                powerup_sound.play()
                t1_bulletspeedup_duration = pygame.time.get_ticks() + run[5][1].getDuration()
                bullet_speedup_timer = pygame.time.get_ticks() + 15000

            if event.type == t2_speedbullets_hit:
                powerup_sound.play()
                t2_bulletspeedup_duration = pygame.time.get_ticks() + run[5][1].getDuration()
                bullet_speedup_timer = pygame.time.get_ticks() + 15000

            winner_text = ""

            if event.type == t1_hit:
                print('Game Over')
                explosion.play()
                game_end = time.time()
                game_duration = game_start - game_end
                exp_rect = pygame.Rect(t1.x - 25, t1.y - 40, 150, 150)
                for exp in exp_list:
                    WIN.blit(pygame.transform.rotate(exp, 180), exp_rect) 
                    pygame.display.update()
                    pygame.time.delay(10)
                pygame.time.delay(500)
                winner_text = "Player 2 Wins"

            if event.type == t2_hit:
                print('Game Over')
                explosion.play()
                game_end = time.time()
                game_duration = game_end - game_start
                exp_rect = pygame.Rect(t2.x - 40, t2.y - 40, 150, 150)
                for exp in exp_list:
                    WIN.blit(exp, exp_rect) 
                    pygame.display.update()
                    pygame.time.delay(10)
                pygame.time.delay(500)
                winner_text = "Player 1 Wins"

            if winner_text != "":
                if winner_text == "Player 1 Wins":
                    t1_total_wins += 1
                elif winner_text == "Player 2 Wins":
                    t2_total_wins += 1

                draw_winner(winner_text, run[1])
                explosion.stop()
                stats_list.append(t1_bullets_fired)
                stats_list.append(t1_total_wins)
                stats_list.append(t2_bullets_fired)
                stats_list.append(t2_total_wins)
                stats_list.append(abs(int(game_duration)))
                stats_list.append(winner_text)
                playagain = play_again(WIN, stats_list)

                if playagain:
                    game(run)
                elif not playagain:
                    game(main_menu(WIN))
      
        keys_pressed = pygame.key.get_pressed()
        
        if run[1] == "map1":
            t1_movement(run[1], keys_pressed, t1, run[3], run[5], powerup_speed(run[5][0].getRect(), speedup_timer, curr_time, t1_speedup_duration), None, None, None, None)
            t2_movement(run[1], keys_pressed, t2, run[3], run[5], powerup_speed(run[5][0].getRect(), speedup_timer, curr_time, t2_speedup_duration), None, None, None, None)
            draw_map1_items(t1, t2, t1_bullets, t2_bullets, run[2], run[3], run[4], run[5], curr_time, shield_timer, speedup_timer, t1_shield_duration, t2_shield_duration, t1_speedup_duration, t2_speedup_duration, run[6], run[7])
            map1_bullet_handler(t1_bullets, t2_bullets, t1, t2, run[3], powerup_shield(run[5][1].getRect(), shield_timer, curr_time, t1_shield_duration), powerup_shield(run[5][1].getRect(), shield_timer, curr_time, t2_shield_duration))
        elif run[1] == "map2":
            t1_movement(run[1], keys_pressed, t1, run[3], run[5], 1, t2, powerup_radiation(run[5][0].getRect(), radiation_timer, curr_time, t1_radiation_duration), powerup_breakdown(run[5][1].getRect(), breakdown_timer, curr_time, t2_breakdown_duration), None)
            t2_movement(run[1], keys_pressed, t2, run[3], run[5], 1, t1, powerup_radiation(run[5][0].getRect(), radiation_timer, curr_time, t2_radiation_duration), powerup_breakdown(run[5][1].getRect(), breakdown_timer, curr_time, t1_breakdown_duration), None)
            draw_map2_items(t1, t2, t1_bullets, t2_bullets, run[2], run[4], run[6], run[7], run[8], run[5], curr_time, radiation_timer, t1_radiation_duration, t2_radiation_duration, t1_breakdown_duration, t2_breakdown_duration, breakdown_timer)
            map2_bullet_handler(t1_bullets, t2_bullets, t1, t2, run[3])     
        elif run[1] == "map3":
            t1_infiniteammo_status = powerup_infiniteammo(run[5][0].getRect(), infinite_ammo_timer, curr_time, t1_infiniteammo_duration)
            t2_infiniteammo_status = powerup_infiniteammo(run[5][0].getRect(), infinite_ammo_timer, curr_time, t2_infiniteammo_duration)
            t1_movement(run[1], keys_pressed, t1, run[3], run[5], 1, None, None, None, None)
            t2_movement(run[1], keys_pressed, t2, run[3], run[5], 1, None, None, None, None)
            draw_map3_items(t1, t2, t1_bullets, t2_bullets, run[2], frame, run[8], run[4], run[5], run[6], run[7], curr_time, bullet_speedup_timer, t1_bulletspeedup_duration, t2_bulletspeedup_duration, infinite_ammo_timer, t1_infiniteammo_duration, t2_infiniteammo_duration)
            map3_bullet_handler(t1_bullets, t2_bullets, t1, t2, run[3], powerup_speedbullet(run[5][1].getRect(), bullet_speedup_timer, curr_time, t1_bulletspeedup_duration), powerup_speedbullet(run[5][1].getRect(), bullet_speedup_timer, curr_time, t2_bulletspeedup_duration))
            if frame >= len(run[2]) - 1:
                frame = 0
            else:
                frame += 1
        elif run[1] == "map4":
            t1_virus_status = powerup_virus(run[5][1].getRect(), virus_timer, curr_time, t1_virus_duration)
            t2_virus_status = powerup_virus(run[5][1].getRect(), virus_timer, curr_time, t2_virus_duration)
            t1_movement(run[1], keys_pressed, t1, run[3], run[5], 1, None, None, None, powerup_hijack(run[5][0].getRect(), hijack_timer, curr_time, t2_hijack_duration))
            t2_movement(run[1], keys_pressed, t2, run[3], run[5], 1, None, None, None, powerup_hijack(run[5][0].getRect(), hijack_timer, curr_time, t1_hijack_duration))
            draw_map4_items(t1, t2, t1_bullets, t2_bullets, run[2], run[3], run[4], run[5], run[6], run[7], curr_time, hijack_timer, t1_hijack_duration, t2_hijack_duration, virus_timer, t1_virus_duration, t2_virus_duration)
            map4_bullet_handler(t1_bullets, t2_bullets, t1, t2, run[3])

        pygame.display.update()

if __name__ == "__main__":
    game(main_menu(WIN))
