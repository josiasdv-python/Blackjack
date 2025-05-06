import pygame
import os

# Initialize Pygame
pygame.init()

# Set up scaling
scale_ratio = 1

# Set up display
width, height = 1080 * scale_ratio, 620 * scale_ratio
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)

# Define colors and font
black = (0, 0, 0)
white = (255, 255, 255)
grey = (239, 239, 232)
dark_grey = (187, 187, 175)
green = (0, 91, 19)
transparent = (0, 128, 255)
transparent_box = (0, 147, 252)
font = pygame.font.Font(os.path.join("Assets", "CalibriBold.ttf"), int(26 * scale_ratio))
font_button = pygame.font.Font(os.path.join("Assets", "CalibriBold.ttf"), int(13 * scale_ratio))
font_main_menu = pygame.font.Font(os.path.join("Assets", "Blackjack.ttf"), int(104 * scale_ratio))

# Define sounds and music
cheer = pygame.mixer.Sound(os.path.join("Assets", "Cheer.wav"))
card_deal = pygame.mixer.Sound(os.path.join("Assets", "CardDeal.wav"))
coin_change = pygame.mixer.Sound(os.path.join("Assets", "CoinChange.wav"))
chip_return = pygame.mixer.Sound(os.path.join("Assets", "ChipReturn.wav"))
sensation = pygame.mixer.music.load(os.path.join("Assets", "Sensation.mid"))

# Define images starting with card back image
back_image_small = pygame.image.load(os.path.join("Assets", "CardBack.png")).convert()
back_image_small_rect = back_image_small.get_rect()
back_image = pygame.transform.scale(back_image_small, ( back_image_small_rect[2] * scale_ratio,
                                                        back_image_small_rect[3] * scale_ratio))
card_rect = back_image.get_rect()
back_image.set_colorkey(transparent)

# Button box highlight image
box_highlight_small = pygame.image.load(os.path.join("Assets", "BoxHighlight.png")).convert()
box_small_rect = box_highlight_small.get_rect()
box_highlight = pygame.transform.scale(box_highlight_small, (   box_small_rect[2] / 2  * scale_ratio,
                                                                box_small_rect[3] / 2  * scale_ratio))
box_highlight_rect = box_highlight.get_rect()
box_highlight.set_colorkey(transparent_box)

# Basic strategy image
basic_strategy = pygame.image.load(os.path.join("Assets", "BasicStrategy.png")).convert()
basic_strategy_rect = basic_strategy.get_rect()
basic = pygame.transform.smoothscale(basic_strategy, (  basic_strategy_rect[2] * (height - card_rect[3] / 12)/
                                                        basic_strategy_rect[3], 
                                                        height - card_rect[3] / 12))
basic_rect = basic.get_rect()

# Background rectangle behind basic strategy image
basic_background_rect = (   width - basic_rect[2] - card_rect[3] / 12,
                            0,
                            basic_rect[2] + card_rect[3] / 12,
                            basic_rect[3] + card_rect[3] / 12)

# Table green image
table_green_small = pygame.image.load(os.path.join("Assets", "TableGreen.png")).convert()
table_green_small_rect = table_green_small.get_rect()
table_green = pygame.transform.smoothscale(table_green_small, ( table_green_small_rect[2] * scale_ratio,
                                                                table_green_small_rect[3] * scale_ratio))

table_green_rect = table_green.get_rect(center = (( width - basic_background_rect[2]) / 2, 
                                                    height / 2 + card_rect[2] / 5))

# Middle card rect                                            
middle_rect = back_image.get_rect(center = ((   width - basic_background_rect[2]) / 2, 
                                                height / 2 + card_rect[2] / 3))

# Main menu destination rectangles
dest_basic_rect = ( width - basic_rect[2] - card_rect[3] / 24,
                    card_rect[3] / 24,
                    basic_rect[2],
                    basic_rect[3])

dest_shortcuts_rect = ((    width - basic_background_rect[2] - middle_rect[2] * 8) / 2, (
                            height - middle_rect[3] * 6) / 2,
                            middle_rect[2] * 8,
                            middle_rect[3] * 6)

dest_rules_rect = ((    width - basic_background_rect[2] - middle_rect[2] * 8) / 2, (
                        height - middle_rect[3] * 6) / 2,
                        middle_rect[2] * 8,
                        middle_rect[3] * 6)

