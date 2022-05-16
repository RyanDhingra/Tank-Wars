import pygame
import sys
pygame.init()
pygame.mixer.init()

FPS = 60
WIDTH, HEIGHT = 900, 500
WHITE = (255,255,255)
GREY = (100,100,100)
TITLE_FONT = pygame.font.Font('Fonts/Stencil Regular.ttf', 60)
MISSIONREPORT_FONT = pygame.font.Font('Fonts/Stencil Regular.ttf', 35)
STATS_FONT = pygame.font.Font('Fonts/Stencil Regular.ttf', 20)
OPTIONS_FONT = pygame.font.Font('Fonts/Stencil Regular.ttf', 30)
TITLE_PANEL = pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (400, 100))
STATS_PANEL = pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (300, 200))
BUTTON_PANEL = pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (200, 50))
EXIT_PANEL = pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (100, 50))
BG = pygame.transform.scale(pygame.image.load("Backgrounds/GameoverBG.jpg"), (WIDTH, HEIGHT))

#Sounds
click_sound = pygame.mixer.Sound('Sounds/Click.wav')
click_sound.set_volume(0.07)





def draw_items(WIN, playagain, mainmenu, exit, playagain_text, mainmenu_text, exit_text, title, title_text, stats_plate, t1_bulletstats_text, t1_powerupstats_text, t2_bulletstats_text, t2_powerupstats_text, game_duration, winner_text, exit_colour, playagain_colour, mainmenu_colour):

    WIN.blit(BG, (0,0))
    WIN.blit(TITLE_PANEL, title)
    title_text = TITLE_FONT.render(title_text, True, WHITE)
    WIN.blit(title_text, (450 - title_text.get_width()/2, 80))
    
    WIN.blit(BUTTON_PANEL, playagain)
    playagain_text = OPTIONS_FONT.render(playagain_text, True, playagain_colour)
    WIN.blit(playagain_text, (250 - playagain_text.get_width()/2, 430))

    WIN.blit(BUTTON_PANEL, mainmenu)
    mainmenu_text = OPTIONS_FONT.render(mainmenu_text, True, mainmenu_colour)
    WIN.blit(mainmenu_text, (650 - mainmenu_text.get_width()/2, 430))
    
    WIN.blit(EXIT_PANEL, exit)
    exit_text = OPTIONS_FONT.render(exit_text, True, exit_colour)
    WIN.blit(exit_text, (450 - exit_text.get_width()/2, 430))

    WIN.blit(STATS_PANEL, stats_plate)

    if winner_text == "Player 1 Wins":
        t1_bulletstats_text = STATS_FONT.render(t1_bulletstats_text, True, WHITE)
        WIN.blit(t1_bulletstats_text, (450 - t1_bulletstats_text.get_width()/2, 270))
        t1_powerupstats_text = STATS_FONT.render(t1_powerupstats_text, True, WHITE)
        WIN.blit(t1_powerupstats_text, (450 - t1_powerupstats_text.get_width()/2, 300))
    
    elif winner_text == "Player 2 Wins":
        t2_bulletstats_text = STATS_FONT.render(t2_bulletstats_text, True, WHITE)
        WIN.blit(t2_bulletstats_text, (450 - t2_bulletstats_text.get_width()/2, 270))
        t2_powerupstats_text = STATS_FONT.render(t2_powerupstats_text, True, WHITE)
        WIN.blit(t2_powerupstats_text, (450 - t2_powerupstats_text.get_width()/2, 300))
    
    winner_text = MISSIONREPORT_FONT.render(winner_text, True, WHITE)
    WIN.blit(winner_text, (450 - winner_text.get_width()/2, 215))
    game_duration = STATS_FONT.render(game_duration, True, WHITE)
    WIN.blit(game_duration, (450 - game_duration.get_width()/2, 330))

    pygame.display.update()





def play_again(WIN, stats_list):

    pygame.display.set_caption("Game Over")

    #Rects
    title = pygame.Rect(250, 50, 400, 100)
    title_text = "Game Over"
    
    playagain_button = pygame.Rect(150, 415, 200, 50)
    playagain_text = "Play Again"
    playagain_colour = WHITE
    
    mainmenu_button = pygame.Rect(550, 415, 200, 50)
    mainmenu_text = "Main Menu"
    mainmenu_colour = WHITE
    
    exit_button = pygame.Rect(400, 415, 100, 50)
    exit_text = "Exit"
    exit_colour = WHITE

    stats_plate = pygame.Rect(300, 175, 300, 200)
    t1_bulletstats_text = "Bullets Fired: " + str(stats_list[0])
    t1_powerupstats_text = "Total Wins: " + str(stats_list[1])
    t2_bulletstats_text = "Bullets Fired: " + str(stats_list[2])
    t2_powerupstats_text = "Total Wins: " + str(stats_list[3])
    game_duration = "Game Duration: " + str(stats_list[4]) + "s"
    winner_text = stats_list[5]

    clock = pygame.time.Clock()
    run = True
    while run:
        
        #Clock
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()

        #Event Handler
        for event in pygame.event.get():        

            if exit_button.collidepoint(mouse[0], mouse[1]):
                exit_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    print("Game Exited")
                    click_sound.play()
                    run = False
                    pygame.quit()
                    sys.exit()
            else:
                exit_colour = WHITE 
                
            if playagain_button.collidepoint(mouse[0], mouse[1]):
                playagain_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    print("Game Started")
                    click_sound.play()
                    return True
            else:
                playagain_colour = WHITE

            if mainmenu_button.collidepoint(mouse[0], mouse[1]):
                mainmenu_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    print("Main Menu")
                    click_sound.play()
                    return False
            else:
                mainmenu_colour = WHITE

        draw_items(WIN, playagain_button, mainmenu_button, exit_button, playagain_text, mainmenu_text, exit_text, title, title_text, stats_plate, t1_bulletstats_text, t1_powerupstats_text, t2_bulletstats_text, t2_powerupstats_text, game_duration, winner_text, exit_colour, playagain_colour, mainmenu_colour)
