import pygame


class CrossHair(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.image = pygame.image.load("cr.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() / 5, self.image.get_height() / 5))
        self.rect = self.image.get_rect()
        self.rect.center = [50, 50]

        self.game = game

        self.sound_coin = pygame.mixer.Sound("bouteille.wav")
        self.sound_bomb = pygame.mixer.Sound("boom.wav")

    def check_pause(self):
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.check_pause()
        if self.game.pause_etat != 1:
            if pygame.sprite.spritecollide(self, self.game.all_coins, True):
                self.sound_coin.set_volume(0.1)
                self.sound_coin.play()
                self.game.coin_count -= 1
                self.game.coin.remove()
                self.game.score += 10

            elif pygame.sprite.spritecollide(self, self.game.all_bombs, True):

                self.sound_bomb.set_volume(9.0)
                self.sound_bomb.play()
                self.game.bomb_count -= 1
                self.game.bomb.remove()
                self.game.score -= 20
