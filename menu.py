import pygame
from intro import intro

pygame.init()
res = (740, 640)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Menu")
pygame.display.set_icon(pygame.image.load("icon.jpg"))

fn = pygame.image.load("design/menu_fon.png")
screen.blit(fn, (0, 0))
color = (255, 255, 255)
color_light = (237, 140, 156)  # светлая тема для кнопки
color_dark = (255, 73, 108)  # темная тема для кнопки

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('Quit', True, color)
text2 = smallfont.render('Start', True, color)

pygame.mixer.music.load("3d20874f20174bd.mp3")
pygame.mixer.music.play(-1)

while True:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 80 <= mouse[0] <= 200 <= mouse[1] <= 240:  # Проверяем, была ли нажата кнопка Start
                intro()
            if 80 <= mouse[0] <= 200 and 250 <= mouse[1] <= 290:  # Проверяем, была ли нажата кнопка Quit
                pygame.quit()

    if 80 <= mouse[0] <= 200 and 250 <= mouse[1] <= 290:  # Если наводим на кнопку, то она меняет на светлую тему
        pygame.draw.rect(screen, color_light, [80, 250, 110, 40])

    else:
        pygame.draw.rect(screen, color_dark, [80, 250, 110, 40])

    if 80 <= mouse[0] <= 200 <= mouse[1] <= 240:
        pygame.draw.rect(screen, color_light, [80, 200, 110, 40])

    else:
        pygame.draw.rect(screen, color_dark, [80, 200, 110, 40])

    screen.blit(text, (100, 250))
    screen.blit(text2, (100, 200))
    pygame.display.update()
