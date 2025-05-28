import pygame
import sys

from Main_Constants import *

# Define starting cash
player_coins = 1000
high_score = 1000

# Define bet current, next, and cycle
bet_current = 10
bet_next = 10
bet_cycle = [25, 50, 100, 250, 10]

# Define animation speed
animation_speed = 60
animation_cycle = [90, 30, 60]

# Define continuous play
continuous_play = False

# Define card count
card_count_toggle = False
card_count_running = 0

# Define default number of decks
num_of_decks = 2

# Create empty variables
deck = []
player_cards = []
dealer_cards = []    
player_split_a = []
player_split_b = []

dealer_score = 0
player_score = 0
split_a_score = 0
split_b_score = 0

double_down_flag = False
double_down_split_a = False
double_down_split_b = False
triple_down_flag = False
triple_down_split_a = False
triple_down_split_b = False
split_flag = False
seven_flag = False
insurance_flag = 0

# Deck strategy image
deck_strategy = pygame.image.load(os.path.join("Assets", "BasicStrategy2Deck.png")).convert()
deck_strategy_rect = deck_strategy.get_rect()
basic_deck = pygame.transform.smoothscale(deck_strategy, (  deck_strategy_rect[2] * (height - card_rect[3] / 12)/
                                                            deck_strategy_rect[3], 
                                                            height - card_rect[3] / 12))

