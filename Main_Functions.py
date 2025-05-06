import pygame
import random
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
        temp_image = pygame.transform.smoothscale(basic_strategy, (temp_rect[2], temp_rect[3]))
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
    screen.blit(basic, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
    text = font.render("$" + str(int(player_coins)), True, white, green)
    screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))

    # Draw buttons
    pygame.draw.rect(screen, grey, stand_button_rect)
    screen.blit(text_stand_grey, stand_rect)
    pygame.draw.rect(screen, grey, hit_button_rect)
    screen.blit(text_hit_grey, hit_rect)
    pygame.draw.rect(screen, grey, double_button_rect)
    screen.blit(text_double_grey, double_rect)
    pygame.draw.rect(screen, grey, triple_button_rect)
    screen.blit(text_triple_grey, triple_rect)
    pygame.draw.rect(screen, grey, split_button_rect)
    screen.blit(text_split_grey, split_rect)
    return

# Define function fill screen no buttons
def fill_screen_no_buttons(player_coins):
    screen.fill(green)
    screen.blit(table_green, (  table_green_rect[0], 
                                table_green_rect[1]))
    pygame.draw.rect(screen, black, basic_background_rect)
    screen.blit(basic, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
    text = font.render("$" + str(int(player_coins)), True, white, green)
    screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
    return

# Define function fill screen main menu
def fill_screen_main_menu(high_score):
    screen.fill(green)
    screen.blit(table_green, (  table_green_rect[0], 
                                table_green_rect[1]))
    pygame.draw.rect(screen, black, basic_background_rect)
    screen.blit(basic, (width - basic_rect[2] - card_rect[3] / 24, card_rect[3] / 24))
    text = font_main_menu.render("Blackjack!", True, white, green)
    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                            height / 2))
    screen.blit(text, (text_rect[0], card_rect[3] / 4))
    text = font.render("High Score $" + str(int(high_score)), True, white, green)
    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                            height / 2))
    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.6))
    return

# Define function new deck:
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
    sub_dest_box = screen.subsurface(dest_rules_rect)
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
            if waiting_event.type == pygame.KEYDOWN or waiting_event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
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
