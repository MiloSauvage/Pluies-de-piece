import pygame
import random


class Event:
    def __init__(self, game):
        self.game = game

        self.spawn_point = [0, 135, 270, 405, 540, 675, 810, 945]
        self.event_count = 0
        self.event_count_max = 7
        self.event = [
            "coin",
            "coin",
            "bomb"
        ]
        self.colum = 0
        self.event_choice = 0

        self.timer = 0
        self.timer_max = 1000

    def choice_event(self):
        if self.event_count <= self.event_count_max:
            self.event_choice = random.randint(0, len(self.event) - 1)
            self.event_count += 1
        else:
            if self.game.coin_count == 0 or self.game.bomb_count == 0:
                self.timer += 1
                if self.timer >= self.timer_max:
                    self.timer = 0
                    self.event_count = 0
                    self.event_count_max += 1

    def hard(self):
        if self.event_count_max >= 10:
            self.game.coin.update()
            self.game.bomb.update()

    def draw_event(self):
        print("E:", self.event_count, "   C:",self.game.coin_count, "  B:", self.game.bomb_count)

        self.choice_event()
        self.hard()

        if self.event_count <= self.event_count_max:

            if self.event_choice == 0:
                self.game.spaw_coin()
                self.game.coin_count += 1

            elif self.event_choice == 1:

                self.game.spaw_coin()
                self.game.coin_count += 1

            elif self.event_choice == 2:
                self.game.spawn_bomb()
                self.game.bomb_count += 1

            elif self.event_count == self.event_count_max:
                self.event_count = 0
                self.event_count_max += 1
