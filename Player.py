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
        self.controller = controller  
    def toggle_control_mode(self):
        if self.controller == "Keyboard":
            self.controller = "Mouse"
        else:
            self.controller = "Keyboard"

    def move(self, keys):
        if self.controller == "Keyboard":
            if keys[pygame.K_z] or keys[pygame.K_UP]:
                self.position_y -= self.speed
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.position_y += self.speed
            if keys[pygame.K_q] or keys[pygame.K_LEFT]:
                self.position_x -= self.speed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.position_x += self.speed
        elif self.controller == "Mouse":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.move_towards(mouse_x, mouse_y)

        self.position_x = max(0, min(self.screen_width, self.position_x))
        self.position_y = max(0, min(self.screen_height, self.position_y))

    def move_towards(self, target_x, target_y):
        direction_x = target_x - self.position_x
        direction_y = target_y - self.position_y
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance > 0:
            direction_x /= distance
            direction_y /= distance

        self.position_x += direction_x * self.speed
        self.position_y += direction_y * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.position_x, self.position_y), self.size)

    def eat_food(self):
        self.score += 1
        self.speed = min(self.speed + 0.05, 5) 
        self.size = min(self.size + 2, 200) 
