import pygame
import random
import sys
import os

import Main_Variables

from Main_Constants import *

# Initialize Pygame
pygame.init()

# Define function woosh
def woosh(destination_rect):
    temp_rect = [middle_rect[0], -card_rect[3] * 3/4, card_rect[2], card_rect[3]]
    x = (destination_rect[0] - temp_rect[0]) / 12
    y = (destination_rect[1] + card_rect[3] * 3/4) / 12
    while temp_rect[1] <= destination_rect[1]:
        screen.blit(back_image, (temp_rect[0], temp_rect[1]))
        temp_rect[0] += x
        temp_rect[1] += y
        pygame.display.update()
        pygame.time.Clock().tick(Main_Variables.animation_speed)    # Limit based on animation speed
    return

# Define function woosh main menu
def woosh_main_menu(destination_rect):
    temp_rect = [middle_rect[0], -card_rect[3] * 3/4, card_rect[2], card_rect[3]]
    x = (destination_rect[0] - temp_rect[0]) / 24
    y = (destination_rect[1] + card_rect[3] * 3/4) / 24
    xx = (destination_rect[2] - temp_rect[2]) / 24
    yy = (destination_rect[3] - temp_rect[3]) / 24
    while temp_rect[1] <= destination_rect[1]:
        temp_image = pygame.transform.smoothscale(Main_Variables.deck_strategy, (temp_rect[2], temp_rect[3]))
        pygame.draw.rect(screen, black,(    temp_rect[0] - card_rect[3] / 24,
                                            temp_rect[1] - card_rect[3] / 24,
                                            temp_rect[2] + card_rect[3] / 12,
                                            temp_rect[3] + card_rect[3] / 12))
        screen.blit(temp_image, (temp_rect[0], temp_rect[1]))
        temp_rect[0] += x
        temp_rect[1] += y
        temp_rect[2] += xx
        temp_rect[3] += yy
        pygame.display.update()
        pygame.time.Clock().tick(Main_Variables.animation_speed)    # Limit based on animation speed
    return

# Define function woosh black box
def woosh_black_box(destination_rect):
    temp_rect = [middle_rect[0], -card_rect[3] * 3/4, card_rect[2], card_rect[3]]
    x = (destination_rect[0] - temp_rect[0]) / 24
    y = (destination_rect[1] + card_rect[3] * 3/4) / 24
    xx = (destination_rect[2] - temp_rect[2]) / 24
    yy = (destination_rect[3] - temp_rect[3]) / 24
    while temp_rect[1] <= destination_rect[1]:
        pygame.draw.rect(screen, black, temp_rect)
        temp_rect[0] += x
        temp_rect[1] += y
        temp_rect[2] += xx
        temp_rect[3] += yy
        pygame.display.update()
        pygame.time.Clock().tick(Main_Variables.animation_speed)    # Limit based on animation speed
    return

# Define function fill screen
def fill_screen(player_coins):
    screen.fill(green)
    screen.blit(table_green, (  table_green_rect[0], 
                                table_green_rect[1]))
    pygame.draw.rect(screen, black, basic_background_rect)
    screen.blit(Main_Variables.basic_deck, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
    text = font.render("$" + str(int(player_coins)), True, white, green)
    screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))

    # Draw buttons
    pygame.draw.rect(screen, grey, stand_button_rect, border_radius=2)
    screen.blit(text_stand_grey, stand_rect)
    pygame.draw.rect(screen, grey, hit_button_rect, border_radius=2)
    screen.blit(text_hit_grey, hit_rect)
    pygame.draw.rect(screen, grey, double_button_rect, border_radius=2)
    screen.blit(text_double_grey, double_rect)
    pygame.draw.rect(screen, grey, triple_button_rect, border_radius=2)
    screen.blit(text_triple_grey, triple_rect)
    pygame.draw.rect(screen, grey, split_button_rect, border_radius=2)
    screen.blit(text_split_grey, split_rect)

    # Draw card counting if activated
    if Main_Variables.card_count_toggle:
        current_decks = len(Main_Variables.deck) // 52 + (len(Main_Variables.deck) % 52 > 0)
        if Main_Variables.card_count_running > 0:
            text = font.render("+" + str(round(Main_Variables.card_count_running / current_decks)), True, white, green)
            screen.blit(text, (width - basic_rect[2] - card_rect[3] / 2, height - card_rect[3] / 2.4))
        elif Main_Variables.card_count_running < 0:
            text = font.render("−" + str(abs(round(Main_Variables.card_count_running / current_decks))), True, white, green)
            screen.blit(text, (width - basic_rect[2] - card_rect[3] / 2, height - card_rect[3] / 2.4))
        else:
            text = font.render("±" + str(round(Main_Variables.card_count_running / current_decks)), True, white, green)
            screen.blit(text, (width - basic_rect[2] - card_rect[3] / 2, height - card_rect[3] / 2.4))
    return

