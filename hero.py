from pygame import *
import pyganim

MOVE_SPEED = 7
WIDTH = 32
HEIGHT = 22
COLOR = (0, 0, 0)
JUMP_POWER = 9
GRAVITY = 0.35
MOVE_EXTRA_SPEED = 2.5  # Ускорение
JUMP_EXTRA_POWER = 1   # дополнительная сила прыжка
ANIMATION_SUPER_SPEED_DELAY = 500 # скорость смены кадров при ускорении
ANIMATION_RIGHT = [('cat/Walk_r_1.png'), ('cat/Walk_r_2.png'), ('cat/Walk_r_3.png'),
                   ('cat/Walk_r_4.png'), ('cat/Walk_r_5.png'), ('cat/Walk_r_6.png')]
ANIMATION_LEFT = [('cat/Walk_l_1.png'), ('cat/Walk_l_2.png'), ('cat/Walk_l_3.png'),
                  ('cat/Walk_l_4.png'), ('cat/Walk_l_5.png'), ('cat/Walk_l_6.png')]
ANIMATION_STAY = [('cat/Idle (1).png'), ('cat/Idle (2).png'), ('cat/Idle (3).png'), ('cat/Idle.png')]
ANIMATION_JUMP_LEFT = [('cat/Walk_l_4.png', 100)]
ANIMATION_JUMP_RIGHT = [('cat/Walk_r_3.png', 100)]
ANIMATION_DELAY = 100


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения
        self.startX = x  # Начальная позиция Х, Y
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False
        self.image.set_colorkey((0, 0, 0))
        # Анимация движения вправо
        boltAnim = []
        boltAnimSuperSpeed = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        self.boltAnimRightSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimRightSuperSpeed.play()
        # Анимация движения влево
        boltAnim = []
        boltAnimSuperSpeed = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
            boltAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        self.boltAnimLeftSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimLeftSuperSpeed.play()
        # Анимация без движения
        boltAnim = []
        for anim in ANIMATION_STAY:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimStay = pyganim.PygAnimation(boltAnim)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

    def update(self, left, right, up, running, platforms):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
                if running and (left or right):  # если есть ускорение и мы движемся
                    self.yvel -= JUMP_EXTRA_POWER  # то прыгаем выше
                self.image.fill(Color(COLOR))
                if left:
                    self.boltAnimJumpLeft.blit(self.image, (0, 0))
                else:
                    self.boltAnimJumpRight.blit(self.image, (0, 0))
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            if running:  # если ускорение
                self.xvel -= MOVE_EXTRA_SPEED  # то передвигаемся быстрее
                if not up:  # и если не прыгаем
                    self.boltAnimLeftSuperSpeed.blit(self.image, (0, 0))  # то отображаем быструю анимацию
            else:  # если не бежим
                if not up:  # и не прыгаем
                    self.boltAnimLeft.blit(self.image, (0, 0))  # отображаем анимацию движения
            if up:  # если же прыгаем
                self.boltAnimJumpLeft.blit(self.image, (0, 0))  # отображаем анимацию прыжка

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            if running:
                self.xvel += MOVE_EXTRA_SPEED
                if not up:
                    self.boltAnimRightSuperSpeed.blit(self.image, (0, 0))
            else:
                if not up:
                    self.boltAnimRight.blit(self.image, (0, 0))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))

        if not (left or right):
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom
                    self.yvel = 0