import pygame
import sys
import time

import Main_Variables

from Main_Functions import fill_screen
from Main_Functions import load_card_image

from Main_Constants import *

# Initialize Pygame
pygame.init()

# Define results
def main_results():

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

    # Insurance results
    if Main_Variables.insurance_flag == 1:
        if Main_Variables.dealer_score == 21 and len(Main_Variables.dealer_cards) == 2:
            pygame.mixer.Sound.play(coin_change)
            Main_Variables.player_coins += Main_Variables.bet_current
            text = font.render("Insurance paid!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
            
            # Drawing dealer cards
            fill_screen(Main_Variables.player_coins)

            card_image = load_card_image(Main_Variables.dealer_cards[0])
            screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))
            card_image = load_card_image(Main_Variables.dealer_cards[1])
            screen.blit(card_image, (dealer_rect_2[0], dealer_rect_2[1]))

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

    # Results if not split
    if Main_Variables.split_flag == False:
        if Main_Variables.player_score > 21:
            text = font.render("Player has bust, Dealer wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
        elif (  Main_Variables.player_score != Main_Variables.dealer_score and 
                Main_Variables.player_score == 21 and 
                len(Main_Variables.player_cards) == 2):
            if Main_Variables.player_cards[0][1] == Main_Variables.player_cards[1][1]:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 3
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Suited Blackjack! Player wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)
            else:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 2.5
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Blackjack! Player wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)       
        
        # Check for 777
        elif Main_Variables.seven_flag == True:
            pygame.mixer.Sound.play(cheer)
            pygame.mixer.Sound.play(coin_change)
            Main_Variables.player_coins += Main_Variables.bet_current * 4
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("7 7 7! Player wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(4)

        # Check for five card charlie
        elif len(Main_Variables.player_cards) == 5:
            if Main_Variables.dealer_score == 21 and len(Main_Variables.dealer_cards) == 2:
                text = font.render("Blackjack! Dealer wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(2)
            else:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 3
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Five-Card Charlie! Player wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)

        # Check for dealer blackjack and player 21
        elif Main_Variables.dealer_score == 21 and len(Main_Variables.dealer_cards) == 2:
            if Main_Variables.player_score == 21 and len(Main_Variables.player_cards) == 2:
                pygame.mixer.Sound.play(chip_return)
                Main_Variables.player_coins += Main_Variables.bet_current
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Result is a Push, bet is returned.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(2)
            else:
                text = font.render("Blackjack! Dealer wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(3)  

        elif Main_Variables.dealer_score > 21:
            pygame.mixer.Sound.play(coin_change)
            if Main_Variables.double_down_flag == True: Main_Variables.player_coins += Main_Variables.bet_current * 4
            elif Main_Variables.triple_down_flag == True: Main_Variables.player_coins += Main_Variables.bet_current * 6
            else: Main_Variables.player_coins += Main_Variables.bet_current * 2
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Dealer has bust, Player wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
        elif Main_Variables.player_score > Main_Variables.dealer_score:
            pygame.mixer.Sound.play(coin_change)
            if Main_Variables.double_down_flag == True: Main_Variables.player_coins += Main_Variables.bet_current * 4
            elif Main_Variables.triple_down_flag == True: Main_Variables.player_coins += Main_Variables.bet_current * 6
            else: Main_Variables.player_coins += Main_Variables.bet_current * 2
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Player wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
        elif Main_Variables.dealer_score > Main_Variables.player_score:
            text = font.render("Dealer wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
        else:
            pygame.mixer.Sound.play(chip_return)
            if Main_Variables.double_down_flag == True: Main_Variables.player_coins += Main_Variables.bet_current * 2
            elif Main_Variables.triple_down_flag == True: Main_Variables.player_coins += Main_Variables.bet_current * 3
            else: Main_Variables.player_coins += Main_Variables.bet_current
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Result is a Push, bet is returned.", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2,
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)

    # Results if split
    if Main_Variables.split_flag == True:
        print(Main_Variables.player_split_a)
        print(Main_Variables.player_split_b)

        # Split (a) results
        if Main_Variables.split_a_score > 21:
            text = font.render("Split A has bust, Dealer wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
        elif (  Main_Variables.split_a_score != Main_Variables.dealer_score and 
                Main_Variables.split_a_score == 21 and 
                len(Main_Variables.player_split_a) == 2):
            if Main_Variables.player_split_a[0][1] == Main_Variables.player_split_a[1][1]:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 3
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Suited Blackjack! Player wins!", True, white, green)
                text_rect = text.get_rect(center =((    width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)
            else:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 2.5
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Blackjack! Split A wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)
             
        elif Main_Variables.seven_flag == True:
            pygame.mixer.Sound.play(cheer)
            pygame.mixer.Sound.play(coin_change)
            Main_Variables.player_coins += Main_Variables.bet_current * 4
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("7 7 7! Player wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(4)

        # Check for five card charlie
        elif len(Main_Variables.player_split_a) == 5:
            if Main_Variables.dealer_score == 21 and len(Main_Variables.dealer_cards) == 2:
                text = font.render("Blackjack! Dealer wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(3)
            else:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 3
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Five-Card Charlie! Split A wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)

        # Check for dealer blackjack and player 21
        elif Main_Variables.dealer_score == 21 and len(Main_Variables.dealer_cards) == 2:
            if Main_Variables.split_a_score == 21 and len(Main_Variables.player_split_a) == 2:
                pygame.mixer.Sound.play(chip_return)
                Main_Variables.player_coins += Main_Variables.bet_current
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Result is a Push, bet A is returned.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(2)
            else:
                text = font.render("Blackjack! Dealer wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(3)

        elif Main_Variables.dealer_score > 21:
            pygame.mixer.Sound.play(coin_change)
            if Main_Variables.double_down_split_a == True: Main_Variables.player_coins += Main_Variables.bet_current * 4
            elif Main_Variables.triple_down_split_a == True: Main_Variables.player_coins += Main_Variables.bet_current * 6
            else: Main_Variables.player_coins += Main_Variables.bet_current * 2
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Dealer has bust, Split A wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
                
        elif Main_Variables.split_a_score > Main_Variables.dealer_score:
            pygame.mixer.Sound.play(coin_change)
            if Main_Variables.double_down_split_a == True: Main_Variables.player_coins += Main_Variables.bet_current * 4
            elif Main_Variables.triple_down_split_a == True: Main_Variables.player_coins += Main_Variables.bet_current * 6
            else: Main_Variables.player_coins += Main_Variables.bet_current * 2
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Split A wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
                
        elif Main_Variables.dealer_score > Main_Variables.split_a_score:
            text = font.render("Dealer wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
            
        else:
            if Main_Variables.double_down_split_a == True: Main_Variables.player_coins += Main_Variables.bet_current * 2
            elif Main_Variables.triple_down_split_a == True: Main_Variables.player_coins += Main_Variables.bet_current * 3
            else: Main_Variables.player_coins += Main_Variables.bet_current
            pygame.mixer.Sound.play(chip_return)
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Result is a Push, bet A is returned.", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)

        # Drawing dealer cards
        fill_screen(Main_Variables.player_coins)

        card_image = load_card_image(Main_Variables.dealer_cards[0])
        screen.blit(card_image, (dealer_rect_1[0], dealer_rect_1[1]))
        card_image = load_card_image(Main_Variables.dealer_cards[1])
        screen.blit(card_image, (dealer_rect_2[0], dealer_rect_2[1]))

        if len(Main_Variables.dealer_cards) >= 3:
            card_image = load_card_image(Main_Variables.dealer_cards[2])
            screen.blit(card_image, (dealer_rect_3[0], dealer_rect_3[1]))
        if len(Main_Variables.dealer_cards) >= 4:
            card_image = load_card_image(Main_Variables.dealer_cards[3])
            screen.blit(card_image, (dealer_rect_4[0], dealer_rect_4[1]))
        if len(Main_Variables.dealer_cards) >= 5:
            card_image = load_card_image(Main_Variables.dealer_cards[4])
            screen.blit(card_image, (dealer_rect_5[0], dealer_rect_5[1]))

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

        # Split (b) results
        if Main_Variables.split_b_score > 21:
            text = font.render("Split B has bust, Dealer wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
        elif (  Main_Variables.split_b_score != Main_Variables.dealer_score and 
                Main_Variables.split_b_score == 21 and 
                len(Main_Variables.player_split_b) == 2):
            if Main_Variables.player_split_b[0][1] == Main_Variables.player_split_b[1][1]:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 3
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Suited Blackjack! Player wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)
            else:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 2.5
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Blackjack! Split B wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)

        elif Main_Variables.seven_flag == True:
            print("Had to move on because 777 was already awarded.")

        # Check for five card charlie
        elif len(Main_Variables.player_split_b) == 5:
            if Main_Variables.dealer_score == 21 and len(Main_Variables.dealer_cards) == 2:
                text = font.render("Blackjack! Dealer wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(3)
            else:
                pygame.mixer.Sound.play(cheer)
                pygame.mixer.Sound.play(coin_change)
                Main_Variables.player_coins += Main_Variables.bet_current * 3
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Five-Card Charlie! Split B wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(4)

        # Check for dealer blackjack and player 21
        elif Main_Variables.dealer_score == 21 and len(Main_Variables.dealer_cards) == 2:
            if Main_Variables.split_b_score == 21 and len(Main_Variables.player_split_b) == 2:
                pygame.mixer.Sound.play(chip_return)
                Main_Variables.player_coins += Main_Variables.bet_current
                text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
                screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
                text = font.render("Result is a Push, bet B is returned.", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(2)
            else:
                text = font.render("Blackjack! Dealer wins!", True, white, green)
                text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                        height / 2))
                screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
                pygame.display.flip()
                time.sleep(3)

        elif Main_Variables.dealer_score > 21:
            pygame.mixer.Sound.play(coin_change)
            if Main_Variables.double_down_split_b == True: Main_Variables.player_coins += Main_Variables.bet_current * 4
            elif Main_Variables.triple_down_split_b == True: Main_Variables.player_coins += Main_Variables.bet_current * 6
            else: Main_Variables.player_coins += Main_Variables.bet_current * 2
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Dealer has bust, Split B wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
                
        elif Main_Variables.split_b_score > Main_Variables.dealer_score:
            pygame.mixer.Sound.play(coin_change)
            if Main_Variables.double_down_split_b == True: Main_Variables.player_coins += Main_Variables.bet_current * 4
            elif Main_Variables.triple_down_split_b == True: Main_Variables.player_coins += Main_Variables.bet_current * 6
            else: Main_Variables.player_coins += Main_Variables.bet_current * 2
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Split B wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
                
        elif Main_Variables.dealer_score > Main_Variables.split_b_score:
            text = font.render("Dealer wins!", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)

        else:
            pygame.mixer.Sound.play(chip_return)
            if Main_Variables.double_down_split_b == True: Main_Variables.player_coins += Main_Variables.bet_current * 2
            elif Main_Variables.triple_down_split_b == True: Main_Variables.player_coins += Main_Variables.bet_current * 3
            else: Main_Variables.player_coins += Main_Variables.bet_current
            text = font.render("$" + str(int(Main_Variables.player_coins)), True, white, green)
            screen.blit(text, (card_rect[3] / 6, height - card_rect[3] / 2.4))
            text = font.render("Result is a Push, bet B is returned.", True, white, green)
            text_rect = text.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                    height / 2))
            screen.blit(text, (text_rect[0], height - card_rect[3] * 1.3))
            pygame.display.flip()
            time.sleep(2)
    return
