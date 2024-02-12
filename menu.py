import pygame
import sys
from main import main

# initializing the constructor
pygame.init()

# screen resolution
res = (740, 640)

# opens up a window
screen = pygame.display.set_mode(res)

fn = pygame.image.load("cat/menu_fon.png")
screen.blit(fn, (0, 0))

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (237, 140, 156)

# dark shade of the button
color_dark = (255, 73, 108)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('Quit', True, color)
text2 = smallfont.render('Start', True, color)

while True:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 80 <= mouse[0] <= 200 <= mouse[1] <= 240:
                main()

            # if the mouse is clicked on the
            # button the game is terminated
            if 80 <= mouse[0] <= 200 and 250 <= mouse[1] <= 290:
                pygame.quit()

    # stores the (x,y) coordinates into
    # the variable as a tuple


    # if mouse is hovered on a button it
    # changes to lighter shade
    if 80 <= mouse[0] <= 200 and 250 <= mouse[1] <= 290:
        pygame.draw.rect(screen, color_light, [80, 250, 110, 40])

    else:
        pygame.draw.rect(screen, color_dark, [80, 250, 110, 40])

    if 80 <= mouse[0] <= 200 <= mouse[1] <= 240:
        pygame.draw.rect(screen, color_light, [80, 200, 110, 40])

    else:
        pygame.draw.rect(screen, color_dark, [80, 200, 110, 40])

    # superimposing the text onto our button
    screen.blit(text, (100, 250))
    screen.blit(text2, (100, 200))

    # updates the frames of the game
    pygame.display.update()
