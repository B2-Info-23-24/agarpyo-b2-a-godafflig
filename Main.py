import pygame
import sys

# Assurez-vous que les classes Player, Food, Trap, GameSettings, et Menu sont correctement définies
from Player import Player
from Food import Food  
from Trap import Trap
from gamesetting import GameSettings
from menu import Menu

def check_overlap(item1, item2):
    x1, y1 = item1.position_x, item1.position_y
    x2, y2 = item2.position_x, item2.position_y
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance < (item1.size + item2.size)

def display_end_game_screen(screen, myfont, score):
    """Affiche un écran de fin de jeu avec le score et attend une action pour continuer."""
    screen.fill((0, 0, 0))  # Efface l'écran
    text_score = myfont.render(f'Score final: {score}', True, (255, 255, 255))
    text_continue = myfont.render('Appuyez sur n\'importe quelle touche pour continuer.', True, (255, 255, 255))
    screen.blit(text_score, (320, 340))
    screen.blit(text_continue, (320, 380))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return  # Retour au menu principal

def game_loop(screen, game_settings, myfont):
    clock = pygame.time.Clock()
    player = Player(640, 360, screen_width=1280, screen_height=720, controller=game_settings.control_mode)
    food = Food(1280, 720)
    traps = [Trap(1280, 720) for _ in range(game_settings.get_nb_pieges())]
    myfont = pygame.font.SysFont('Comic Sans MS', 30)  

    TIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER, 1000)
    sec = 60

    running = True
    while running:
        for event in pygame.event.get():
            # Gestion des événements...
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Retour immédiat au menu principal
                elif event.key == pygame.K_p:
                    player.toggle_control_mode()
            elif event.type == TIMER:
                sec -= 1
                if sec <= 0:
                    display_end_game_screen(screen, myfont, player.score)
                    return  # Fin de la partie, retour au menu


        keys = pygame.key.get_pressed()
        player.move(keys)

        if food.is_eaten(player.position_x, player.position_y, player.size):
            food.reposition()
            player.eat_food()

        for trap in traps:
            if trap.player_touch_trap(player):
                if player.size > trap.size:
                    player.size /= 2
                    difficulty = game_settings.get_difficulty()
                    if difficulty is not None:
                        player.speed = max(player.speed / difficulty, 1)
                    else:
                        player.speed = max(player.speed, 1)
                    trap.reposition()
        screen.fill((0, 0, 0))
        food.draw(screen)
        player.draw(screen)
        for trap in traps:
            trap.draw(screen)

        # Affichage des informations du jeu...
        countdown_surface = myfont.render(f'Temps restant: {sec}s', False, (255, 255, 255))
        screen.blit(countdown_surface, (10, 100))
        score_surface = myfont.render(f'Score: {player.score}', False, (255, 255, 255))
        speed_surface = myfont.render(f'Speed: {int(player.speed * 100)}', False, (255, 255, 255))
        size_surface = myfont.render(f'Size: {player.size}', False, (255, 255, 255))
        difficulty_text = f"                Difficulté :  {game_settings.get_difficulty_name()} ,     recommencer : ECHAP  ,   quitter le jeu : P "  # Adaptez cette ligne
        difficulty_surface = myfont.render(difficulty_text, False, (255, 255, 255))
        screen.blit(difficulty_surface, (10, 10))  # Ajustez la position selon vos besoins
        screen.blit(score_surface, (10, 10))
        screen.blit(speed_surface, (10, 40))
        screen.blit(size_surface, (10, 70))
         # Après avoir dessiné tout le reste sur l'écran, mais avant `pygame.display.flip()`
        countdown_surface = myfont.render(f'Temps restant: {sec}s', False, (255, 255, 255))
        screen.blit(countdown_surface, (10, 100))  # Ajustez la position selon vos besoins
        pygame.display.flip()
        clock.tick(60)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Agarpyo")
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    while True:
        main_menu = Menu(screen)
        main_menu.display_menu()

        game_settings = GameSettings(screen)
        game_settings.set_difficulty(main_menu.selected_difficulty)
        game_settings.set_control_mode(main_menu.selected_control_mode)
        game_settings.configure_game()
        

        game_loop(screen, game_settings, myfont)

if __name__ == "__main__":
    main()