dest_about_rect = ((    width - basic_background_rect[2] - middle_rect[2] * 8) / 2, (
                        height - middle_rect[3] * 6) / 2,
                        middle_rect[2] * 8,
                        middle_rect[3] * 6)

# Define rectangles
dealer_rect_1 = (middle_rect[0], card_rect[3] / 3, card_rect[2], card_rect[3])
dealer_rect_2 = (middle_rect[0] + 75 * scale_ratio, card_rect[3] / 3, card_rect[2], card_rect[3])
dealer_rect_3 = (middle_rect[0] - 75 * scale_ratio, card_rect[3] / 3, card_rect[2], card_rect[3])
dealer_rect_4 = (middle_rect[0] - 75 * scale_ratio * 2, card_rect[3] / 3, card_rect[2], card_rect[3])
dealer_rect_5 = (middle_rect[0] - 75 * scale_ratio * 3, card_rect[3] / 3, card_rect[2], card_rect[3])
player_rect_1 = (middle_rect[0] - 53 * scale_ratio * 2, middle_rect[1], card_rect[2], card_rect[3])
player_rect_2 = (middle_rect[0] - 53 * scale_ratio, middle_rect[1] - card_rect[3] / 3, card_rect[2], card_rect[3])
player_rect_3 = (middle_rect[0], middle_rect[1] - 2 * card_rect[3] / 3, card_rect[2], card_rect[3])
player_rect_4 = (middle_rect[0] + 53 * scale_ratio, middle_rect[1] - 3 * card_rect[3] / 3, card_rect[2], card_rect[3])
player_rect_5 = (middle_rect[0] + 53 * scale_ratio * 2, middle_rect[1] - 4 * card_rect[3] / 3, card_rect[2], card_rect[3])

# Define card placement dictionary
card_place_deal = {}
card_place_play = {}
card_place_deal["place_deal_1"] = dealer_rect_1
card_place_deal["place_deal_2"] = dealer_rect_2
card_place_deal["place_deal_3"] = dealer_rect_3
card_place_deal["place_deal_4"] = dealer_rect_4
card_place_deal["place_deal_5"] = dealer_rect_5
card_place_play["place_play_1"] = player_rect_1
card_place_play["place_play_2"] = player_rect_2
card_place_play["place_play_3"] = player_rect_3
card_place_play["place_play_4"] = player_rect_4
card_place_play["place_play_5"] = player_rect_5

# Define split rectangles and split dictionary
player_split_1 = (middle_rect[0] - 53 * scale_ratio * 3, middle_rect[1], card_rect[2], card_rect[3])
player_split_2 = (middle_rect[0] - 53 * scale_ratio * 2, middle_rect[1] - card_rect[3] / 3, card_rect[2], card_rect[3])
player_split_3 = (middle_rect[0] - 53 * scale_ratio, middle_rect[1] - 2 * card_rect[3] / 3, card_rect[2], card_rect[3])
player_split_4 = (middle_rect[0], middle_rect[1] - 3 * card_rect[3] / 3, card_rect[2], card_rect[3])
player_split_5 = (middle_rect[0] + 53 * scale_ratio, middle_rect[1] - 4 * (card_rect[3] / 3), card_rect[2], card_rect[3])
player_split_6 = (middle_rect[0] - 53 * scale_ratio, middle_rect[1], card_rect[2], card_rect[3])
player_split_7 = (middle_rect[0], middle_rect[1] - card_rect[3] / 3, card_rect[2], card_rect[3])
player_split_8 = (middle_rect[0] + 53 * scale_ratio, middle_rect[1] - 2 * card_rect[3] / 3, card_rect[2], card_rect[3])
player_split_9 = (middle_rect[0] + 53 * scale_ratio * 2, middle_rect[1] - 3 * card_rect[3] / 3, card_rect[2], card_rect[3])
player_split_10 = (middle_rect[0] + 53 * scale_ratio * 3, middle_rect[1] - 4 * card_rect[3] / 3, card_rect[2], card_rect[3])

