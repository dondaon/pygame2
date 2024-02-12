import pygame
from main import main


def intro():
    size = width, height = (800, 640)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60

    fon = pygame.image.load("intro.jpg")
    screen.blit(fon, (0, 0))
    text = ['Кот по кличке Барсик был уважаемым членом уличной банды в городе.',
            'Однако, однажды его лидер выгнал его из банды, обвинив невиновного. ',
            'Гордый и обиженный Барсик решил, что пришло время мстить бывшим "друзьям".',
            'Пытаясь найти способ вернуться и дать отпор банде, Барсик',
            'случайно попадает в запутанное подземелье, полное опасностей.',
            'Он должен пройти через множество испытаний, чтобы выбраться из этого лабиринта...']

    pygame.font.init()
    font = pygame.font.Font(None, 27)
    font2 = pygame.font.Font(None, 60)
    text2 = font2.render('Предыстория', True, (255, 255, 255))
    text3 = font.render('Нажмите любую клавишу, чтобы начать!', True, (255, 255, 255))
    text_coord = 200
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
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                main()
        pygame.display.flip()
        clock.tick(fps)
    intro()
