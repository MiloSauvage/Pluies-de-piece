import pygame


class BG1(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.image = pygame.image.load("bg_sky1.png")
        self.image = pygame.transform.scale(self.image, (1080, 720))
        self.rect = self.image.get_rect()
        self.speed = 1
        self.rect.x = -1080
        self.rect.y = 0

    def spawn(self):
        self.game.spawn_bg1()

    def update(self):
        if self.rect.x <= 1080:
            if self.game.pause_etat != 1:
                self.rect.x += self.speed
        else:
            self.rect.x = -1080