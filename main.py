import pygame
import sys
from level import Level

vertical_tile_number = 16
tile_size = 24

screen_height = vertical_tile_number * tile_size
screen_width = 1200
screen = pygame.display.set_mode((screen_width, screen_height))


class Game:
    def __init__(self):
        # game attributes
        self.max_level = 2

        self.level = Level(0, screen)
        self.status = 'level'

    def run(self):
        self.level.run()


def main():
    pygame.init()

    pygame.display.set_caption("Slovo BarsiKa")
    bg = pygame.Surface((screen_width, screen_height))
    fon = pygame.transform.scale(pygame.image.load('природаа.jpg'), (screen_width, screen_height))
    bg.blit(fon, (0, 0))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg, (0, 0))
        game.run()

        pygame.display.update()
        clock.tick(60)