card_place_split = {}
card_place_split["place_split_1"] = player_split_1
card_place_split["place_split_2"] = player_split_2
card_place_split["place_split_3"] = player_split_3
card_place_split["place_split_4"] = player_split_4
card_place_split["place_split_5"] = player_split_5
card_place_split["place_split_6"] = player_split_6
card_place_split["place_split_7"] = player_split_7
card_place_split["place_split_8"] = player_split_8
card_place_split["place_split_9"] = player_split_9
card_place_split["place_split_10"] = player_split_10

# Define button rectangles
stand_button_rect = pygame.Rect(    middle_rect[0] - card_rect[3] * 2, 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
hit_button_rect = pygame.Rect(      middle_rect[0] - card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
double_button_rect = pygame.Rect(   middle_rect[0], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
triple_button_rect = pygame.Rect(   middle_rect[0] + card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
split_button_rect = pygame.Rect(    middle_rect[0] + card_rect[3] * 2, 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2], 
                                    card_rect[2] / 3.3)
yes_button_rect = pygame.Rect(      middle_rect[0] - card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2], 
                                    card_rect[2] / 3.3)
no_button_rect = pygame.Rect(       middle_rect[0] + card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2], 
                                    card_rect[2] / 3.3)
new_button_rect = pygame.Rect(      middle_rect[0] - card_rect[3] * 2, 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2], 
                                    card_rect[2] / 3.3)
