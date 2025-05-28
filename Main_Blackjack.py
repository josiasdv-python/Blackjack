import pygame
import random
import sys
import time
import copy

import Main_Variables
import Main_Split
import Main_Results

from Main_Functions import woosh
from Main_Functions import fill_screen
from Main_Functions import fill_screen_no_buttons
from Main_Functions import new_deck
from Main_Functions import card_value
from Main_Functions import count_value
from Main_Functions import load_card_image
from Main_Functions import high_score_code

from Main_Constants import *

# Initialize Pygame
pygame.init()

def main_blackjack():
    # Set or reset player coins to 1000
    Main_Variables.player_coins = 1000
    
    # Reset the card count
    Main_Variables.card_count_running = 0

    # Reset deck
    Main_Variables.deck = []

    # Game loop
    while Main_Variables.player_coins > 0:
        
        # Reset variables
        Main_Variables.dealer_cards = []
        Main_Variables.player_cards = []
        Main_Variables.player_split_a = []
        Main_Variables.player_split_b = []
        Main_Variables.dealer_score = 0
        Main_Variables.player_score = 0
        Main_Variables.split_a_score = 0
        Main_Variables.split_b_score = 0

        Main_Variables.double_down_flag = False
        Main_Variables.double_down_split_a = False
        Main_Variables.double_down_split_b = False
        Main_Variables.triple_down_flag = False
        Main_Variables.triple_down_split_a = False
        Main_Variables.triple_down_split_b = False
        Main_Variables.split_flag = False
        Main_Variables.seven_flag = False
        Main_Variables.insurance_flag = 0

        # New deck if running low and add necessary decks to the shoe
        if len(Main_Variables.deck) < 15:
            Main_Variables.card_count_running = 0
            Main_Variables.deck = new_deck()
            if Main_Variables.num_of_decks >= 2:
                temp_deck = new_deck()
                for card in temp_deck:
                    Main_Variables.deck.insert(0, card)
                random.shuffle(Main_Variables.deck)
            if Main_Variables.num_of_decks >= 3:
                temp_deck = new_deck()
                for card in temp_deck:
                    Main_Variables.deck.insert(0, card)
                random.shuffle(Main_Variables.deck)
            if Main_Variables.num_of_decks >= 4:
                temp_deck = new_deck()
                for card in temp_deck:
                    Main_Variables.deck.insert(0, card)
                random.shuffle(Main_Variables.deck)           
            if Main_Variables.num_of_decks >= 5:
                temp_deck = new_deck()
                for card in temp_deck:
                    Main_Variables.deck.insert(0, card)
                random.shuffle(Main_Variables.deck)           
            if Main_Variables.num_of_decks >= 6:
                temp_deck = new_deck()
                for card in temp_deck:
                    Main_Variables.deck.insert(0, card)
                random.shuffle(Main_Variables.deck)
            if Main_Variables.num_of_decks >= 7:
                temp_deck = new_deck()
                for card in temp_deck:
                    Main_Variables.deck.insert(0, card)
                random.shuffle(Main_Variables.deck)
            if Main_Variables.num_of_decks >= 8:
                temp_deck = new_deck()
                for card in temp_deck:
                    Main_Variables.deck.insert(0, card)
                random.shuffle(Main_Variables.deck)

        # Deal cards
        Main_Variables.player_cards = [Main_Variables.deck.pop(), Main_Variables.deck.pop()]
        Main_Variables.dealer_cards = [Main_Variables.deck.pop(), Main_Variables.deck.pop()]

        # Table draw
        fill_screen_no_buttons(Main_Variables.player_coins)
        pygame.display.flip()

        # Player bets amount with mouse
        if Main_Variables.continuous_play == False:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        
                        # Assess the high score from file
                        Main_Variables.high_score = high_score_code(Main_Variables.player_coins)
                        pygame.quit()
                        sys.exit()

                # Drawing
                fill_screen_no_buttons(Main_Variables.player_coins)
                text = font.render("How much will you bet?", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))

                # Mouse hover code for player bets
                if bet10_button_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pygame.draw.rect(screen, dark_grey, bet10_button_rect, border_radius=2)  
                        screen.blit(text_bet10_dark_grey, bet10_rect)
                    else:
                        pygame.draw.rect(screen, grey, bet10_button_rect, border_radius=2)
                        screen.blit(text_bet10_grey, bet10_rect)
                        pygame.draw.rect(screen, light_orange, bet10_button_rect, 2, border_radius=2)
                        pygame.draw.rect(screen, orange, bet10_button_rect, 1, border_radius=2)                 
                else:
                    pygame.draw.rect(screen, grey, bet10_button_rect, border_radius=2)
                    screen.blit(text_bet10_grey, bet10_rect)            
                if bet25_button_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pygame.draw.rect(screen, dark_grey, bet25_button_rect, border_radius=2)  
                        screen.blit(text_bet25_dark_grey, bet25_rect)
                    else:
                        pygame.draw.rect(screen, grey, bet25_button_rect, border_radius=2)
                        screen.blit(text_bet25_grey, bet25_rect)
                        pygame.draw.rect(screen, light_orange, bet25_button_rect, 2, border_radius=2)
                        pygame.draw.rect(screen, orange, bet25_button_rect, 1, border_radius=2)
                else:
                    pygame.draw.rect(screen, grey, bet25_button_rect, border_radius=2)
                    screen.blit(text_bet25_grey, bet25_rect)
                if bet50_button_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pygame.draw.rect(screen, dark_grey, bet50_button_rect, border_radius=2)  
                        screen.blit(text_bet50_dark_grey, bet50_rect)
                    else:
                        pygame.draw.rect(screen, grey, bet50_button_rect, border_radius=2)
                        screen.blit(text_bet50_grey, bet50_rect)
                        pygame.draw.rect(screen, light_orange, bet50_button_rect, 2, border_radius=2)
                        pygame.draw.rect(screen, orange, bet50_button_rect, 1, border_radius=2)
                else:
                    pygame.draw.rect(screen, grey, bet50_button_rect, border_radius=2)
                    screen.blit(text_bet50_grey, bet50_rect)
                if bet100_button_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pygame.draw.rect(screen, dark_grey, bet100_button_rect, border_radius=2)  
                        screen.blit(text_bet100_dark_grey, bet100_rect)
                    else:
                        pygame.draw.rect(screen, grey, bet100_button_rect, border_radius=2)
                        screen.blit(text_bet100_grey, bet100_rect)
                        pygame.draw.rect(screen, light_orange, bet100_button_rect, 2, border_radius=2)
                        pygame.draw.rect(screen, orange, bet100_button_rect, 1, border_radius=2)
                else:
                    pygame.draw.rect(screen, grey, bet100_button_rect, border_radius=2)
                    screen.blit(text_bet100_grey, bet100_rect)
                if bet250_button_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pygame.draw.rect(screen, dark_grey, bet250_button_rect, border_radius=2)  
                        screen.blit(text_bet250_dark_grey, bet250_rect)
                    else:
                        pygame.draw.rect(screen, grey, bet250_button_rect, border_radius=2)
                        screen.blit(text_bet250_grey, bet250_rect)
                        pygame.draw.rect(screen, light_orange, bet250_button_rect, 2, border_radius=2)
                        pygame.draw.rect(screen, orange, bet250_button_rect, 1, border_radius=2)
                else:
                    pygame.draw.rect(screen, grey, bet250_button_rect, border_radius=2)
                    screen.blit(text_bet250_grey, bet250_rect)

                pygame.display.flip()

                # Pause to wait for player bet
                event = pygame.event.wait()
            
                # Look for keys pressed
                keys = pygame.key.get_pressed()

                # Toggle fullscreen
                if keys[pygame.K_f]:
                    pygame.display.toggle_fullscreen()
                    time.sleep(.2)
                
                # Quit to main menu
                if keys[pygame.K_q]: return
                
                # Escape game
                if keys[pygame.K_ESCAPE]:
                    
                    # Assess the high score from file
                    Main_Variables.high_score = high_score_code(Main_Variables.player_coins)
                    pygame.quit()
                    sys.exit()

                # Look for mouse button released
                if event.type == pygame.MOUSEBUTTONUP:

                    # Check if it was the left button
                    if event.button == 1:
                    
                        # Check if mouse cursor collides with $10 rectangle
                        if bet10_button_rect.collidepoint(event.pos):
                            Main_Variables.bet_current = 10
                            Main_Variables.player_coins -= Main_Variables.bet_current
                            break

                        # Check if mouse cursor collides with $25 rectangle
                        if bet25_button_rect.collidepoint(event.pos):
                            Main_Variables.bet_current = 25
                            Main_Variables.player_coins -= Main_Variables.bet_current
                            break

                        # Check if mouse cursor collides with $50 rectangle
                        if bet50_button_rect.collidepoint(event.pos):
                            Main_Variables.bet_current = 50
                            Main_Variables.player_coins -= Main_Variables.bet_current
                            break

                        # Check if mouse cursor collides with $100 rectangle
                        if bet100_button_rect.collidepoint(event.pos):
                            Main_Variables.bet_current = 100
                            Main_Variables.player_coins -= Main_Variables.bet_current
                            break

                        # Check if mouse cursor collides with $250 rectangle
                        if bet250_button_rect.collidepoint(event.pos):
                            Main_Variables.bet_current = 250
                            Main_Variables.player_coins -= Main_Variables.bet_current
                            break
        
        # Player bets automatically if continuous play is enabled
        if Main_Variables.continuous_play:
            Main_Variables.bet_current = copy.copy(Main_Variables.bet_next)
            Main_Variables.player_coins -= Main_Variables.bet_current 

        print("-------------------------------------------------")
        print("Player Coin Purse:", Main_Variables.player_coins)
        print("-------------------------------------------------")

        # Table draw
        fill_screen(Main_Variables.player_coins)
        pygame.display.flip()

        pygame.mixer.Sound.play(card_deal)
        woosh(card_place_play["place_play_1"])
        fill_screen(Main_Variables.player_coins)
        card_image = load_card_image(Main_Variables.player_cards[0])
        screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))

        # Display refresh for card 1
        pygame.display.flip()
            
        pygame.mixer.Sound.play(card_deal)
        woosh(card_place_deal["place_deal_1"])
        fill_screen(Main_Variables.player_coins)
        card_image = load_card_image(Main_Variables.player_cards[0])
        screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
        card_image = load_card_image(Main_Variables.dealer_cards[0])
        screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))

        # Display refresh for card 2
        pygame.display.flip()
        
        pygame.mixer.Sound.play(card_deal)
        woosh(card_place_play["place_play_2"])
        fill_screen(Main_Variables.player_coins)
        card_image = load_card_image(Main_Variables.player_cards[0])
        screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
        card_image = load_card_image(Main_Variables.dealer_cards[0])
        screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))
        card_image = load_card_image(Main_Variables.player_cards[1])
        screen.blit(card_image, (player_rect_2[0], player_rect_2[1]))

        # Display refresh for card 3
        pygame.display.flip()
        
        pygame.mixer.Sound.play(card_deal)
        woosh(card_place_deal["place_deal_2"])
        
        # Calculate counting cards
        Main_Variables.card_count_running += sum(count_value(card) for card in Main_Variables.player_cards)
        Main_Variables.card_count_running += count_value(Main_Variables.dealer_cards[0])    # But not the 2nd dealer card

        # Player gets to hit, stand, double down, or split
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    # Assess the high score from file
                    Main_Variables.high_score = high_score_code(Main_Variables.player_coins)
                    pygame.quit()
                    sys.exit()    
            
            # Calculate player score
            Main_Variables.player_score = sum(card_value(card) for card in Main_Variables.player_cards)

            # Check for ace cards in player hand
            ace_cards = 0
            for card in Main_Variables.player_cards:
                if card[0] == "Ace": ace_cards += 1
            while ace_cards > 0 and Main_Variables.player_score > 21:
                Main_Variables.player_score -= 10
                ace_cards -= 1

            # Drawing
            fill_screen(Main_Variables.player_coins)

            card_image = load_card_image(Main_Variables.player_cards[0])
            screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
            card_image = load_card_image(Main_Variables.player_cards[1])
            screen.blit(card_image, (player_rect_2[0], player_rect_2[1]))
            card_image = load_card_image(Main_Variables.dealer_cards[0])
            screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))

            # Dealer's second card is not shown
            screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))

            if len(Main_Variables.player_cards) >= 3:
                if Main_Variables.double_down_flag == True or Main_Variables.triple_down_flag == True:
                    card_image = load_card_image(Main_Variables.player_cards[2])
                    rotate_card = pygame.transform.rotate(card_image, 90)
                    screen.blit(rotate_card, (player_rect_3[0], player_rect_3[1]))
                else:
                    card_image = load_card_image(Main_Variables.player_cards[2])
                    screen.blit(card_image, (player_rect_3[0], player_rect_3[1]))
            if len(Main_Variables.player_cards) >= 4:
                card_image = load_card_image(Main_Variables.player_cards[3])
                screen.blit(card_image, (player_rect_4[0], player_rect_4[1]))
            if len(Main_Variables.player_cards) >= 5:
                card_image = load_card_image(Main_Variables.player_cards[4])
                screen.blit(card_image, (player_rect_5[0], player_rect_5[1]))

            # Check if player has blackjack
            if Main_Variables.player_score == 21 and len(Main_Variables.player_cards) == 2: break

            # Check if player bust, double down, or triple down
            if Main_Variables.player_score > 21: break
            if Main_Variables.double_down_flag == True or Main_Variables.triple_down_flag == True: break

            # Check for 777
            if len(Main_Variables.player_cards) == 3:
                if (    Main_Variables.player_cards[0][0] == "7" and 
                        Main_Variables.player_cards[0][0] == 
                        Main_Variables.player_cards[1][0] == 
                        Main_Variables.player_cards[2][0]):
                    Main_Variables.seven_flag = True
                    break

            # Check for five card charlie
            if len(Main_Variables.player_cards) == 5: break        

            # Insurance code
            if Main_Variables.insurance_flag == 0 and Main_Variables.dealer_cards[0][0] == "Ace":
                while Main_Variables.insurance_flag == 0:      
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:

                            # Assess the high score from file
                            Main_Variables.high_score = high_score_code(Main_Variables.player_coins)
                            pygame.quit()
                            sys.exit()

                    # Drawing
                    fill_screen_no_buttons(Main_Variables.player_coins)
                    card_image = load_card_image(Main_Variables.player_cards[0])
                    screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
                    card_image = load_card_image(Main_Variables.player_cards[1])
                    screen.blit(card_image, (player_rect_2[0], player_rect_2[1]))
                    card_image = load_card_image(Main_Variables.dealer_cards[0])
                    screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))

                    # Dealer's second card is not shown
                    screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))
                    text = font.render("Insurance - Will you bet that the Dealer has Blackjack?", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))

                    # Mouse hover code for insurance
                    if yes_button_rect.collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            pygame.draw.rect(screen, dark_grey, yes_button_rect, border_radius=2)  
                            screen.blit(text_yes_dark_grey, yes_rect)
                        else:
                            pygame.draw.rect(screen, grey, yes_button_rect, border_radius=2)
                            screen.blit(text_yes_grey, yes_rect)
                            pygame.draw.rect(screen, light_orange, yes_button_rect, 2, border_radius=2)
                            pygame.draw.rect(screen, orange, yes_button_rect, 1, border_radius=2)                 
                    else:
                        pygame.draw.rect(screen, grey, yes_button_rect, border_radius=2)
                        screen.blit(text_yes_grey, yes_rect)            
                    if no_button_rect.collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            pygame.draw.rect(screen, dark_grey, no_button_rect, border_radius=2)  
                            screen.blit(text_no_dark_grey, no_rect)
                        else:
                            pygame.draw.rect(screen, grey, no_button_rect, border_radius=2)
                            screen.blit(text_no_grey, no_rect)
                            pygame.draw.rect(screen, light_orange, no_button_rect, 2, border_radius=2)
                            pygame.draw.rect(screen, orange, no_button_rect, 1, border_radius=2)
                    else:
                        pygame.draw.rect(screen, grey, no_button_rect, border_radius=2)
                        screen.blit(text_no_grey, no_rect)

                    pygame.display.flip()

                    # Pause to wait for insurance
                    event = pygame.event.wait()
                
                    # Look for keys pressed
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_y]:
                        Main_Variables.player_coins -= Main_Variables.bet_current / 2
                        # Drawing
                        fill_screen(Main_Variables.player_coins)
                        card_image = load_card_image(Main_Variables.player_cards[0])
                        screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
                        card_image = load_card_image(Main_Variables.player_cards[1])
                        screen.blit(card_image, (player_rect_2[0], player_rect_2[1]))
                        card_image = load_card_image(Main_Variables.dealer_cards[0])
                        screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))
                        # Dealer's second card is not shown
                        screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))
                        text = font.render("Insurance taken.", True, white, green)
                        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                height / 2))
                        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                        pygame.display.flip()
                        time.sleep(1)
                        Main_Variables.insurance_flag = 1

                    if keys[pygame.K_n]:
                        # Drawing
                        fill_screen(Main_Variables.player_coins)
                        card_image = load_card_image(Main_Variables.player_cards[0])
                        screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
                        card_image = load_card_image(Main_Variables.player_cards[1])
                        screen.blit(card_image, (player_rect_2[0], player_rect_2[1]))
                        card_image = load_card_image(Main_Variables.dealer_cards[0])
                        screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))
                        # Dealer's second card is not shown
                        screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))
                        text = font.render("Insurance declined.", True, white, green)
                        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                height / 2))
                        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                        pygame.display.flip()
                        time.sleep(1)
                        Main_Variables.insurance_flag = 2

                    # Toggle fullscreen
                    if keys[pygame.K_f]:
                        pygame.display.toggle_fullscreen()
                        time.sleep(.2)
                    
                    # Quit to main menu
                    if keys[pygame.K_q]: return
                    
                    # Escape game
                    if keys[pygame.K_ESCAPE]:
                        
                        # Assess the high score from file
                        Main_Variables.high_score = high_score_code(Main_Variables.player_coins)
                        pygame.quit()
                        sys.exit()

                    # Look for mouse button released
                    if event.type == pygame.MOUSEBUTTONUP:

                        # Check if it was the left button
                        if event.button == 1:
                        
                            # Check if mouse cursor collides with yes rectangle
                            if yes_button_rect.collidepoint(event.pos):
                                Main_Variables.player_coins -= Main_Variables.bet_current / 2
                                # Drawing
                                fill_screen(Main_Variables.player_coins)
                                card_image = load_card_image(Main_Variables.player_cards[0])
                                screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
                                card_image = load_card_image(Main_Variables.player_cards[1])
                                screen.blit(card_image, (player_rect_2[0], player_rect_2[1]))
                                card_image = load_card_image(Main_Variables.dealer_cards[0])
                                screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))
                                # Dealer's second card is not shown
                                screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))
                                text = font.render("Insurance taken.", True, white, green)
                                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                        height / 2))
                                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                                pygame.display.flip()
                                time.sleep(1)
                                Main_Variables.insurance_flag = 1

                            # Check if mouse cursor collides with no rectangle
                            if no_button_rect.collidepoint(event.pos):
                                # Drawing
                                fill_screen(Main_Variables.player_coins)
                                card_image = load_card_image(Main_Variables.player_cards[0])
                                screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
                                card_image = load_card_image(Main_Variables.player_cards[1])
                                screen.blit(card_image, (player_rect_2[0], player_rect_2[1]))
                                card_image = load_card_image(Main_Variables.dealer_cards[0])
                                screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))
                                # Dealer's second card is not shown
                                screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))
                                text = font.render("Insurance declined.", True, white, green)
                                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                        height / 2))
                                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                                pygame.display.flip()
                                time.sleep(1)
                                Main_Variables.insurance_flag = 2
                        
            # Mouse hover code
            if stand_button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.rect(screen, dark_grey, stand_button_rect, border_radius=2)  
                    screen.blit(text_stand_dark_grey, stand_rect)
                else:
                    pygame.draw.rect(screen, grey, stand_button_rect, border_radius=2)
                    screen.blit(text_stand_grey, stand_rect)
                    pygame.draw.rect(screen, light_orange, stand_button_rect, 2, border_radius=2)
                    pygame.draw.rect(screen, orange, stand_button_rect, 1, border_radius=2)                   
            if hit_button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.rect(screen, dark_grey, hit_button_rect, border_radius=2)  
                    screen.blit(text_hit_dark_grey, hit_rect)
                else:
                    pygame.draw.rect(screen, grey, hit_button_rect, border_radius=2)
                    screen.blit(text_hit_grey, hit_rect)
                    pygame.draw.rect(screen, light_orange, hit_button_rect, 2, border_radius=2)
                    pygame.draw.rect(screen, orange, hit_button_rect, 1, border_radius=2)   
            if double_button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.rect(screen, dark_grey, double_button_rect, border_radius=2)  
                    screen.blit(text_double_dark_grey, double_rect)
                else:
                    pygame.draw.rect(screen, grey, double_button_rect, border_radius=2)
                    screen.blit(text_double_grey, double_rect)
                    pygame.draw.rect(screen, light_orange, double_button_rect, 2, border_radius=2)
                    pygame.draw.rect(screen, orange, double_button_rect, 1, border_radius=2)
            if triple_button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.rect(screen, dark_grey, triple_button_rect, border_radius=2)  
                    screen.blit(text_triple_dark_grey, triple_rect)
                else:
                    pygame.draw.rect(screen, grey, triple_button_rect, border_radius=2)
                    screen.blit(text_triple_grey, triple_rect)
                    pygame.draw.rect(screen, light_orange, triple_button_rect, 2, border_radius=2)
                    pygame.draw.rect(screen, orange, triple_button_rect, 1, border_radius=2)
            if split_button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.rect(screen, dark_grey, split_button_rect, border_radius=2)  
                    screen.blit(text_split_dark_grey, split_rect)
                else:
                    pygame.draw.rect(screen, grey, split_button_rect, border_radius=2)
                    screen.blit(text_split_grey, split_rect)
                    pygame.draw.rect(screen, light_orange, split_button_rect, 2, border_radius=2)
                    pygame.draw.rect(screen, orange, split_button_rect, 1, border_radius=2)    
            
            # Display refresh for dealt card 4 and subsequent
            pygame.display.flip()
            
            # Pause to wait for an event
            event = pygame.event.wait()
            
            # Look for keys pressed
            keys = pygame.key.get_pressed()

            # Hit code
            if keys[pygame.K_h]:
                pygame.mixer.Sound.play(card_deal)
                new_card = Main_Variables.deck.pop()
                Main_Variables.card_count_running += count_value(new_card)
                Main_Variables.player_cards.append(new_card)
                which_card = len(Main_Variables.player_cards)
                woosh(card_place_play[f"place_play_{which_card}"])

            # Double down code
            if keys[pygame.K_d]:
                if len(Main_Variables.player_cards) >= 3:
                    text = font.render("Can't Double Down after Hit.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))     
                    pygame.display.flip()
                    time.sleep(1)          
                else:
                    Main_Variables.double_down_flag = True
                    Main_Variables.player_coins -= Main_Variables.bet_current
                    pygame.mixer.Sound.play(card_deal)
                    new_card = Main_Variables.deck.pop()
                    Main_Variables.card_count_running += count_value(new_card)
                    Main_Variables.player_cards.append(new_card)
                    woosh(card_place_play["place_play_3"])

            # Triple down code
            if keys[pygame.K_t]:
                if len(Main_Variables.player_cards) >= 3:
                    text = font.render("Can't Triple Down after Hit.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                    pygame.display.flip()
                    time.sleep(1)          
                elif Main_Variables.player_score < 9 or Main_Variables.player_score > 11:
                    text = font.render("Can only Triple Down on Hard 9, 10, 11.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                    pygame.display.flip()
                    time.sleep(1)
                else:
                    Main_Variables.triple_down_flag = True
                    Main_Variables.player_coins -= Main_Variables.bet_current * 2
                    pygame.mixer.Sound.play(card_deal)
                    new_card = Main_Variables.deck.pop()
                    Main_Variables.card_count_running += count_value(new_card)
                    Main_Variables.player_cards.append(new_card)
                    woosh(card_place_play["place_play_3"])

            # Split code
            if keys[pygame.K_v]:
                if len(Main_Variables.player_cards) >= 3:
                    text = font.render("Can't Split after Hit.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                    pygame.display.flip()
                    time.sleep(1)
                elif card_value(Main_Variables.player_cards[0]) != card_value(Main_Variables.player_cards[1]):
                    text = font.render("Can't Split if you don't have a Pair.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                    pygame.display.flip()
                    time.sleep(1)
                else:
                    Main_Variables.split_flag = True
                    Main_Variables.player_coins -= Main_Variables.bet_current
                    Main_Split.main_split()
                    break

            # Stand code
            if keys[pygame.K_s]: break         

            # Toggle continuous play
            if keys[pygame.K_p]:
                Main_Variables.continuous_play = not Main_Variables.continuous_play
                if Main_Variables.continuous_play:
                    text = font.render("Continuous Play enabled.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                else:
                    text = font.render("Continuous Play disabled.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(1)

            # Toggle fullscreen
            if keys[pygame.K_f]:
                pygame.display.toggle_fullscreen()
                time.sleep(.2)

            # Toggle card counting
            if keys[pygame.K_c]:
                Main_Variables.card_count_toggle = not Main_Variables.card_count_toggle
                if Main_Variables.card_count_toggle:
                    text = font.render("True Card Count enabled.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
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
                else:
                    text = font.render("True Card Count disabled.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(1)

            # Change bet for next hand
            if keys[pygame.K_b]:
                temp_item = Main_Variables.bet_cycle.pop(0)
                Main_Variables.bet_next = copy.copy(temp_item)
                Main_Variables.bet_cycle.append(temp_item)
                text = font.render("Default Bet changed to $" + str(Main_Variables.bet_next) + " for future hands.", True, white, green)
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

            # Quit to main menu
            if keys[pygame.K_q]: return

            # Escape game
            if keys[pygame.K_ESCAPE]:

                # Assess the high score from file
                Main_Variables.high_score = high_score_code(Main_Variables.player_coins)
                pygame.quit()
                sys.exit()
            
            # Look for mouse button released
            if event.type == pygame.MOUSEBUTTONUP:

                # Check if it was the left button
                if event.button == 1:
                
                    # Check if mouse cursor collides with hit rectangle
                    if hit_button_rect.collidepoint(event.pos):
                        pygame.mixer.Sound.play(card_deal)
                        new_card = Main_Variables.deck.pop()
                        Main_Variables.card_count_running += count_value(new_card)
                        Main_Variables.player_cards.append(new_card)
                        which_card = len(Main_Variables.player_cards)
                        woosh(card_place_play[f"place_play_{which_card}"])

                    # Check if mouse cursor collides with double rectangle
                    if double_button_rect.collidepoint(event.pos):
                        if len(Main_Variables.player_cards) >= 3:
                            text = font.render("Can't Double Down after Hit.", True, white, green)
                            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                    height / 2))
                            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                            pygame.display.flip()
                            time.sleep(1)          
                        else:
                            Main_Variables.double_down_flag = True
                            Main_Variables.player_coins -= Main_Variables.bet_current
                            pygame.mixer.Sound.play(card_deal)
                            new_card = Main_Variables.deck.pop()
                            Main_Variables.card_count_running += count_value(new_card)
                            Main_Variables.player_cards.append(new_card)
                            woosh(card_place_play["place_play_3"])

                    # Check if mouse cursor collides with triple rectangle
                    if triple_button_rect.collidepoint(event.pos):
                        if len(Main_Variables.player_cards) >= 3:
                            text = font.render("Can't Triple Down after Hit.", True, white, green)
                            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                    height / 2))
                            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                            pygame.display.flip()
                            time.sleep(1)          
                        elif Main_Variables.player_score < 9 or Main_Variables.player_score > 11:
                            text = font.render("Can only Triple Down on Hard 9, 10, 11.", True, white, green)
                            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                    height / 2))
                            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                            pygame.display.flip()
                            time.sleep(1)
                        else:
                            Main_Variables.triple_down_flag = True
                            Main_Variables.player_coins -= Main_Variables.bet_current * 2
                            pygame.mixer.Sound.play(card_deal)
                            new_card = Main_Variables.deck.pop()
                            Main_Variables.card_count_running += count_value(new_card)
                            Main_Variables.player_cards.append(new_card)
                            woosh(card_place_play["place_play_3"])

                    # Check if mouse cursor collides with split rectangle
                    if split_button_rect.collidepoint(event.pos):
                        if len(Main_Variables.player_cards) >= 3:
                            text = font.render("Can't Split after Hit.", True, white, green)
                            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                    height / 2))
                            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                            pygame.display.flip()
                            time.sleep(1)
                        elif card_value(Main_Variables.player_cards[0]) != card_value(Main_Variables.player_cards[1]):
                            text = font.render("Can't Split if you don't have a Pair.", True, white, green)
                            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                    height / 2))
                            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                            pygame.display.flip()
                            time.sleep(1)
                        else:
                            Main_Variables.split_flag = True
                            Main_Variables.player_coins -= Main_Variables.bet_current
                            Main_Split.main_split()
                            break

                    # Check if mouse cursor collides with stand rectangle
                    if stand_button_rect.collidepoint(event.pos): break
            
            pygame.time.Clock().tick(60)    # Limit to 60 FPS

        # Display refresh for dealt card and subsequent if break to dealer
        pygame.display.flip()
        
        # Get ready to only card count the 2nd dealer card once if it's shown
        once_count_2nd_dealer_card = 1
        
        # Dealer gets to hit or stand
        while True:

            # Calculate dealer score
            Main_Variables.dealer_score = sum(card_value(card) for card in Main_Variables.dealer_cards)
        
            # Check if player has blackjack
            if Main_Variables.player_score == 21 and len(Main_Variables.player_cards) == 2:
                card_image = load_card_image(Main_Variables.dealer_cards[1])
                Main_Variables.card_count_running += count_value(Main_Variables.dealer_cards[1])
                screen.blit(card_image, (dealer_rect_2[0], dealer_rect_2[1]))
                break

            # Check if player bust or both of the splits bust
            if Main_Variables.player_score > 21: break
            if Main_Variables.split_a_score > 21 and Main_Variables.split_b_score > 21: break

            # Check for 777 or 77 7
            if Main_Variables.seven_flag == True: break

            # Check for five card charlie
            if len(Main_Variables.player_split_a) == 5 and len(Main_Variables.player_split_b) == 5:
                card_image = load_card_image(Main_Variables.dealer_cards[1])
                Main_Variables.card_count_running += count_value(Main_Variables.dealer_cards[1])
                screen.blit(card_image, (dealer_rect_2[0], dealer_rect_2[1]))
                break
            if len(Main_Variables.player_cards) == 5:
                card_image = load_card_image(Main_Variables.dealer_cards[1])
                Main_Variables.card_count_running += count_value(Main_Variables.dealer_cards[1])
                screen.blit(card_image, (dealer_rect_2[0], dealer_rect_2[1]))
                break

            # Check for ace cards in dealer hand
            ace_cards = 0
            for card in Main_Variables.dealer_cards:
                if card[0] == "Ace": ace_cards += 1
            while ace_cards > 0 and Main_Variables.dealer_score > 21:
                Main_Variables.dealer_score -= 10
                ace_cards -= 1

            # Drawing dealer cards
            fill_screen(Main_Variables.player_coins)

            card_image = load_card_image(Main_Variables.dealer_cards[0])
            screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))
            card_image = load_card_image(Main_Variables.dealer_cards[1])
            screen.blit(card_image, (dealer_rect_2[0], dealer_rect_2[1]))
            
            # For card counting, only count the dealer's 2nd card once
            if once_count_2nd_dealer_card == 1:
                Main_Variables.card_count_running += count_value(Main_Variables.dealer_cards[1])
            once_count_2nd_dealer_card += 1

            if len(Main_Variables.dealer_cards) >= 3:
                card_image = load_card_image(Main_Variables.dealer_cards[2])
                screen.blit(card_image, (dealer_rect_3[0], dealer_rect_3[1]))
            if len(Main_Variables.dealer_cards) >= 4:
                card_image = load_card_image(Main_Variables.dealer_cards[3])
                screen.blit(card_image, (dealer_rect_4[0], dealer_rect_4[1]))
            if len(Main_Variables.dealer_cards) >= 5:
                card_image = load_card_image(Main_Variables.dealer_cards[4])
                screen.blit(card_image, (dealer_rect_5[0], dealer_rect_5[1]))
            
            # Drawing player cards if not split
            if Main_Variables.split_flag == False:          
                
                card_image = load_card_image(Main_Variables.player_cards[0])
                screen.blit(card_image, (player_rect_1[0], player_rect_1[1]))
                card_image = load_card_image(Main_Variables.player_cards[1])
                screen.blit(card_image, (player_rect_2[0], player_rect_2[1]))     

                if len(Main_Variables.player_cards) >= 3:
                    if Main_Variables.double_down_flag == True or Main_Variables.triple_down_flag == True:
                        card_image = load_card_image(Main_Variables.player_cards[2])
                        rotate_card = pygame.transform.rotate(card_image, 90)
                        screen.blit(rotate_card, (player_rect_3[0], player_rect_3[1]))
                    else:
                        card_image = load_card_image(Main_Variables.player_cards[2])
                        screen.blit(card_image, (player_rect_3[0], player_rect_3[1]))
                if len(Main_Variables.player_cards) >= 4:
                    card_image = load_card_image(Main_Variables.player_cards[3])
                    screen.blit(card_image, (player_rect_4[0], player_rect_4[1]))
                if len(Main_Variables.player_cards) >= 5:
                    card_image = load_card_image(Main_Variables.player_cards[4])
                    screen.blit(card_image, (player_rect_5[0], player_rect_5[1]))

            # Drawing player cards if split
            if Main_Variables.split_flag == True:

                card_image = load_card_image(Main_Variables.player_split_a[0])
                screen.blit(card_image, (player_split_6[0], player_split_6[1]))
                card_image = load_card_image(Main_Variables.player_split_a[1])
                screen.blit(card_image, (player_split_7[0], player_split_7[1]))
                card_image = load_card_image(Main_Variables.player_split_b[0])
                screen.blit(card_image, (player_split_1[0], player_split_1[1]))
                card_image = load_card_image(Main_Variables.player_split_b[1])
                screen.blit(card_image, (player_split_2[0], player_split_2[1]))

                if len(Main_Variables.player_split_a) >= 3:
                    if Main_Variables.double_down_split_a == True or Main_Variables.triple_down_split_a == True:
                        card_image = load_card_image(Main_Variables.player_split_a[2])
                        rotate_card = pygame.transform.rotate(card_image, 90)
                        screen.blit(rotate_card, (player_split_8[0], player_split_8[1]))
                    else:
                        card_image = load_card_image(Main_Variables.player_split_a[2])
                        screen.blit(card_image, (player_split_8[0], player_split_8[1]))
                if len(Main_Variables.player_split_a) >= 4:
                    card_image = load_card_image(Main_Variables.player_split_a[3])
                    screen.blit(card_image, (player_split_9[0], player_split_9[1]))
                if len(Main_Variables.player_split_a) >= 5:
                    card_image = load_card_image(Main_Variables.player_split_a[4])
                    screen.blit(card_image, (player_split_10[0], player_split_10[1]))

                if len(Main_Variables.player_split_b) >= 3:
                    if Main_Variables.double_down_split_b == True or Main_Variables.triple_down_split_b == True:
                        card_image = load_card_image(Main_Variables.player_split_b[2])
                        rotate_card = pygame.transform.rotate(card_image, 90)
                        screen.blit(rotate_card, (player_split_3[0], player_split_3[1]))
                    else:
                        card_image = load_card_image(Main_Variables.player_split_b[2])
                        screen.blit(card_image, (player_split_3[0], player_split_3[1]))
                if len(Main_Variables.player_split_b) >= 4:
                    card_image = load_card_image(Main_Variables.player_split_b[3])
                    screen.blit(card_image, (player_split_4[0], player_split_4[1]))
                if len(Main_Variables.player_split_b) >= 5:
                    card_image = load_card_image(Main_Variables.player_split_b[4])
                    screen.blit(card_image, (player_split_5[0], player_split_5[1]))

            # Display refresh
            pygame.display.flip()

            # Check for five card dealer
            if len(Main_Variables.dealer_cards) == 5: break

            # Check if dealer above 17
            if Main_Variables.dealer_score > 17: break

            # Check remaining soft Aces from earlier Ace check for Soft 17
            if Main_Variables.dealer_score == 17:
                if ace_cards == 0: break
                if ace_cards > 0:
                    pygame.mixer.Sound.play(card_deal)
                    new_card = Main_Variables.deck.pop()
                    Main_Variables.card_count_running += count_value(new_card)
                    Main_Variables.dealer_cards.append(new_card)
                    which_card = len(Main_Variables.dealer_cards)
                    woosh(card_place_deal[f"place_deal_{which_card}"])

            # Deal a new card if under 17
            if Main_Variables.dealer_score < 17:
                pygame.mixer.Sound.play(card_deal)
                new_card = Main_Variables.deck.pop()
                Main_Variables.card_count_running += count_value(new_card)
                Main_Variables.dealer_cards.append(new_card)
                which_card = len(Main_Variables.dealer_cards)
                woosh(card_place_deal[f"place_deal_{which_card}"])

            pygame.time.Clock().tick(60)    # Limit to 60 FPS

        # Display refresh
        pygame.display.flip()

        # Show cards
        print("Dealer has:", Main_Variables.dealer_cards)
        print("Player has:", Main_Variables.player_cards)
        
        # Results code
        Main_Results.main_results()
    return
