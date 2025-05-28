import pygame
import sys
import time
import copy

import Main_Variables

from Main_Functions import woosh
from Main_Functions import fill_screen
from Main_Functions import card_value
from Main_Functions import count_value
from Main_Functions import load_card_image

from Main_Constants import *

# Initialize Pygame
pygame.init()

# Define split code
def main_split():

    Main_Variables.player_split_a = [Main_Variables.player_cards[0]]
    Main_Variables.player_split_b = [Main_Variables.player_cards[1]]

    new_card = Main_Variables.deck.pop()
    Main_Variables.card_count_running += count_value(new_card)
    Main_Variables.player_split_a.append(new_card)    

    # Split table draw
    fill_screen(Main_Variables.player_coins)
    card_image = load_card_image(Main_Variables.player_split_a[0])
    screen.blit(card_image, (player_split_6[0], player_split_6[1]))
    card_image = load_card_image(Main_Variables.player_split_b[0])
    screen.blit(card_image, (player_split_1[0], player_split_1[1]))       
    card_image = load_card_image(Main_Variables.dealer_cards[0])
    screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))

    # Dealer's second card is not shown
    screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))

    # Display refresh for split table
    pygame.display.flip()

    pygame.mixer.Sound.play(card_deal)
    woosh(card_place_split["place_split_7"])

    # Split (a) gets to hit, stand, or double down
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                # Assess the high score from file
                Main_Variables.high_score = high_score_code(Main_Variables.player_coins)
                pygame.quit()
                sys.exit()
        
        # Calculate player score
        Main_Variables.split_a_score = sum(card_value(card) for card in Main_Variables.player_split_a)

        # Check for ace cards in player hand
        ace_cards = 0
        for card in Main_Variables.player_split_a:
            if card[0] == "Ace": ace_cards += 1
        while ace_cards > 0 and Main_Variables.split_a_score > 21:
            Main_Variables.split_a_score -= 10
            ace_cards -= 1

        # Drawing
        fill_screen(Main_Variables.player_coins)

        card_image = load_card_image(Main_Variables.player_split_a[0])
        screen.blit(card_image, (player_split_6[0], player_split_6[1]))
        card_image = load_card_image(Main_Variables.player_split_a[1])
        screen.blit(card_image, (player_split_7[0], player_split_7[1]))
        card_image = load_card_image(Main_Variables.player_split_b[0])
        screen.blit(card_image, (player_split_1[0], player_split_1[1]))      
        card_image = load_card_image(Main_Variables.dealer_cards[0])
        screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))

        # Dealer's second card is not shown
        screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))

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

        # Check if player bust, double down, or triple down
        if Main_Variables.split_a_score > 21: break
        if Main_Variables.double_down_split_a == True or Main_Variables.triple_down_split_a == True: break

        # Check for 77 7 distributed over split hands
        if (    Main_Variables.player_split_a[0][0] == "7" and 
                Main_Variables.player_split_a[0][0] == 
                Main_Variables.player_split_a[1][0] == 
                Main_Variables.player_split_b[0][0]):
            Main_Variables.seven_flag = True
            return

        # Check for five card charlie
        if len(Main_Variables.player_split_a) == 5: break

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

        # Display refresh for card 2 of split (a) and subsequent
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
            Main_Variables.player_split_a.append(new_card)
            which_card = len(Main_Variables.player_split_a) + 5
            woosh(card_place_split[f"place_split_{which_card}"])

        # Double down code split (a)
        if keys[pygame.K_d]:
            if len(Main_Variables.player_split_a) >= 3:
                text = font.render("Can't Double Down after Hit.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(1)
            else:
                Main_Variables.double_down_split_a = True
                Main_Variables.player_coins -= Main_Variables.bet_current
                pygame.mixer.Sound.play(card_deal)
                new_card = Main_Variables.deck.pop()
                Main_Variables.card_count_running += count_value(new_card)
                Main_Variables.player_split_a.append(new_card)
                woosh(card_place_split["place_split_8"])

        # Triple down code split (a)
        if keys[pygame.K_t]:
            if len(Main_Variables.player_split_a) >= 3:
                text = font.render("Can't Triple Down after Hit.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(1)          
            elif Main_Variables.split_a_score < 9 or Main_Variables.split_a_score > 11:
                text = font.render("Can only Triple Down on Hard 9, 10, 11.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(1)
            else:
                Main_Variables.triple_down_split_a = True
                Main_Variables.player_coins -= Main_Variables.bet_current * 2
                pygame.mixer.Sound.play(card_deal)
                new_card = Main_Variables.deck.pop()
                Main_Variables.card_count_running += count_value(new_card)
                Main_Variables.player_split_a.append(new_card)
                woosh(card_place_split["place_split_8"])

        # Split code can't split after split
        if keys[pygame.K_v]:
            text = font.render("Can't Split after Split.", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(1)

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
                    Main_Variables.player_split_a.append(new_card)
                    which_card = len(Main_Variables.player_split_a) + 5
                    woosh(card_place_split[f"place_split_{which_card}"])

                # Check if mouse cursor collides with double rectangle
                if double_button_rect.collidepoint(event.pos):
                    if len(Main_Variables.player_split_a) >= 3:
                        text = font.render("Can't Double Down after Hit.", True, white, green)
                        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                height / 2))
                        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                        pygame.display.flip()
                        time.sleep(1)
                    else:
                        Main_Variables.double_down_split_a = True
                        Main_Variables.player_coins -= Main_Variables.bet_current
                        pygame.mixer.Sound.play(card_deal)
                        new_card = Main_Variables.deck.pop()
                        Main_Variables.card_count_running += count_value(new_card)
                        Main_Variables.player_split_a.append(new_card)
                        woosh(card_place_split["place_split_8"])      
                
                # Check if mouse cursor collides with triple rectangle
                if triple_button_rect.collidepoint(event.pos):
                    if len(Main_Variables.player_split_a) >= 3:
                        text = font.render("Can't Triple Down after Hit.", True, white, green)
                        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                height / 2))
                        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                        pygame.display.flip()
                        time.sleep(1)          
                    elif Main_Variables.split_a_score < 9 or Main_Variables.split_a_score > 11:
                        text = font.render("Can only Triple Down on Hard 9, 10, 11.", True, white, green)
                        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                height / 2))
                        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                        pygame.display.flip()
                        time.sleep(1)
                    else:
                        Main_Variables.triple_down_split_a = True
                        Main_Variables.player_coins -= Main_Variables.bet_current * 2
                        pygame.mixer.Sound.play(card_deal)
                        new_card = Main_Variables.deck.pop()
                        Main_Variables.card_count_running += count_value(new_card)
                        Main_Variables.player_split_a.append(new_card)
                        woosh(card_place_split["place_split_8"])
                
                # Check if mouse cursor collides with split rectangle
                if split_button_rect.collidepoint(event.pos):
                    text = font.render("Can't Split after Split.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                    pygame.display.flip()
                    time.sleep(1)

                # Check if mouse cursor collides with stand rectangle
                if stand_button_rect.collidepoint(event.pos): break

        pygame.time.Clock().tick(60)    # Limit to 60 FPS

    # Display refresh
    pygame.display.flip()

    new_card = Main_Variables.deck.pop()
    Main_Variables.card_count_running += count_value(new_card)
    Main_Variables.player_split_b.append(new_card)
    
    pygame.mixer.Sound.play(card_deal)
    woosh(card_place_split["place_split_2"])

    # Split (b) gets to hit, stand, or double down
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                # Assess the high score from file
                Main_Variables.high_score = high_score_code(Main_Variables.player_coins)
                pygame.quit()
                sys.exit()
        
        # Calculate player score
        Main_Variables.split_b_score = sum(card_value(card) for card in Main_Variables.player_split_b)

        # Check for ace cards in player hand
        ace_cards = 0
        for card in Main_Variables.player_split_b:
            if card[0] == "Ace": ace_cards += 1
        while ace_cards > 0 and Main_Variables.split_b_score > 21:
            Main_Variables.split_b_score -= 10
            ace_cards -= 1

        # Drawing
        fill_screen(Main_Variables.player_coins)

        card_image = load_card_image(Main_Variables.player_split_a[0])
        screen.blit(card_image, (player_split_6[0], player_split_6[1]))
        card_image = load_card_image(Main_Variables.player_split_a[1])
        screen.blit(card_image, (player_split_7[0], player_split_7[1]))
        card_image = load_card_image(Main_Variables.player_split_b[0])
        screen.blit(card_image, (player_split_1[0], player_split_1[1]))
        card_image = load_card_image(Main_Variables.player_split_b[1])
        screen.blit(card_image, (player_split_2[0], player_split_2[1])) 
        card_image = load_card_image(Main_Variables.dealer_cards[0])
        screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))

        # Dealer's second card is not shown
        screen.blit(back_image, (dealer_rect_2[0], dealer_rect_2[1]))

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

        # Check if player bust, double down, or triple down
        if Main_Variables.split_b_score > 21: break
        if Main_Variables.double_down_split_b == True or Main_Variables.triple_down_split_b == True: break

        # Check for five card charlie
        if len(Main_Variables.player_split_b) == 5: break

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

        # Display refresh for card 2 of split (b) and subsequent
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
            Main_Variables.player_split_b.append(new_card)
            which_card = len(Main_Variables.player_split_b)
            woosh(card_place_split[f"place_split_{which_card}"])

        # Double down code split (b)
        if keys[pygame.K_d]:
            if len(Main_Variables.player_split_b) >= 3:
                text = font.render("Can't Double Down after Hit.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(1)
            else:
                Main_Variables.double_down_split_b = True
                Main_Variables.player_coins -= Main_Variables.bet_current
                pygame.mixer.Sound.play(card_deal)
                new_card = Main_Variables.deck.pop()
                Main_Variables.card_count_running += count_value(new_card)
                Main_Variables.player_split_b.append(new_card)
                woosh(card_place_split["place_split_3"])

        # Triple down code split (b)
        if keys[pygame.K_t]:
            if len(Main_Variables.player_split_b) >= 3:
                text = font.render("Can't Triple Down after Hit.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(1)          
            elif Main_Variables.split_b_score < 9 or Main_Variables.split_b_score > 11:
                text = font.render("Can only Triple Down on Hard 9, 10, 11.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(1)
            else:
                Main_Variables.triple_down_split_b = True
                Main_Variables.player_coins -= Main_Variables.bet_current * 2
                pygame.mixer.Sound.play(card_deal)
                new_card = Main_Variables.deck.pop()
                Main_Variables.card_count_running += count_value(new_card)
                Main_Variables.player_split_b.append(new_card)
                woosh(card_place_split["place_split_3"])

        # Split code can't split after split
        if keys[pygame.K_v]:
            text = font.render("Can't Split after Split.", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(1)

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
                    Main_Variables.player_split_b.append(new_card)
                    which_card = len(Main_Variables.player_split_b)
                    woosh(card_place_split[f"place_split_{which_card}"])

                # Check if mouse cursor collides with double rectangle
                if double_button_rect.collidepoint(event.pos):
                    if len(Main_Variables.player_split_b) >= 3:
                        text = font.render("Can't Double Down after Hit.", True, white, green)
                        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                height / 2))
                        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                        pygame.display.flip()
                        time.sleep(1)
                    else:
                        Main_Variables.double_down_split_b = True
                        Main_Variables.player_coins -= Main_Variables.bet_current
                        pygame.mixer.Sound.play(card_deal)
                        new_card = Main_Variables.deck.pop()
                        Main_Variables.card_count_running += count_value(new_card)
                        Main_Variables.player_split_b.append(new_card)
                        woosh(card_place_split["place_split_3"])      
                
                # Check if mouse cursor collides with triple rectangle
                if triple_button_rect.collidepoint(event.pos):
                    if len(Main_Variables.player_split_b) >= 3:
                        text = font.render("Can't Triple Down after Hit.", True, white, green)
                        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                height / 2))
                        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                        pygame.display.flip()
                        time.sleep(1)          
                    elif Main_Variables.split_b_score < 9 or Main_Variables.split_b_score > 11:
                        text = font.render("Can only Triple Down on Hard 9, 10, 11.", True, white, green)
                        text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                                height / 2))
                        screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                        pygame.display.flip()
                        time.sleep(1)
                    else:
                        Main_Variables.triple_down_split_b = True
                        Main_Variables.player_coins -= Main_Variables.bet_current * 2
                        pygame.mixer.Sound.play(card_deal)
                        new_card = Main_Variables.deck.pop()
                        Main_Variables.card_count_running += count_value(new_card)
                        Main_Variables.player_split_b.append(new_card)
                        woosh(card_place_split["place_split_3"])
                
                # Check if mouse cursor collides with split rectangle
                if split_button_rect.collidepoint(event.pos):
                    text = font.render("Can't Split after Split.", True, white, green)
                    text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                            height / 2))
                    screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                    pygame.display.flip()
                    time.sleep(1)

                # Check if mouse cursor collides with stand rectangle
                if stand_button_rect.collidepoint(event.pos): break
                
        pygame.time.Clock().tick(60)    # Limit to 60 FPS
    return
