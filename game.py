import pygame

from event import Event
from coin import Coin
from bomb import Bomb
from crosshair import CrossHair
from bg import BG
from bg1 import BG1
from pause import Pause


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Pluis de piece")

        self.background = pygame.image.load("sky.webp")
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))
        self.background_rect = self.background.get_rect()

        self.button = pygame.image.load("button.png")
        self.button_rect = self.button.get_rect()
        self.button_rect.x = self.screen.get_width() / 6
        self.button_rect.y = self.screen.get_height() / 3.5

        self.is_playing = False

        self.all_coins = pygame.sprite.Group()
        self.coin = Coin(self)
        self.coin_count = 0

        self.all_bombs = pygame.sprite.Group()
        self.bomb = Bomb(self)
        self.bomb_count = 0

        self.event = Event(self)

        self.score = 0
        self.previous_score = 0

        self.crosshair = CrossHair(self)
        self.crosshair_group = pygame.sprite.Group()
        self.crosshair_group.add(CrossHair(self))

        self.bg = BG(self)
        self.bg_group = pygame.sprite.Group()

        self.bg1 = BG1(self)
        self.bg1_group = pygame.sprite.Group()

        self.aeron = pygame.mixer.Sound("aeron.wav")
        self.aeron.set_volume(0.04)
        self.pause_etat = 0

        self.pause = Pause(self)

    def spaw_coin(self):
        self.all_coins.add(Coin(self))

    def spawn_bomb(self):
        self.all_bombs.add(Bomb(self))

    def spawn_bg(self):
        self.bg_group.add(BG(self))

    def spawn_bg1(self):
        self.bg1_group.add(BG1(self))

    def update(self):

        for bg1 in self.bg1_group:
            bg1.update()

        for bg in self.bg_group:
            bg.update()

        for coin in self.all_coins:
            coin.forward()
            coin.detection()

        for bomb in self.all_bombs:
            bomb.forward()
            bomb.detection()

        for crosshair in self.crosshair_group:
            crosshair.update()

        self.event.draw_event()

    def display(self):

        #self.screen.blit(self.background, (0, 0))

        self.bg_group.draw(self.screen)
        self.bg1_group.draw(self.screen)
        self.all_coins.draw(self.screen)
        self.all_bombs.draw(self.screen)
        self.crosshair_group.draw(self.screen)

        font = pygame.font.SysFont("Segoe UI", 30)
        text = font.render(f"score : {self.score}", True, (0, 0, 0))
        self.screen.blit(text, (30, 30))

        self.pause.update()

        self.crosshair_group.draw(self.screen)

        pygame.display.flip()

    def restart(self):
        pygame.mouse.set_visible(True)
        self.is_playing = False
        self.coin_count = 0
        self.bomb_count = 0
        self.previous_score = self.score
        self.score = 0
        self.event.event_count = 0
        self.event.event_count_max = 7
        self.event.event_choice = 0
        self.coin.speed_min = 1
        self.bomb.speed_min = 2
        self.coin.speed_max = 2
        self.bomb.speed_max = 3
        self.all_coins = pygame.sprite.Group()
        self.all_bombs = pygame.sprite.Group()
        self.bg_group = pygame.sprite.Group()
        self.bg.rect.x = 0
        self.bg1_group = pygame.sprite.Group()
        self.bg1.rect.x = -1080

    def run(self):

        running = True

        self.aeron.play()

        while running:

            if self.is_playing:

                self.update()

                self.display()

            else:
                font = pygame.font.SysFont("Segoe UI", 40)
                text = font.render(f"Old Score : {self.previous_score}", True, (0, 0, 0))
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.button, self.button_rect)
                self.screen.blit(text, (400, 500))

                pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_playing == False:
                        if self.button_rect.collidepoint(event.pos):
                            self.is_playing = True
                            self.bg.spawn()
                            self.bg1.spawn()
                            pygame.mouse.set_visible(False)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.is_playing == True:
                        if self.pause_etat == 0:
                            self.pause_etat = 1

                        elif self.pause_etat == 1:
                            self.pause_etat = 0