# Define function fill screen no buttons
def fill_screen_no_buttons(player_coins):
    screen.fill(green)
    screen.blit(table_green, (  table_green_rect[0], 
                                table_green_rect[1]))
    pygame.draw.rect(screen, black, basic_background_rect)
    screen.blit(Main_Variables.basic_deck, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
    text = font.render("$" + str(int(player_coins)), True, white, green)
    screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
    
    # Draw card counting if activated
    if Main_Variables.card_count_toggle:
        current_decks = len(Main_Variables.deck) // 52 + (len(Main_Variables.deck) % 52 > 0)
        if Main_Variables.card_count_running > 0:
            text = font.render("+" + str(round(Main_Variables.card_count_running / current_decks)), True, white, green)
            screen.blit(text, (width - basic_rect[2] - card_rect[3] / 2, height - card_rect[3] / 2.4))
        elif Main_Variables.card_count_running < 0:
            text = font.render("−" + str(abs(round(Main_Variables.card_count_running / current_decks))), True, white, green)
            screen.blit(text, (width - basic_rect[2] - card_rect[3] / 2, height - card_rect[3] / 2.4))
        else:
            text = font.render("±" + str(round(Main_Variables.card_count_running / current_decks)), True, white, green)
            screen.blit(text, (width - basic_rect[2] - card_rect[3] / 2, height - card_rect[3] / 2.4))
    return

# Define function fill screen main menu
def fill_screen_main_menu(high_score):
    screen.fill(green)
    screen.blit(table_green, (  table_green_rect[0], 
                                table_green_rect[1]))
    pygame.draw.rect(screen, black, basic_background_rect)
    screen.blit(Main_Variables.basic_deck, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
    text = font_main_menu.render("Blackjack!", True, white, green)
    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                            height / 2))
    screen.blit(text, (text_rect[0], card_rect[3] / 4))
    text = font.render("High Score $" + str(int(high_score)), True, white, green)
    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                            height / 2))
    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.6))
    
    # Draw buttons
    pygame.draw.rect(screen, grey, new_button_rect, border_radius=2)
    screen.blit(text_new_grey, new_rect)
    pygame.draw.rect(screen, grey, shortcuts_button_rect, border_radius=2)
    screen.blit(text_shortcuts_grey, shortcuts_rect)
    pygame.draw.rect(screen, grey, options_button_rect, border_radius=2)
    screen.blit(text_options_grey, options_rect)
    pygame.draw.rect(screen, grey, about_button_rect, border_radius=2)
    screen.blit(text_about_grey, about_rect)
    pygame.draw.rect(screen, grey, quit_button_rect, border_radius=2)
    screen.blit(text_quit_grey, quit_rect)

    # Draw card counting if activated
    if Main_Variables.card_count_toggle:
        text = font.render("±0", True, white, green)
        screen.blit(text, (width - basic_rect[2] - card_rect[3] / 2, height - card_rect[3] / 2.4))
    return

