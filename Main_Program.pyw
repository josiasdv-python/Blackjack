import pygame
import sys
import time
import copy

import Main_Variables

from Main_Blackjack import main_blackjack
from Main_Functions import woosh_main_menu
from Main_Functions import woosh_black_box
from Main_Functions import fill_screen_main_menu
from Main_Functions import scrolling_code
from Main_Functions import high_score_code

from Main_Constants import *

# Initialize Pygame
pygame.init()

# Drawing
pygame.display.set_caption("Blackjack!")
once_woosh = 1

# Assess the high score from file
Main_Variables.high_score = high_score_code(Main_Variables.player_coins)

# Main menu
while True:      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Woosh basic strategy once
    if once_woosh == 1:
        screen.fill(green)
        screen.blit(table_green, (  table_green_rect[0], 
                                    table_green_rect[1]))
        pygame.display.flip()
        pygame.mixer.Sound.play(card_deal)
        woosh_main_menu(dest_basic_rect)
    once_woosh += 1
    
    # Drawing
    fill_screen_main_menu(Main_Variables.high_score)

    # Mouse hover code
    if new_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, dark_grey, new_button_rect)  
            screen.blit(text_new_dark_grey, new_rect)
        else:
            pygame.draw.rect(screen, grey, new_button_rect)
            screen.blit(text_new_grey, new_rect)
            screen.blit(box_highlight, (new_button_rect[0], new_button_rect[1]))                 
    else:
        pygame.draw.rect(screen, grey, new_button_rect)
        screen.blit(text_new_grey, new_rect)            
    if shortcuts_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, dark_grey, shortcuts_button_rect)  
            screen.blit(text_shortcuts_dark_grey, shortcuts_rect)
        else:
            pygame.draw.rect(screen, grey, shortcuts_button_rect)
            screen.blit(text_shortcuts_grey, shortcuts_rect)
            screen.blit(box_highlight, (shortcuts_button_rect[0], shortcuts_button_rect[1]))
    else:
        pygame.draw.rect(screen, grey, shortcuts_button_rect)
        screen.blit(text_shortcuts_grey, shortcuts_rect)
    if rules_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, dark_grey, rules_button_rect)  
            screen.blit(text_rules_dark_grey, rules_rect)
        else:
            pygame.draw.rect(screen, grey, rules_button_rect)
            screen.blit(text_rules_grey, rules_rect)
            screen.blit(box_highlight, (rules_button_rect[0], rules_button_rect[1]))
    else:
        pygame.draw.rect(screen, grey, rules_button_rect)
        screen.blit(text_rules_grey, rules_rect)
    if about_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, dark_grey, about_button_rect)  
            screen.blit(text_about_dark_grey, about_rect)
        else:
            pygame.draw.rect(screen, grey, about_button_rect)
            screen.blit(text_about_grey, about_rect)
            screen.blit(box_highlight, (about_button_rect[0], about_button_rect[1]))
    else:
        pygame.draw.rect(screen, grey, about_button_rect)
        screen.blit(text_about_grey, about_rect)
    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, dark_grey, quit_button_rect)  
            screen.blit(text_quit_dark_grey, quit_rect)
        else:
            pygame.draw.rect(screen, grey, quit_button_rect)
            screen.blit(text_quit_grey, quit_rect)
            screen.blit(box_highlight, (quit_button_rect[0], quit_button_rect[1]))
    else:
        pygame.draw.rect(screen, grey, quit_button_rect)
        screen.blit(text_quit_grey, quit_rect)

    pygame.display.flip()

    music = pygame.mixer.music.get_busy()
    if music == False:
        pygame.mixer.music.set_volume(50/100)
        pygame.mixer.music.play(5)

    # Pause to wait for event
    event = pygame.event.wait()

    # Look for keys pressed
    keys = pygame.key.get_pressed()

    # New game check
    if keys[pygame.K_n]:
        
        # Set and fade volume because of MIDI bug in Windows SDL
        vol = 50
        while vol != 0:
            vol -= 2
            pygame.mixer.music.set_volume(vol/100)
            pygame.time.Clock().tick(60)    # Limit to 60 FPS
        pygame.mixer.music.stop()
        silence = pygame.mixer.music.load(os.path.join("Assets", "Silence.mid"))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.stop()
        
        # Start blackjack game
        main_blackjack()
        
        # Return to main menu after game
        once_woosh = 1
        sensation = pygame.mixer.music.load(os.path.join("Assets", "Sensation.mid"))

        # Assess the high score from file
        Main_Variables.high_score = high_score_code(Main_Variables.player_coins)

    # Toggle fullscreen
    if keys[pygame.K_f]: pygame.display.toggle_fullscreen()

    # Change bet for next hand
    if keys[pygame.K_b]:
        temp_item = Main_Variables.bet_cycle.pop(0)
        Main_Variables.bet_next = copy.copy(temp_item)
        Main_Variables.bet_cycle.append(temp_item)
        text = font.render("Bet changed to $" + str(Main_Variables.bet_next) + " for future hands.", True, white, green)
        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                height / 2))
        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
        pygame.display.flip()
        time.sleep(1)

    # Change animation speed
    if keys[pygame.K_a]:
        temp_anim = Main_Variables.animation_cycle.pop(0)
        Main_Variables.animation_speed = copy.copy(temp_anim)
        Main_Variables.animation_cycle.append(temp_anim)
        if temp_anim == 30: text = font.render("Animation changed to Slow.", True, white, green)
        if temp_anim == 60: text = font.render("Animation changed to Medium.", True, white, green)
        if temp_anim == 90: text = font.render("Animation changed to Fast.", True, white, green)       
        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                height / 2))
        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
        pygame.display.flip()
        time.sleep(1)
    
    # Escape game
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Look for mouse button released
    if event.type == pygame.MOUSEBUTTONUP:

        # Check if it was the left button
        if event.button == 1:
        
            # Check if mouse cursor collides with new rectangle
            if new_button_rect.collidepoint(event.pos):
                
                # Set and fade volume because of MIDI bug in Windows SDL
                vol = 50
                while vol != 0:
                    vol -= 5
                    pygame.mixer.music.set_volume(vol/100)
                    pygame.time.Clock().tick(60)    # Limit to 60 FPS
                pygame.mixer.music.stop()
                silence = pygame.mixer.music.load(os.path.join("Assets", "Silence.mid"))
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.stop()
                
                # Start blackjack game
                main_blackjack()
                
                # Return to main menu after game
                once_woosh = 1
                sensation = pygame.mixer.music.load(os.path.join("Assets", "Sensation.mid"))

                # Assess the high score from file
                Main_Variables.high_score = high_score_code(Main_Variables.player_coins)

            # Check if mouse cursor collides with shortcuts rectangle
            if shortcuts_button_rect.collidepoint(event.pos):
                pygame.mixer.Sound.play(card_deal)
                woosh_black_box(dest_shortcuts_rect)
                screen.fill(green)
                screen.blit(table_green, (  table_green_rect[0], 
                                            table_green_rect[1]))
                pygame.draw.rect(screen, black, basic_background_rect)
                screen.blit(basic, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
                pygame.draw.rect(screen, black, dest_shortcuts_rect)
                pygame.display.flip()
                
                # Scrolling shortcuts
                scrolling_code(scrolling_shortcuts_list)

            # Check if mouse cursor collides with rules rectangle
            if rules_button_rect.collidepoint(event.pos):
                pygame.mixer.Sound.play(card_deal)
                woosh_black_box(dest_rules_rect)
                screen.fill(green)
                screen.blit(table_green, (  table_green_rect[0], 
                                            table_green_rect[1]))
                pygame.draw.rect(screen, black, basic_background_rect)
                screen.blit(basic, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
                pygame.draw.rect(screen, black, dest_rules_rect)
                pygame.display.flip()
                
                # Scrolling rules
                scrolling_code(scrolling_rules_list)

            # Check if mouse cursor collides with about rectangle
            if about_button_rect.collidepoint(event.pos):
                pygame.mixer.Sound.play(card_deal)
                woosh_black_box(dest_about_rect)
                screen.fill(green)
                screen.blit(table_green, (  table_green_rect[0], 
                                            table_green_rect[1]))
                pygame.draw.rect(screen, black, basic_background_rect)
                screen.blit(basic, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
                pygame.draw.rect(screen, black, dest_about_rect)
                pygame.display.flip()

                # Scrolling about
                scrolling_code(scrolling_about_list)

            # Check if mouse cursor collides with quit rectangle
            if quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    pygame.time.Clock().tick(60)    # Limit to 60 FPS



