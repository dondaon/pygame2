from csv import reader
from hero import Player
from monsters import Enemy, Tile, Bloc
import pygame

vertical_tile_number = 11
tile_size = 24

screen_height = vertical_tile_number * tile_size
screen_width = 1200


def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map


class Level:
    def __init__(self, lvl, surface):
        # general setup
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = None
        self.collidable_sprites = pygame.sprite.Group()
        layout = import_csv_layout('level1_data.csv')

        # player
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(layout)

        # sprites
        self.enemy_sprites = self.create_tile_group(layout, 'en')
        self.collidable_sprites = self.create_tile_group(layout, 'co')
        self.constraint_sprites = self.create_tile_group(layout, 'con')
        self.noncollidable_sprites = self.create_tile_group(layout, 'non')

    def create_tile_group(self, layout, t):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    if t == 'co':
                        if val in '012345678':
                            sprite = Bloc(tile_size, x, y, val)
                            sprite_group.add(sprite)

                    elif t == 'en':
                        if val == '50':
                            sprite = Enemy(tile_size, x, y)
                            sprite_group.add(sprite)

                    elif t == 'non':
                        if val in ['9', '10', '11', '12', '13', '14', '15', '16']:
                            sprite = Bloc(tile_size, x, y, val)
                            sprite_group.add(sprite)

                    elif t == 'con':
                        if val == '60' or val in '012345678':
                            sprite = Tile(tile_size, x, y)
                            sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '40':
                    sprite = Player((x, y), self.display_surface)
                    self.player.add(sprite)

    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def run(self):
        # enemy
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy_sprites.draw(self.display_surface)

        self.collidable_sprites.update(self.world_shift)
        self.collidable_sprites.draw(self.display_surface)

        self.noncollidable_sprites.update(self.world_shift)
        self.noncollidable_sprites.draw(self.display_surface)

        # player sprites
        self.player.update()
        self.horizontal_movement_collision()

        self.get_player_on_ground()
        self.vertical_movement_collision()

        self.scroll_x()
        self.player.draw(self.display_surface)