shortcuts_button_rect = pygame.Rect(middle_rect[0] - card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
rules_button_rect = pygame.Rect(    middle_rect[0], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
about_button_rect = pygame.Rect(    middle_rect[0] + card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
quit_button_rect = pygame.Rect(     middle_rect[0] + card_rect[3] * 2, 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)

# Define text rectangles for buttons
text_stand_grey = font_button.render("Stand", True, black, grey)
text_stand_dark_grey = font_button.render("Stand", True, black, dark_grey)
stand_rect = text_stand_grey.get_rect(center = (    stand_button_rect[0] + card_rect[2] / 2, 
                                                    stand_button_rect[1] + stand_button_rect[3] / 2.1))

text_hit_grey = font_button.render("Hit", True, black, grey)
text_hit_dark_grey = font_button.render("Hit", True, black, dark_grey)
hit_rect = text_hit_grey.get_rect(center = (    hit_button_rect[0] + card_rect[2] / 2, 
                                                hit_button_rect[1] + hit_button_rect[3] / 2.1))

text_double_grey = font_button.render("Double", True, black, grey)
text_double_dark_grey = font_button.render("Double", True, black, dark_grey)
double_rect = text_double_grey.get_rect(center = (  double_button_rect[0] + card_rect[2] / 2, 
                                                    double_button_rect[1] + double_button_rect[3] / 2.1))

text_triple_grey = font_button.render("Triple", True, black, grey)
text_triple_dark_grey = font_button.render("Triple", True, black, dark_grey)
triple_rect = text_triple_grey.get_rect(center = (  triple_button_rect[0] + card_rect[2] / 2, 
                                                    triple_button_rect[1] + triple_button_rect[3] / 2.1))

text_split_grey = font_button.render("Split", True, black, grey)
text_split_dark_grey = font_button.render("Split", True, black, dark_grey)
split_rect = text_split_grey.get_rect(center = (    split_button_rect[0] + card_rect[2] / 2, 
                                                    split_button_rect[1] + split_button_rect[3] / 2.1))

text_yes_grey = font_button.render("Yes", True, black, grey)
text_yes_dark_grey = font_button.render("Yes", True, black, dark_grey)
yes_rect = text_yes_grey.get_rect(center = (    yes_button_rect[0] + card_rect[2] / 2, 
                                                yes_button_rect[1] + yes_button_rect[3] / 2.1))

text_no_grey = font_button.render("No", True, black, grey)
text_no_dark_grey = font_button.render("No", True, black, dark_grey)
no_rect = text_no_grey.get_rect(center = (  no_button_rect[0] + card_rect[2] / 2, 
                                            no_button_rect[1] + no_button_rect[3] / 2.1))

text_new_grey = font_button.render("New Game", True, black, grey)
text_new_dark_grey = font_button.render("New Game", True, black, dark_grey)
new_rect = text_new_grey.get_rect(center = (    new_button_rect[0] + card_rect[2] / 2, 
                                                new_button_rect[1] + new_button_rect[3] / 2.1))

text_shortcuts_grey = font_button.render("Shortcuts", True, black, grey)
text_shortcuts_dark_grey = font_button.render("Shortcuts", True, black, dark_grey)
shortcuts_rect = text_shortcuts_grey.get_rect(center = (    shortcuts_button_rect[0] + card_rect[2] / 2, 
                                                            shortcuts_button_rect[1] + shortcuts_button_rect[3] / 2.1))

text_rules_grey = font_button.render("Rules", True, black, grey)
text_rules_dark_grey = font_button.render("Rules", True, black, dark_grey)
rules_rect = text_rules_grey.get_rect(center = (    rules_button_rect[0] + card_rect[2] / 2, 
                                                    rules_button_rect[1] + rules_button_rect[3] / 2.1))

text_about_grey = font_button.render("About", True, black, grey)
text_about_dark_grey = font_button.render("About", True, black, dark_grey)
about_rect = text_about_grey.get_rect(center = (    about_button_rect[0] + card_rect[2] / 2, 
                                                    about_button_rect[1] + about_button_rect[3] / 2.1))

text_quit_grey = font_button.render("Quit", True, black, grey)
text_quit_dark_grey = font_button.render("Quit", True, black, dark_grey)
quit_rect = text_quit_grey.get_rect(center = (  quit_button_rect[0] + card_rect[2] / 2, 
                                                quit_button_rect[1] + quit_button_rect[3] / 2.1))
                                                
# Define text for main menu
scrolling_shortcuts_list = [    "Keyboard Shortcuts:"," ",
                                "S - Stand",
                                "H - Hit",
                                "D - Double Down",
                                "T - Triple Down",
                                "V - Split"," ",
                                "Y - Yes for Insurance",
                                "N - No for Insurance"," ",
                                "N - New Game on Main Menu",
                                "A - Change Animation Speed",
                                "B - Change Bet Amount",
                                "F - Toggle Fullscreen",
                                "Q - Quit to Main Menu",
                                "(...and assess High Score)"," ",
                                "Esc - Quit Game"]

scrolling_rules_list = [    "House Rules for this table that benefit the Player:"," ",
                            "The deck is only 1 deck.",
                            "Blackjack pays 3 to 2.",
                            "An unnatural Blackjack (after Split) pays 3 to 2.",
                            "Suited Blackjack pays 2 to 1.",
                            "Split allowed on any Pair.",
                            "Any 10 value card is considered a Pair.",
                            "Double Down on any card total.",
                            "Double or Triple Down allowed after Split.",
                            "Maximum Dealer or Player cards is 5.",
                            "5 cards dealt without bust (Charlie) wins...",
                            "unless Dealer has Blackjack.",
                            "Five-Card Charlie allowed after Split.",
                            "Five-Card Charlie pays 2 to 1.",
                            "777 wins outright and pays 3 to 1."," "," "," "," "," "," "," ",
                            
                            "House Rules for this table that benefit the Dealer:"," ",
                            "Dealer hits on soft 17.",
                            "$10 Min. Bet and $50 Max. Bet",
                            "Blackjack wins immediately unless...",
                            "the Dealer also has one, then result is push.",
                            "No-Peak table means the Dealer...",
                            "won't check for Blackjack till Player is done.",
                            "Split allowed only after the first deal.",
                            "Triple down only on Hard 9, 10, or 11.",
                            "Double or Triple down not allowed after Hit.",
                            "Insurance allowed only after the first deal.",
                            "Insurance pays 2 to 1 but costs half initial Bet.",
                            "Surrender is not allowed."]
                            

scrolling_about_list = [    "Blackjack! made using:"," ",
                            "Python 3.13.2",
                            "Pygame 2.6.1"," ",
                            "Blackjack Font provided free by:",
                            "Typadelic Fonts COPYRIGHT 2002"," ",
                            'Card images by "Sleepy"',
                            'Basic strategy by "Josias"'," ",
                            "Sound by https://freesound.org"," ",
                            '"Sensation Rag" - 1908',
                            "Music Composed by Joseph F. Lamb",
                            "Arranged by Scott Joplin",
                            "MIDI Sequenced By Colin D. MacDonald",
                            "https://www.ragtimemusic.com",]





