import pygame
import random


class Coin(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.spawn_point = [0, 135, 270, 405, 540, 675, 810, 945]
        self.spawn_point_y = [0, -135-135, -270-270, -405-405, -540-540, -675-675, -810-810, -945-945]

        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (135, 103.0965))
        self.rect = self.image.get_rect()

        c = random.randint(0, len(self.spawn_point) - 1)
        d = random.randint(0, len(self.spawn_point_y) - 1)

        self.speed_min = 1
        self.speed_max = 2
        self.rect.x = self.spawn_point[c]
        self.rect.y = self.spawn_point[d] -1000
        self.speed = 4

    def forward(self):
        if self.game.pause_etat != 1:
            self.rect.y += self.speed

    def remove(self):
        self.game.all_coins.remove(self)

    def detection(self):
        if self.rect.y >= 720 - 50:
            self.game.coin_count -= 1
            self.remove()
            self.game.score -= 10
            self.game.restart()

    def update(self):
        self.speed = 6
