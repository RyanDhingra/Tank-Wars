from tkinter import *
from PIL import ImageTk, Image
import sys





def help_menu():

    def bg_resizer(event):
        global new_BG, BG_resized, BG_pic

        new_BG = Image.open('Backgrounds/Help Panel.png')
        BG_resized = new_BG.resize((event.width, event.height), Image.ANTIALIAS)
        BG_pic = ImageTk.PhotoImage(BG_resized)
        helpmenu_canvas.create_image(0, 0, image=BG_pic, anchor="nw")
        
        #About Text
        helpmenu_canvas.create_text(35, 15, text="ABOUT:", font=('Fonts/Stencil Regular.ttf', 12), fill="White")
        helpmenu_canvas.create_text(185, 35, text="Welcome to Tank Wars. This is a free-to-play multiplayer tank", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(194, 50, text="game with unique battlefields and epic powerups. Tank Wars was", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(195, 65, text="created for the purpose of fun only. All images and sprites used in", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(148, 80, text="in this program are credited to their respective owners.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")

        #Controls Text
        helpmenu_canvas.create_text(50, 120, text="CONTROLS:", font=('Fonts/Stencil Regular.ttf', 12), fill="White")
        helpmenu_canvas.create_text(183, 140, text="Player 1's tank is located on the left. To move player 1's tank,", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(183, 155, text="use the WASD keys. To fire a bullet from player 1's tank, use", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(178, 170, text="the right ALT key. Player 2's tank is located on the right. To", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(183, 185, text="move player 2's tank, use the arrow keys. To fire a bullet from", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(112, 200, text="player 2's tank, use the left ALT key.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")

        #How-To-Play Text
        helpmenu_canvas.create_text(61, 240, text="HOW-TO-PLAY:", font=('Fonts/Stencil Regular.ttf', 12), fill="White")
        helpmenu_canvas.create_text(190, 260, text="In order to win, you must hit your opponent's tank once with one", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(181, 275, text="of your bullets. You may only fire 3 bullets at once. Note that", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(176, 290, text="bullets will automatically rebound when they collide with an", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(184, 305, text="obstacle. If a bullet rebounds and hits your tank, you will lose.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(185, 320, text="Around your selected map, you will find various power-ups. To", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(174, 335, text="acquire a power-up, simply drive over it with your tank. The", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(163, 350, text="power-ups that are available provide the following buffs:", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        
        #Power-Up Text        
        helpmenu_canvas.create_text(162, 380, text="Speed Boost: Doubles movement speed, lasts for 10s.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(113, 395, text="Shield: Bullet immunity, lasts for 10s.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(181, 410, text="Radiation: Destroys enemy tank upon collision, lasts for 15s.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(162, 425, text="Breakdown: Disables enemy movement, lasts for 2.5s.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(134, 440, text="Infinite Ammo: Unlimited bullets, lasts for 5s.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(176, 455, text="Speed Bullets: Increases bullet speed by 50%, lasts for 5s.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(165, 470, text="Hijack: Inverts enemy movement controls, lasts for 10s.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")
        helpmenu_canvas.create_text(133, 485, text="Virus: Disables enemy weapon, lasts for 5s.", font=('Fonts/Stencil Regular.ttf', 10), fill="White")

    help_menu = Tk()
    help_menu.title("Help Menu")
    help_menu.configure(bg='#01121a')
    screen_width = help_menu.winfo_screenwidth()
    screen_height = help_menu.winfo_screenheight()
    help_menu.geometry('400x500+' + str(screen_width//2 - 150) + '+' + str(screen_height//2 - 200))
    BG = ImageTk.PhotoImage(file='Backgrounds/Help Panel.png')
    helpmenu_canvas = Canvas(help_menu)
    helpmenu_canvas.pack(fill="both", expand=True)
    helpmenu_canvas.create_image(0, 0, image=BG, anchor="nw")

    help_menu.bind("<Configure>", bg_resizer)
    help_menu.protocol('WM_DELETE_WINDOW', help_menu.destroy)   
    help_menu.mainloop()