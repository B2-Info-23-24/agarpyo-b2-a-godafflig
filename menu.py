# Fichier menu.py
import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.title_font = pygame.font.SysFont('Comic Sans MS', 60)
        self.option_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.difficulty_levels = ['Facile', 'Moyen', 'Difficile']
        self.control_modes = ['Mouse', 'Keyboard']  # Mis à jour pour uniformité
        self.selected_difficulty = None
        self.selected_control_mode = None  # Maintenant géré comme une checkbox
        self.buttons = {
            'start': pygame.Rect(540, 340, 200, 60),
            'quit': pygame.Rect(540, 420, 200, 60)
        }
        self.checkboxes = {
            'Facile': pygame.Rect(100, 600, 20, 20),
            'Moyen': pygame.Rect(400, 600, 20, 20),
            'Difficile': pygame.Rect(700, 600, 20, 20),
            'Mouse': pygame.Rect(100, 500, 20, 20),  # Nouvelle checkbox pour Mouse
            'Keyboard': pygame.Rect(400, 500, 20, 20)  # Nouvelle checkbox pour Keyboard
        }

    def draw_button(self, text, rect, action=None):
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        text_surface = self.option_font.render(text, False, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_checkbox(self, label, rect, is_selected):
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)  # Draw checkbox border
        if is_selected:
            pygame.draw.rect(self.screen, (255, 255, 255), rect.inflate(-2, -2))  # Fill checkbox
        label_surface = self.option_font.render(label, False, (255, 255, 255))
        self.screen.blit(label_surface, (rect.right + 10, rect.top - 5))

    def handle_mouse_click(self, pos):
    # Gestion des sélections de difficulté
        for difficulty, rect in self.checkboxes.items():
            if rect.collidepoint(pos) and difficulty in self.difficulty_levels:
                self.selected_difficulty = difficulty
                break  # Arrête la recherche une fois une difficulté sélectionnée

        # Gestion des sélections de mode de contrôle
        # Pas besoin de réinitialiser self.selected_control_mode ici
        for control_mode, rect in self.checkboxes.items():
            if rect.collidepoint(pos) and control_mode in self.control_modes:
                self.selected_control_mode = control_mode
                break  # Arrête la recherche une fois un mode de contrôle sélectionné

        # Vérification des conditions pour le démarrage du jeu avec le bouton start
        if self.buttons['start'].collidepoint(pos):
            if self.selected_difficulty and self.selected_control_mode:
                self.running = False  # Conditions remplies, le jeu peut démarrer
            else:
                print("Veuillez sélectionner une difficulté et un mode de contrôle")

        # Gestion du bouton Quit
        if self.buttons['quit'].collidepoint(pos):
            pygame.quit()
            quit()


    def display_menu(self):
        while self.running:
            self.screen.fill((0, 0, 0))  # Background color

            # Draw buttons and checkboxes
            for label, rect in self.buttons.items():
                self.draw_button(label.capitalize(), rect)
            for label, rect in self.checkboxes.items():
                is_selected = (label == self.selected_difficulty)
                self.draw_checkbox(label, rect, is_selected)
                for label, rect in self.checkboxes.items():
                    is_selected = label == self.selected_difficulty or label == self.selected_control_mode
                    self.draw_checkbox(label, rect, is_selected)


            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self.handle_mouse_click(event.pos)

            pygame.display.flip()
