import pygame
import sys
from Help_Menu import help_menu
from Map_Select import map_select
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WHITE = (255,255,255)
GREY = (100,100,100)
BG = pygame.transform.scale(pygame.image.load("Backgrounds/MainMenuBG.jpg"), (WIDTH, HEIGHT))
TITLE_PANEL = pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (400, 100))
BUTTON_PANEL = pygame.transform.scale(pygame.image.load("Backgrounds/Text Panel.png"), (200, 75))
FPS = 60
TITLE_FONT = pygame.font.Font('Fonts/Stencil Regular.ttf', 60)
OPTIONS_FONT = pygame.font.Font('Fonts/Stencil Regular.ttf', 50)

start_game = pygame.USEREVENT + 1
help_window = pygame.USEREVENT + 2

#Sounds
click_sound = pygame.mixer.Sound('Sounds/Click.wav')
click_sound.set_volume(0.07)





def draw_items(WIN, BG, start, title_panel, title_text, help, exit, start_text, help_text, exit_text, start_colour, help_colour, exit_colour):
    WIN.blit(BG, (0,0))

    WIN.blit(TITLE_PANEL, title_panel)
    title_text = TITLE_FONT.render(title_text, True, WHITE)
    WIN.blit(title_text, (450 - title_text.get_width()/2, 80))
    
    WIN.blit(BUTTON_PANEL, start)
    start_text = OPTIONS_FONT.render(start_text, True, start_colour)
    WIN.blit(start_text, (450 - start_text.get_width()/2, 200))
    
    WIN.blit(BUTTON_PANEL, help)
    help_text = OPTIONS_FONT.render(help_text, True, help_colour)
    WIN.blit(help_text, (450 - help_text.get_width()/2, 300))
    
    WIN.blit(BUTTON_PANEL, exit)
    exit_text = OPTIONS_FONT.render(exit_text, True, exit_colour)
    WIN.blit(exit_text, (450 - exit_text.get_width()/2, 400))
    
    pygame.display.update()





def main_menu(WIN):

    pygame.display.set_caption("Main Menu")

    #Rects
    title = pygame.Rect(250, 50, 400, 100)
    title_text = "Tank Wars"
    start_button = pygame.Rect(350, 180, 200, 75)
    start_text = "Start"
    help_button = pygame.Rect(350, 280, 200, 75)
    help_text = "Help"
    exit_button = pygame.Rect(350, 380, 200, 75)
    exit_text = "Exit"

    start_colour = WHITE
    help_colour = WHITE
    exit_colour = WHITE

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
                    click_sound.play()
                    run = False
                    pygame.quit()
                    sys.exit()
            else:
                exit_colour = WHITE
            
            if start_button.collidepoint(mouse[0], mouse[1]):
                start_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    click_sound.play()
                    return map_select(WIN)
            else:
                start_colour = WHITE

            if help_button.collidepoint(mouse[0], mouse[1]):
                help_colour = GREY
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    click_sound.play()
                    help_menu()
            else:
                help_colour = WHITE

        draw_items(WIN, BG, start_button, title, title_text, help_button, exit_button, start_text, help_text, exit_text, start_colour, help_colour, exit_colour)