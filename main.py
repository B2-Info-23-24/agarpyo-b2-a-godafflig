import pygame
import sys

from player import Player
from food import Food  
from trap import Trap
from gamesetting import GameSettings
from menu import Menu

def check_overlap(item1, item2):
    x1, y1 = item1.position_x, item1.position_y
    x2, y2 = item2.position_x, item2.position_y
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance < (item1.size + item2.size)

def display_end_game_screen(screen, myfont, score):
    screen.fill((0, 0, 0))  
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
                return  

def game_loop(screen, game_settings, myfont):
    clock = pygame.time.Clock()
    player = Player(640, 360, screen_width=1280, screen_height=720, controller=game_settings.control_mode)
    food_items = [Food(1280, 720) for _ in range(game_settings.get_nb_food())]  
    traps = [Trap(1280, 720) for _ in range(game_settings.get_nb_pieges())]

    TIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER, 1000)
    sec = 60

    running = True
    while running:
        screen.fill((0, 0, 0))  

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  
                elif event.key == pygame.K_p:
                    player.toggle_control_mode()
            elif event.type == TIMER:
                sec -= 1
                if sec <= 0:
                    display_end_game_screen(screen, myfont, player.score)
                    return 

        keys = pygame.key.get_pressed()
        player.move(keys)
        
        for single_food in food_items: 
            single_food.draw(screen)
            if single_food.is_eaten(player.position_x, player.position_y, player.size):
                single_food.reposition()
                player.eat_food()
                
        player.draw(screen) 
                

        for trap in traps:  
            trap.draw(screen)
            if trap.player_touch_trap(player):
                if player.size > trap.size:
                    player.size /= 2
                    difficulty = game_settings.get_difficulty()
                    if difficulty is not None:
                        player.speed = max(player.speed / difficulty, 1)
                    else:
                        player.speed = max(player.speed, 1)
                    trap.reposition()

        
        
        
        
        countdown_surface = myfont.render(f'Temps restant: {sec}s', False, (255, 255, 255))
        screen.blit(countdown_surface, (10, 100))
        score_surface = myfont.render(f'Score: {player.score}', False, (255, 255, 255))
        speed_surface = myfont.render(f'Speed: {int(player.speed * 100)}', False, (255, 255, 255))
        size_surface = myfont.render(f'Size: {player.size}', False, (255, 255, 255))
        difficulty_text = f"                Difficulté :  {game_settings.get_difficulty_name()} ,     menu : ECHAP  ,   controller : P "  
        difficulty_surface = myfont.render(difficulty_text, False, (255, 255, 255))
        screen.blit(difficulty_surface, (10, 10))  
        screen.blit(score_surface, (10, 10))
        screen.blit(speed_surface, (10, 40))
        screen.blit(size_surface, (10, 70))
        countdown_surface = myfont.render(f'Temps restant: {sec}s', False, (255, 255, 255))
        screen.blit(countdown_surface, (10, 100)) 
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
