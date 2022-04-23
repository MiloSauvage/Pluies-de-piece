import pygame
import random


class Bomb(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.spawn_point = [0, 135, 270, 405, 540, 675, 810, 945]
        self.spawn_point_y = [0, -200, -335, -465, -595, -740, -880, -970]

        self.image = pygame.image.load("Bomb.png")
        self.image = pygame.transform.scale(self.image, (135, 103.0965))
        self.rect = self.image.get_rect()

        c = random.randint(0, len(self.spawn_point) - 1)
        y = random.randint(0, len(self.spawn_point_y) - 1)

        self.speed_min = 2
        self.speed_max = 3
        self.rect.x = self.spawn_point[c]
        self.rect.y = self.spawn_point_y[y] - 1500
        self.speed = 4

    def forward(self):
        if self.game.pause_etat != 1:
            self.rect.y += self.speed

    def remove(self):
        self.game.all_bombs.remove(self)

    def detection(self):
        if self.rect.y >= 720 - 50:
            self.game.bomb_count -= 1
            self.remove()

    def update(self):
        self.speed = 7
