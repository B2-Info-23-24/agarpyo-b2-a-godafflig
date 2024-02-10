import pygame
import sys

class GameSettings:
    def __init__(self, screen):
        self.screen = screen
        self.difficulty = None
        self.control_mode = None  
        self.nb_pieges = 0
        self.nb_food = 0 
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.difficulties = {
            'Facile': 1,
            'Moyen': 2,
            'Difficile': 3,
        }

    def select_difficulty(self):
        self.screen.fill((0, 0, 0))  
        y = 100
        for difficulty in self.difficulties.keys():
            text_surface = self.myfont.render(difficulty, False, (255, 255, 255))
            self.screen.blit(text_surface, (100, y))
            y += 50
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.difficulty = self.difficulties['Facile']
                    elif event.key == pygame.K_2:
                        self.difficulty = self.difficulties['Normal']
                    elif event.key == pygame.K_3:
                        self.difficulty = self.difficulties['Difficile']
                    running = False
    
    def set_difficulty(self, difficulty):
        if difficulty in self.difficulties:
            self.difficulty = self.difficulties[difficulty]
            self.configure_game() 

    def configure_game(self):
        if self.difficulty:
            if self.difficulty == 1:  
                self.nb_pieges = 2
                self.nb_food = 5
            elif self.difficulty == 2:  
                self.nb_pieges = 4
                self.nb_food = 3
            elif self.difficulty == 3:  
                self.nb_pieges = 6
                self.nb_food = 2

    def get_nb_pieges(self):
        return self.nb_pieges
    def get_nb_food(self):
        return self.nb_food

    def get_difficulty(self):
        return self.difficulty
    def set_control_mode(self, mode):
        self.control_mode = mode
    def get_difficulty_name(self):
        for name, value in self.difficulties.items():
            if value == self.difficulty:
                return name
        return "Inconnu" 

