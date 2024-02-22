import pygame


def the_end():
    size = width, height = (1200, 512)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60

    fon = pygame.transform.scale(pygame.image.load('design/output_348845950_0.jpg'), (1200, 512))
    screen.blit(fon, (0, 0))
    text = ['///']

    pygame.font.init()
    font = pygame.font.Font(None, 27)
    font2 = pygame.font.Font(None, 60)
    text2 = font2.render('You win!', True, (255, 255, 255))
    text3 = font.render('Нажмите любую клавишу, чтобы exit', True, (255, 255, 255))
    text_coord = 150
    for line in text:
        string = font.render(line, 1, pygame.Color('white'))
        string_rect = string.get_rect()
        text_coord += 10
        string_rect.top = text_coord
        string_rect.x = 10
        text_coord += string_rect.height
        screen.blit(string, string_rect)

    while True:
        screen.blit(text2, text2.get_rect(center=(width / 2, height / 4)))
        screen.blit(text3, text3.get_rect(center=(width / 2, 5 * height / 6)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()

        pygame.display.flip()
        clock.tick(fps)

    the_end()
