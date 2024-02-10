import pygame
import math

class Player:
    def __init__(self, position_x, position_y, speed=1, screen_width=1280, screen_height=720, controller="Keyboard"):
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.size = 40
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.score = 0
        self.controller = controller  # Utilisez le paramètre controller passé lors de l'initialisation

    def move(self, keys):
        if self.controller == "Keyboard":
            # Déplacement vers le haut
            if keys[pygame.K_z] or keys[pygame.K_UP]:
                self.position_y -= self.speed
            # Déplacement vers le bas
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.position_y += self.speed
            # Déplacement vers la gauche
            if keys[pygame.K_q] or keys[pygame.K_LEFT]:
                self.position_x -= self.speed
            # Déplacement vers la droite
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.position_x += self.speed
        elif self.controller == "Mouse":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.move_towards(mouse_x, mouse_y)

        # Empêche le joueur de sortir de l'écran
        self.position_x = max(0, min(self.screen_width, self.position_x))
        self.position_y = max(0, min(self.screen_height, self.position_y))

    def move_towards(self, target_x, target_y):
        # Calculer la direction vers la position cible
        direction_x = target_x - self.position_x
        direction_y = target_y - self.position_y

        # Normaliser la direction pour contrôler la vitesse du joueur
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance > 0:
            direction_x /= distance
            direction_y /= distance

        # Mettre à jour la position du joueur
        self.position_x += direction_x * self.speed
        self.position_y += direction_y * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.position_x, self.position_y), self.size)

    def eat_food(self):
        self.score += 1
        self.speed = min(self.speed + 0.05, 5)  # Augmente la vitesse, avec une limite de 5
        self.size = min(self.size + 2, 200)  # Augmente la taille, avec une limite de 200