# Define function new deck
def new_deck():
    card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    card_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = [(card, suits) for card in card_list for suits in card_suits]
    random.shuffle(deck)
    return deck

# Define function card value
def card_value(card):
    if card[0] in ["Jack", "Queen", "King"]: return 10
    elif card[0] == "Ace": return 11
    return int(card[0])
    
# Define function count value
def count_value(card):
    if card[0] in ["10", "Jack", "Queen", "King", "Ace"]: return -1
    elif card[0] in ["7", "8", "9"]: return 0
    return 1

# Define function load card image
def load_card_image(card):
    image_name = (card[1] + card[0] + ".png")
    card_image_small = pygame.image.load(os.path.join("Assets", image_name)).convert()
    card_image = pygame.transform.smoothscale(card_image_small, (   back_image_small_rect[2] * scale_ratio,
                                                                    back_image_small_rect[3] * scale_ratio))
    card_image.set_colorkey(transparent)
    return card_image
    
# Define function scrolling code
def scrolling_code(scrolling_list):
    sub_dest_box = screen.subsurface(dest_about_rect)
    sub_dest_box_rect = sub_dest_box.get_rect()
    scrolling_texts = []
    for iterable, line in enumerate(scrolling_list):
        scrolling_surface = font.render(line, True, white)
        scrolling_rect = scrolling_surface.get_rect(    centerx = sub_dest_box_rect.centerx,
                                                        y = sub_dest_box_rect.bottom + iterable * card_rect[3] / 3)
        scrolling_texts.append((scrolling_rect, scrolling_surface))
    waiting = True
    while waiting:
        for waiting_event in pygame.event.get():
            if waiting_event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
            if waiting_event.type == pygame.KEYDOWN:

                # Look for keys pressed
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                    print("Moved manually.")
                else:
                    waiting = False

        # Look for keys pressed
        keys = pygame.key.get_pressed()

        # Escape game or scroll faster
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_UP]:
            for scrolling_rect, scrolling_surface in scrolling_texts:
                scrolling_rect.move_ip(0, +2)
                sub_dest_box.blit(scrolling_surface, scrolling_rect)
        if keys[pygame.K_DOWN]:
            for scrolling_rect, scrolling_surface in scrolling_texts:
                scrolling_rect.move_ip(0, -2)
                sub_dest_box.blit(scrolling_surface, scrolling_rect)
            
        sub_dest_box.fill(black)
        for scrolling_rect, scrolling_surface in scrolling_texts:
            scrolling_rect.move_ip(0, -1)
            sub_dest_box.blit(scrolling_surface, scrolling_rect)
        
        # If all scrolling rects have left the box, repeat
        if not sub_dest_box_rect.collidelistall([scrolling_rects for (scrolling_rects, _) in scrolling_texts]):
            scrolling_texts = []
            for iterable, line in enumerate(scrolling_list):
                scrolling_surface = font.render(line, True, white)
                scrolling_rect = scrolling_surface.get_rect(    centerx = sub_dest_box_rect.centerx,
                                                                y = sub_dest_box_rect.bottom + iterable * card_rect[3] / 3)
                scrolling_texts.append((scrolling_rect, scrolling_surface))
        pygame.display.flip()

        # Framerate
        pygame.time.Clock().tick(Main_Variables.animation_speed / 2)
    return

# Define function to check high score
def high_score_code(player_coins):
    high_score_file = open(os.path.join("Assets", "HighScore.txt"), 'r')        # Open file in read mode
    high_score_list = high_score_file.readlines()                               # Only 1 high score line in the list
    high_score = int(high_score_list[0])
    high_score_file.close()
    if high_score < int(player_coins):                                          # Compare with the current player coins
        high_score_file = open(os.path.join("Assets", "HighScore.txt"), 'w')    # Open file in write mode
        high_score_file.write(str(int(player_coins)))                           # Write the new high score
        high_score_file.close()
        return int(player_coins)
    return high_score

