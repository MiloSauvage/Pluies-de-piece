import pygame


class Pause(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.image = pygame.image.load("pause.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 250

    def update(self):
        if self.game.pause_etat == 1:
            self.game.screen.blit(self.image, (self.rect.x, self.rect.y))
