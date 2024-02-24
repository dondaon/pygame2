import pygame
import sys
from level import Level

vertical_tile_number = 16
tile_size = 32

screen_height = vertical_tile_number * tile_size
screen_width = 1200
screen = pygame.display.set_mode((screen_width, screen_height))


levels = {0: 'design/image.png', 1: 'design/природаа.jpg', 2: 'design/roof.png'}


def main(a):
    pygame.init()

    pygame.display.set_caption("Slovo BarsiKa")
    bg = pygame.Surface((screen_width, screen_height))
    fon = pygame.transform.scale(pygame.image.load(levels[a]), (screen_width, screen_height))
    bg.blit(fon, (0, 0))
    clock = pygame.time.Clock()
    level = Level(a, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg, (0, 0))
        level.run()

        pygame.display.update()
        clock.tick(60)
