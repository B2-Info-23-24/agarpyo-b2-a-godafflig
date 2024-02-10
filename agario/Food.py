import pygame
import random

class Food:
    def __init__(self, screenw, screenh):
        self.screenw = screenw  # Initialise l'attribut screen_width
        self.screenh = screenh  # Initialise l'attribut screen_height
        self.position_x = random.randint(0, screenw)
        self.position_y = random.randint(0, screenh)
        self.size = 50
        self.color = (0,255,0)

    def reposition(self):
        """Place la nourriture à une position aléatoire sur la carte."""
        self.position_x = random.randint(0, self.screenw)
        self.position_y = random.randint(0, self.screenh)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), self.size)

    def is_eaten(self, pos_x, pos_y, size):
        distance = ((self.position_x - pos_x) ** 2 + (self.position_y - pos_y) ** 2) ** 0.5
        if distance < self.size + size:
            return True
        return False
   