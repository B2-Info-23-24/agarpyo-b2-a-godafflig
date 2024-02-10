import random
import pygame
class Trap:
    def __init__(self, screenw, screenh):
        # recuperation de la taille de l'ecran de jeu 
        self.screenw = screenw  
        self.screenh = screenh  
        self.size = random.randint(40, 150)
        self.position_x = random.randint(self.size, screenw - self.size)
        self.position_y = random.randint(self.size, screenh - self.size)
        self.color = (255, 0, 0)  # Couleur rouge pour les pièges

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), self.size)

    def player_touch_trap(self, player):
        distance = ((self.position_x - player.position_x) ** 2 + (self.position_y - player.position_y) ** 2) ** 0.5
        if distance < self.size + player.size:
            return True
        return False
    
    def reposition(self):
    # S'assure que le piège est repositionné à l'intérieur des limites de l'écran
        self.position_x = random.randint(self.size, self.screenw - self.size)
        self.position_y = random.randint(self.size, self.screenh - self.size)