# Define blue selection circle draw
def blue_selection_circle(temp_x, temp_y):
    pygame.draw.circle(screen, dark_blue, [temp_x, temp_y], 7)
    pygame.draw.circle(screen, blue, [temp_x, temp_y], 5)
    pygame.draw.circle(screen, light_blue, [temp_x, temp_y], 3)

# Define options code
def options_code():
    sub_dest_box = screen.subsurface(dest_options_rect)
    sub_dest_box_rect = sub_dest_box.get_rect()

    light_black_box = (card_rect[2] / 2,
                       card_rect[2] / 2,
                       sub_dest_box_rect[2] - card_rect[2],
                       sub_dest_box_rect[3] - card_rect[2] * 1.3)
                                                      
    text_options_rect = text_options.get_rect(center = (sub_dest_box_rect.centerx, 
                                                        sub_dest_box_rect.centery))

    # Create a list that has the current state of all options
    options_list = [Main_Variables.num_of_decks, Main_Variables.animation_speed,
                    Main_Variables.bet_next, Main_Variables.card_count_toggle, bool(screen.get_flags() & pygame.FULLSCREEN),
                    Main_Variables.continuous_play]
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        sub_dest_box.fill(black)
        pygame.draw.rect(sub_dest_box, light_black, light_black_box)
        pygame.draw.rect(sub_dest_box, white, light_black_box, 1)
  
        # Mouse hover code for buttons
        if confirm_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.rect(screen, dark_grey, confirm_button_rect, border_radius=2)  
                screen.blit(text_confirm_dark_grey, confirm_rect)
            else:
                pygame.draw.rect(screen, grey, confirm_button_rect, border_radius=2)
                screen.blit(text_confirm_grey, confirm_rect)
                pygame.draw.rect(screen, light_orange, confirm_button_rect, 2, border_radius=2)
                pygame.draw.rect(screen, orange, confirm_button_rect, 1, border_radius=2)
        else:
            pygame.draw.rect(screen, grey, confirm_button_rect, border_radius=2)
            screen.blit(text_confirm_grey, confirm_rect)
        if default_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.rect(screen, dark_grey, default_button_rect, border_radius=2)  
                screen.blit(text_default_dark_grey, default_rect)
            else:
                pygame.draw.rect(screen, grey, default_button_rect, border_radius=2)
                screen.blit(text_default_grey, default_rect)
                pygame.draw.rect(screen, light_orange, default_button_rect, 2, border_radius=2)
                pygame.draw.rect(screen, orange, default_button_rect, 1, border_radius=2)
        else:
            pygame.draw.rect(screen, grey, default_button_rect, border_radius=2)
            screen.blit(text_default_grey, default_rect)
        if cancel_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.rect(screen, dark_grey, cancel_button_rect, border_radius=2)  
                screen.blit(text_cancel_dark_grey, cancel_rect)
            else:
                pygame.draw.rect(screen, grey, cancel_button_rect, border_radius=2)
                screen.blit(text_cancel_grey, cancel_rect)
                pygame.draw.rect(screen, light_orange, cancel_button_rect, 2, border_radius=2)
                pygame.draw.rect(screen, orange, cancel_button_rect, 1, border_radius=2)
        else:
            pygame.draw.rect(screen, grey, cancel_button_rect, border_radius=2)
            screen.blit(text_cancel_grey, cancel_rect)

        # Mouse hover code for selection rectangles
        if highlight_box_1.collidepoint(pygame.mouse.get_pos()):
            if options_list[0] == 1: pygame.draw.rect(screen, blue, highlight_box_1, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_1, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 3], 6, width=1)
        if highlight_box_2.collidepoint(pygame.mouse.get_pos()):
            if options_list[0] == 2: pygame.draw.rect(screen, blue, highlight_box_2, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_2, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * .7, screen_rect.centery - card_rect[2] * 3], 6, width=1)
        if highlight_box_3.collidepoint(pygame.mouse.get_pos()):
            if options_list[0] == 3: pygame.draw.rect(screen, blue, highlight_box_3, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_3, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0], screen_rect.centery - card_rect[2] * 3], 6, width=1)
        if highlight_box_4.collidepoint(pygame.mouse.get_pos()):
            if options_list[0] == 4: pygame.draw.rect(screen, blue, highlight_box_4, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_4, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * .7, screen_rect.centery - card_rect[2] * 3], 6, width=1)
        if highlight_box_5.collidepoint(pygame.mouse.get_pos()):
            if options_list[0] == 5: pygame.draw.rect(screen, blue, highlight_box_5, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_5, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 3], 6, width=1)
        if highlight_box_6.collidepoint(pygame.mouse.get_pos()):
            if options_list[0] == 6: pygame.draw.rect(screen, blue, highlight_box_6, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_6, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * 2.1, screen_rect.centery - card_rect[2] * 3], 6, width=1)
        if highlight_box_7.collidepoint(pygame.mouse.get_pos()):
            if options_list[0] == 7: pygame.draw.rect(screen, blue, highlight_box_7, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_7, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * 2.8, screen_rect.centery - card_rect[2] * 3], 6, width=1)
        if highlight_box_8.collidepoint(pygame.mouse.get_pos()):
            if options_list[0] == 8: pygame.draw.rect(screen, blue, highlight_box_8, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_8, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * 3.5, screen_rect.centery - card_rect[2] * 3], 6, width=1)

        if highlight_box_9.collidepoint(pygame.mouse.get_pos()):
            if options_list[1] == 30: pygame.draw.rect(screen, blue, highlight_box_9, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_9, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 2], 6, width=1)
        if highlight_box_10.collidepoint(pygame.mouse.get_pos()):
            if options_list[1] == 60: pygame.draw.rect(screen, blue, highlight_box_10, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_10, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery - card_rect[2] * 2], 6, width=1)
        if highlight_box_11.collidepoint(pygame.mouse.get_pos()):
            if options_list[1] == 90: pygame.draw.rect(screen, blue, highlight_box_11, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_11, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * .9, screen_rect.centery - card_rect[2] * 2], 6, width=1)

        if highlight_box_12.collidepoint(pygame.mouse.get_pos()):
            if options_list[2] == 10: pygame.draw.rect(screen, blue, highlight_box_12, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_12, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2]], 6, width=1)
        if highlight_box_13.collidepoint(pygame.mouse.get_pos()):
            if options_list[2] == 25: pygame.draw.rect(screen, blue, highlight_box_13, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_13, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery - card_rect[2]], 6, width=1)
        if highlight_box_14.collidepoint(pygame.mouse.get_pos()):
            if options_list[2] == 50: pygame.draw.rect(screen, blue, highlight_box_14, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_14, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * .6, screen_rect.centery - card_rect[2]], 6, width=1)
        if highlight_box_15.collidepoint(pygame.mouse.get_pos()):
            if options_list[2] == 100: pygame.draw.rect(screen, blue, highlight_box_15, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_15, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * 1.6, screen_rect.centery - card_rect[2]], 6, width=1)
        if highlight_box_16.collidepoint(pygame.mouse.get_pos()):
            if options_list[2] == 250: pygame.draw.rect(screen, blue, highlight_box_16, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_16, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] + card_rect[2] * 2.6, screen_rect.centery - card_rect[2]], 6, width=1)

        if highlight_box_17.collidepoint(pygame.mouse.get_pos()):
            if options_list[3] == True: pygame.draw.rect(screen, blue, highlight_box_17, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_17, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery], 6, width=1)
        if highlight_box_18.collidepoint(pygame.mouse.get_pos()):
            if options_list[3] == False: pygame.draw.rect(screen, blue, highlight_box_18, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_18, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery], 6, width=1)
        if highlight_box_19.collidepoint(pygame.mouse.get_pos()):
            if options_list[4] == True: pygame.draw.rect(screen, blue, highlight_box_19, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_19, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery + card_rect[2]], 6, width=1)
        if highlight_box_20.collidepoint(pygame.mouse.get_pos()):
            if options_list[4] == False: pygame.draw.rect(screen, blue, highlight_box_20, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_20, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery + card_rect[2]], 6, width=1)
        if highlight_box_21.collidepoint(pygame.mouse.get_pos()):
            if options_list[5] == True: pygame.draw.rect(screen, blue, highlight_box_21, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_21, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery + card_rect[2] * 2], 6, width=1)
        if highlight_box_22.collidepoint(pygame.mouse.get_pos()):
            if options_list[5] == False: pygame.draw.rect(screen, blue, highlight_box_22, 1)
            else:
                pygame.draw.rect(screen, white, highlight_box_22, 1)
                pygame.draw.circle(screen, white, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery + card_rect[2] * 2], 6, width=1)

        # Check options and fill cirlces with current options
        if options_list[0] == 1: blue_selection_circle(text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 3)
        if options_list[0] == 2: blue_selection_circle(text_all_rect[0] - card_rect[2] * .7, screen_rect.centery - card_rect[2] * 3)
        if options_list[0] == 3: blue_selection_circle(text_all_rect[0], screen_rect.centery - card_rect[2] * 3)
        if options_list[0] == 4: blue_selection_circle(text_all_rect[0] + card_rect[2] * .7, screen_rect.centery - card_rect[2] * 3)
        if options_list[0] == 5: blue_selection_circle(text_all_rect[0] + card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 3)
        if options_list[0] == 6: blue_selection_circle(text_all_rect[0] + card_rect[2] * 2.1, screen_rect.centery - card_rect[2] * 3)
        if options_list[0] == 7: blue_selection_circle(text_all_rect[0] + card_rect[2] * 2.8, screen_rect.centery - card_rect[2] * 3)
        if options_list[0] == 8: blue_selection_circle(text_all_rect[0] + card_rect[2] * 3.5, screen_rect.centery - card_rect[2] * 3)

        if options_list[1] == 30: blue_selection_circle(text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 2)
        if options_list[1] == 60: blue_selection_circle(text_all_rect[0] - card_rect[2] * .4, screen_rect.centery - card_rect[2] * 2)
        if options_list[1] == 90: blue_selection_circle(text_all_rect[0] + card_rect[2] * .9, screen_rect.centery - card_rect[2] * 2)
        
        if options_list[2] == 10: blue_selection_circle(text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2])
        if options_list[2] == 25: blue_selection_circle(text_all_rect[0] - card_rect[2] * .4, screen_rect.centery - card_rect[2])
        if options_list[2] == 50: blue_selection_circle(text_all_rect[0] + card_rect[2] * .6, screen_rect.centery - card_rect[2])
        if options_list[2] == 100: blue_selection_circle(text_all_rect[0] + card_rect[2] * 1.6, screen_rect.centery - card_rect[2])
        if options_list[2] == 250: blue_selection_circle(text_all_rect[0] + card_rect[2] * 2.6, screen_rect.centery - card_rect[2])

        if options_list[3] == True: blue_selection_circle(text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery)
        if options_list[3] == False: blue_selection_circle(text_all_rect[0] - card_rect[2] * .4, screen_rect.centery)
        if options_list[4] == True: blue_selection_circle(text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery + card_rect[2])
        if options_list[4] == False: blue_selection_circle(text_all_rect[0] - card_rect[2] * .4, screen_rect.centery + card_rect[2])
        if options_list[5] == True: blue_selection_circle(text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery + card_rect[2] * 2)
        if options_list[5] == False: blue_selection_circle(text_all_rect[0] - card_rect[2] * .4, screen_rect.centery + card_rect[2] * 2)
        
        # Draw all the dark circles
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 3], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * .7, screen_rect.centery - card_rect[2] * 3], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0], screen_rect.centery - card_rect[2] * 3], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * .7, screen_rect.centery - card_rect[2] * 3], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 3], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * 2.1, screen_rect.centery - card_rect[2] * 3], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * 2.8, screen_rect.centery - card_rect[2] * 3], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * 3.5, screen_rect.centery - card_rect[2] * 3], 9, width=2)
                                                    
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 2], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery - card_rect[2] * 2], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * .9, screen_rect.centery - card_rect[2] * 2], 9, width=2)
        
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery - card_rect[2]], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery - card_rect[2]], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * .6, screen_rect.centery - card_rect[2]], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * 1.6, screen_rect.centery - card_rect[2]], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] + card_rect[2] * 2.6, screen_rect.centery - card_rect[2]], 9, width=2)
        
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery + card_rect[2]], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery + card_rect[2]], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * 1.4, screen_rect.centery + card_rect[2]  * 2], 9, width=2)
        pygame.draw.circle(screen, black, [text_all_rect[0] - card_rect[2] * .4, screen_rect.centery + card_rect[2]  * 2], 9, width=2)

        # Blit all the text
        sub_dest_box.blit(text_options, (text_options_rect[0], sub_dest_box_rect.top))
        screen.blit(text_decks_in_shoe, (text_all_rect[0] - card_rect[2] * 3.8, text_all_rect[1] - card_rect[2] * 3))
        screen.blit(text_animation_speed, (text_all_rect[0] - card_rect[2] * 3.8, text_all_rect[1] - card_rect[2] * 2))
        screen.blit(text_default_bet, (text_all_rect[0] - card_rect[2] * 3.8, text_all_rect[1] - card_rect[2]))
        screen.blit(text_true_count, (text_all_rect[0] - card_rect[2] * 3.8, text_all_rect[1]))
        screen.blit(text_fullscreen, (text_all_rect[0] - card_rect[2] * 3.8, text_all_rect[1] + card_rect[2]))
        screen.blit(text_continuous_play, (text_all_rect[0] - card_rect[2] * 3.8, text_all_rect[1] + card_rect[2] * 2))
        
        screen.blit(text_1, (text_all_rect[0] - card_rect[2] * 1.2, text_all_rect[1] - card_rect[2] * 3))
        screen.blit(text_2, (text_all_rect[0] - card_rect[2] * .5, text_all_rect[1] - card_rect[2] * 3))
        screen.blit(text_3, (text_all_rect[0] + card_rect[2] * .2, text_all_rect[1] - card_rect[2] * 3))
        screen.blit(text_4, (text_all_rect[0] + card_rect[2] * .9, text_all_rect[1] - card_rect[2] * 3))
        screen.blit(text_5, (text_all_rect[0] + card_rect[2] * 1.6, text_all_rect[1] - card_rect[2] * 3))
        screen.blit(text_6, (text_all_rect[0] + card_rect[2] * 2.3, text_all_rect[1] - card_rect[2] * 3))
        screen.blit(text_7, (text_all_rect[0] + card_rect[2] * 3.0, text_all_rect[1] - card_rect[2] * 3))
        screen.blit(text_8, (text_all_rect[0] + card_rect[2] * 3.7, text_all_rect[1] - card_rect[2] * 3))

        screen.blit(text_slow, (text_all_rect[0] - card_rect[2] * 1.2, text_all_rect[1] - card_rect[2] * 2))
        screen.blit(text_medium, (text_all_rect[0] - card_rect[2] * .2, text_all_rect[1] - card_rect[2] * 2))
        screen.blit(text_fast, (text_all_rect[0] + card_rect[2] * 1.1, text_all_rect[1] - card_rect[2] * 2))

        screen.blit(text_10, (text_all_rect[0] - card_rect[2] * 1.2, text_all_rect[1] - card_rect[2]))
        screen.blit(text_25, (text_all_rect[0] - card_rect[2] * .2, text_all_rect[1] - card_rect[2]))
        screen.blit(text_50, (text_all_rect[0] + card_rect[2] * .8, text_all_rect[1] - card_rect[2]))
        screen.blit(text_100, (text_all_rect[0] + card_rect[2] * 1.8, text_all_rect[1] - card_rect[2]))
        screen.blit(text_250, (text_all_rect[0] + card_rect[2] * 2.8, text_all_rect[1] - card_rect[2]))

        screen.blit(text_on_1, (text_all_rect[0] - card_rect[2] * 1.2, text_all_rect[1]))
        screen.blit(text_off_1, (text_all_rect[0] - card_rect[2] * .2, text_all_rect[1]))
        screen.blit(text_on_2, (text_all_rect[0] - card_rect[2] * 1.2, text_all_rect[1] + card_rect[2]))
        screen.blit(text_off_2, (text_all_rect[0] - card_rect[2] * .2, text_all_rect[1] + card_rect[2]))
        screen.blit(text_on_3, (text_all_rect[0] - card_rect[2] * 1.2, text_all_rect[1] + card_rect[2] * 2))
        screen.blit(text_off_3, (text_all_rect[0] - card_rect[2] * .2, text_all_rect[1] + card_rect[2] * 2))
        
        pygame.display.flip()
        
        # Pause to wait for event
        event = pygame.event.wait()

        # Look for keys pressed
        keys = pygame.key.get_pressed()

        # Escape game
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        # Look for mouse button released
        if event.type == pygame.MOUSEBUTTONUP:

            # Check if it was the left button
            if event.button == 1:
            
                # Check if mouse cursor collides with confirm rectangle
                if confirm_button_rect.collidepoint(event.pos):
                    Main_Variables.num_of_decks = options_list[0]

                    # Deck strategy image
                    image_name = ("BasicStrategy" + str(options_list[0]) + "Deck.png")
                    Main_Variables.deck_strategy = pygame.image.load(os.path.join("Assets", image_name)).convert()
                    Main_Variables.basic_deck = pygame.transform.smoothscale(   Main_Variables.deck_strategy,(
                                                                                Main_Variables.deck_strategy_rect[2] * (
                                                                                height - card_rect[3] / 12)/
                                                                                Main_Variables.deck_strategy_rect[3], 
                                                                                height - card_rect[3] / 12))
                    Main_Variables.animation_speed = options_list[1]
                    Main_Variables.bet_next = options_list[2]
                    Main_Variables.card_count_toggle = options_list[3]
                    if options_list[4] != bool(screen.get_flags() & pygame.FULLSCREEN): pygame.display.toggle_fullscreen()
                    Main_Variables.continuous_play = options_list[5]
                    waiting = False

                # Check if mouse cursor collides with default rectangle
                if default_button_rect.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list = [2, 60, 10, False, False, False]

                # Check if mouse cursor collides with cancel rectangle
                if cancel_button_rect.collidepoint(event.pos): waiting = False

                # Check for selection button up of highlight boxes
                if highlight_box_1.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[0] = 1
                if highlight_box_2.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[0] = 2
                if highlight_box_3.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[0] = 3
                if highlight_box_4.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[0] = 4
                if highlight_box_5.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[0] = 5
                if highlight_box_6.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[0] = 6
                if highlight_box_7.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[0] = 7
                if highlight_box_8.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[0] = 8

                if highlight_box_9.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[1] = 30
                if highlight_box_10.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[1] = 60
                if highlight_box_11.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[1] = 90

                if highlight_box_12.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[2] = 10
                if highlight_box_13.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[2] = 25
                if highlight_box_14.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[2] = 50
                if highlight_box_15.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[2] = 100
                if highlight_box_16.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[2] = 250

                if highlight_box_17.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[3] = True
                if highlight_box_18.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[3] = False
                if highlight_box_19.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[4] = True
                if highlight_box_20.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[4] = False
                if highlight_box_21.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[5] = True
                if highlight_box_22.collidepoint(event.pos):
                    pygame.mixer.Sound.play(card_deal)
                    options_list[5] = False      
    return
    
