import pygame
import os

# Initialize Pygame
pygame.init()

# Set up scaling
scale_ratio = 1

# Set up display
width, height = pygame.display.Info().current_w * 3/4, pygame.display.Info().current_h * 3/4
screen = pygame.display.set_mode([width, height], pygame.SCALED)
# width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
# screen = pygame.display.set_mode([width, height], pygame.FULLSCREEN)
# width, height = 1080, 620
# screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
screen_rect = screen.get_rect()

# Define colors and font
black = (0, 0, 0)
light_black = (64, 64, 64)
white = (255, 255, 255)
grey = (239, 239, 232)
dark_grey = (187, 187, 175)
green = (0, 91, 19)
light_blue = (205, 244, 255)
blue = (86, 205, 236)
dark_blue = (100, 187, 199)
orange = (243, 172, 36)
light_orange = (248, 204, 118)
transparent = (0, 128, 255)
font = pygame.font.Font(os.path.join("Assets", "CalibriBold.ttf"), int(26 * scale_ratio))
font_button = pygame.font.Font(os.path.join("Assets", "CalibriBold.ttf"), int(13 * scale_ratio))
font_options = pygame.font.Font(os.path.join("Assets", "CalibriBold.ttf"), int(16 * scale_ratio))
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

# Default basic strategy image
basic_strategy = pygame.image.load(os.path.join("Assets", "BasicStrategy2Deck.png")).convert()
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

dest_shortcuts_rect = ( card_rect[2],
                        card_rect[2] / 2,
                        width - (basic_background_rect[2] + card_rect[2] * 2),
                        height - card_rect[2])

dest_options_rect = (   card_rect[2],
                        card_rect[2] / 2,
                        width - (basic_background_rect[2] + card_rect[2] * 2),
                        height - card_rect[2])

dest_about_rect = (     card_rect[2],
                        card_rect[2] / 2,
                        width - (basic_background_rect[2] + card_rect[2] * 2),
                        height - card_rect[2])

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
bet10_button_rect = pygame.Rect(    middle_rect[0] - card_rect[3] * 2, 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
bet25_button_rect = pygame.Rect(    middle_rect[0] - card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
bet50_button_rect = pygame.Rect(    middle_rect[0], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
bet100_button_rect = pygame.Rect(   middle_rect[0] + card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
bet250_button_rect = pygame.Rect(   middle_rect[0] + card_rect[3] * 2, 
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
options_button_rect = pygame.Rect(  middle_rect[0], 
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
confirm_button_rect = pygame.Rect(  middle_rect[0] - card_rect[3], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
default_button_rect = pygame.Rect(  middle_rect[0], 
                                    height - card_rect[2] * 1.05, 
                                    card_rect[2],
                                    card_rect[2] / 3.3)
cancel_button_rect = pygame.Rect(   middle_rect[0] + card_rect[3], 
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

text_bet10_grey = font_button.render("$10", True, black, grey)
text_bet10_dark_grey = font_button.render("$10", True, black, dark_grey)
bet10_rect = text_bet10_grey.get_rect(center = (    bet10_button_rect[0] + card_rect[2] / 2, 
                                                    bet10_button_rect[1] + bet10_button_rect[3] / 2.1))

text_bet25_grey = font_button.render("$25", True, black, grey)
text_bet25_dark_grey = font_button.render("$25", True, black, dark_grey)
bet25_rect = text_bet25_grey.get_rect(center = (    bet25_button_rect[0] + card_rect[2] / 2, 
                                                    bet25_button_rect[1] + bet25_button_rect[3] / 2.1))

text_bet50_grey = font_button.render("$50", True, black, grey)
text_bet50_dark_grey = font_button.render("$50", True, black, dark_grey)
bet50_rect = text_bet50_grey.get_rect(center = (    bet50_button_rect[0] + card_rect[2] / 2, 
                                                    bet50_button_rect[1] + bet50_button_rect[3] / 2.1))

text_bet100_grey = font_button.render("$100", True, black, grey)
text_bet100_dark_grey = font_button.render("$100", True, black, dark_grey)
bet100_rect = text_bet100_grey.get_rect(center = (  bet100_button_rect[0] + card_rect[2] / 2, 
                                                    bet100_button_rect[1] + bet100_button_rect[3] / 2.1))

text_bet250_grey = font_button.render("$250", True, black, grey)
text_bet250_dark_grey = font_button.render("$250", True, black, dark_grey)
bet250_rect = text_bet250_grey.get_rect(center = (  bet250_button_rect[0] + card_rect[2] / 2, 
                                                    bet250_button_rect[1] + bet250_button_rect[3] / 2.1))

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

text_options_grey = font_button.render("Options", True, black, grey)
text_options_dark_grey = font_button.render("Options", True, black, dark_grey)
options_rect = text_options_grey.get_rect(center = (    options_button_rect[0] + card_rect[2] / 2, 
                                                    options_button_rect[1] + options_button_rect[3] / 2.1))

text_about_grey = font_button.render("About", True, black, grey)
text_about_dark_grey = font_button.render("About", True, black, dark_grey)
about_rect = text_about_grey.get_rect(center = (    about_button_rect[0] + card_rect[2] / 2, 
                                                    about_button_rect[1] + about_button_rect[3] / 2.1))

text_quit_grey = font_button.render("Quit", True, black, grey)
text_quit_dark_grey = font_button.render("Quit", True, black, dark_grey)
quit_rect = text_quit_grey.get_rect(center = (  quit_button_rect[0] + card_rect[2] / 2, 
                                                quit_button_rect[1] + quit_button_rect[3] / 2.1))

text_confirm_grey = font_button.render("Confirm", True, black, grey)
text_confirm_dark_grey = font_button.render("Confirm", True, black, dark_grey)
confirm_rect = text_confirm_grey.get_rect(center = (    confirm_button_rect[0] + card_rect[2] / 2, 
                                                        confirm_button_rect[1] + confirm_button_rect[3] / 2.1))

text_default_grey = font_button.render("Default", True, black, grey)
text_default_dark_grey = font_button.render("Default", True, black, dark_grey)
default_rect = text_default_grey.get_rect(center = (    default_button_rect[0] + card_rect[2] / 2, 
                                                        default_button_rect[1] + default_button_rect[3] / 2.1))

text_cancel_grey = font_button.render("Cancel", True, black, grey)
text_cancel_dark_grey = font_button.render("Cancel", True, black, dark_grey)
cancel_rect = text_cancel_grey.get_rect(center = (  cancel_button_rect[0] + card_rect[2] / 2, 
                                                    cancel_button_rect[1] + cancel_button_rect[3] / 2.1))


# Define text for main menu
scrolling_shortcuts_list = [    "Keyboard Shortcuts:",
                                "Use Up or Down to manually Scroll"," ",
                                "Set Number of Decks with 1-8 (Only on Main Menu)",
                                "N - New Game (Only on Main Menu)"," ",
                                "S - Stand",
                                "H - Hit",
                                "D - Double Down",
                                "T - Triple Down",
                                "V - Split"," ",
                                "Y - Yes for Insurance",
                                "N - No for Insurance"," ",
                                "A - Change Animation Speed",
                                "B - Change Default Bet Amount",
                                "C - Toggle True Card Count",
                                "F - Toggle Fullscreen",
                                "P - Toggle Continuous Play"," ",
                                "Q - Quit to Main Menu",
                                "Esc - Quit Game",
                                "(Q, Esc, and Close Window will assess High Score)"]

scrolling_about_list = [    "House Rules for this Table that benefit the Player:"," ",
                            "Blackjack pays 3 to 2.",
                            "Unnatural Blackjack (after Split) pays 3 to 2.",
                            "Suited Blackjack pays 2 to 1.",
                            "Split allowed on any Pair.",
                            "Any 10 value card is considered a Pair.",
                            "Double Down on any card total.",
                            "Double or Triple Down allowed after Split.",
                            "Maximum Dealer or Player cards is 5.",
                            "5 Player cards dealt without bust (Charlie)...",
                            "wins unless Dealer has Blackjack.",
                            "Five-Card Charlie allowed after Split.",
                            "Five-Card Charlie pays 2 to 1.",
                            "777 wins outright and pays 3 to 1."," "," "," "," "," ",
                            
                            "House Rules for this Table that benefit the Dealer:"," ",
                            "Dealer hits on Soft 17.",
                            "$10 Min. Bet and $250 Max. Bet (Low Spread)",
                            "Player Blackjack wins immediately unless...",
                            "Dealer also has one, then result is a Push.",
                            "No-Peek Table means the Dealer...",
                            "won't check for Blackjack till Player is done.",
                            "Split allowed only after the first deal.",
                            "Triple Down only on Hard 9, 10, or 11.",
                            "Double or Triple Down not allowed after Hit.",
                            "Insurance allowed only after the first deal.",
                            "Insurance pays 2 to 1 but costs half initial Bet.",
                            "Surrender is not allowed."," "," "," "," "," ",
                            
                            "Blackjack! made using:"," ",
                            "Python 3.13.2",
                            "Pygame 2.6.1"," ",
                            "Blackjack Font provided free by:",
                            "Typadelic Fonts Copyright ©2002"," ",
                            'Card images by "Sleepy"',
                            'Basic Strategy images by "Josias"',
                            "(referencing https://wizardofodds.com)"," ",
                            "Sound by https://freesound.org"," ",
                            '"Sensation Rag" - 1908',
                            "Music Composed by Joseph F. Lamb",
                            "Arranged by Scott Joplin",
                            "MIDI Sequenced By Colin D. MacDonald",
                            "https://ragtimemusic.com"]

# Define text and rects for all the options text
text_1 = font_options.render("1", True, white, light_black)                                               
text_2 = font_options.render("2", True, white, light_black)
text_3 = font_options.render("3", True, white, light_black)
text_4 = font_options.render("4", True, white, light_black)
text_5 = font_options.render("5", True, white, light_black)
text_6 = font_options.render("6", True, white, light_black)
text_7 = font_options.render("7", True, white, light_black)                                            
text_8 = font_options.render("8", True, white, light_black)
text_decks_in_shoe = font_options.render("Decks in Shoe", True, white, light_black)

text_slow = font_options.render("Slow", True, white, light_black)
text_medium = font_options.render("Medium", True, white, light_black)
text_fast = font_options.render("Fast", True, white, light_black)
text_animation_speed = font_options.render("Animation Speed", True, white, light_black)

text_10 = font_options.render("$10", True, white, light_black)
text_25 = font_options.render("$25", True, white, light_black)
text_50 = font_options.render("$50", True, white, light_black)
text_100 = font_options.render("$100", True, white, light_black)
text_250 = font_options.render("$250", True, white, light_black)
text_default_bet = font_options.render("Default Bet Amount", True, white, light_black)

text_on_1 = font_options.render("On", True, white, light_black)
text_off_1 = font_options.render("Off", True, white, light_black)
text_true_count = font_options.render("True Card Count", True, white, light_black)
text_on_2 = font_options.render("On", True, white, light_black)
text_off_2 = font_options.render("Off", True, white, light_black)
text_fullscreen = font_options.render("Fullscreen", True, white, light_black)
text_on_3 = font_options.render("On", True, white, light_black)
text_off_3 = font_options.render("Off", True, white, light_black)
text_continuous_play = font_options.render("Continuous Play", True, white, light_black)

text_options = font.render("Options", True, white, black)

text_all_rect = text_fast.get_rect(center = ((  width - basic_background_rect[2]) / 2, 
                                                screen_rect.centery - 1))

# Define highlight box rects for options screen
highlight_box_1 = pygame.Rect(0, 0, 20, 20)
highlight_box_1.center = (text_all_rect[0] - card_rect[2] * 1.4 - 1, screen_rect.centery - card_rect[2] * 3)
highlight_box_2 = pygame.Rect(0, 0, 20, 20)
highlight_box_2.center = (text_all_rect[0] - card_rect[2] * .7, screen_rect.centery - card_rect[2] * 3)
highlight_box_3 = pygame.Rect(0, 0, 20, 20)
highlight_box_3.center = (text_all_rect[0], screen_rect.centery - card_rect[2] * 3)
highlight_box_4 = pygame.Rect(0, 0, 20, 20)
highlight_box_4.center = (text_all_rect[0] + card_rect[2] * .7 - 1, screen_rect.centery - card_rect[2] * 3)
highlight_box_5 = pygame.Rect(0, 0, 20, 20)
highlight_box_5.center = (text_all_rect[0] + card_rect[2] * 1.4, screen_rect.centery - card_rect[2] * 3)
highlight_box_6 = pygame.Rect(0, 0, 20, 20)
highlight_box_6.center = (text_all_rect[0] + card_rect[2] * 2.1, screen_rect.centery - card_rect[2] * 3)
highlight_box_7 = pygame.Rect(0, 0, 20, 20)
highlight_box_7.center = (text_all_rect[0] + card_rect[2] * 2.8 - 1, screen_rect.centery - card_rect[2] * 3)
highlight_box_8 = pygame.Rect(0, 0, 20, 20)
highlight_box_8.center = (text_all_rect[0] + card_rect[2] * 3.5 - 1, screen_rect.centery - card_rect[2] * 3)

highlight_box_9 = pygame.Rect(0, 0, 20, 20)
highlight_box_9.center = (text_all_rect[0] - card_rect[2] * 1.4 - 1, screen_rect.centery - card_rect[2] * 2)
highlight_box_10 = pygame.Rect(0, 0, 20, 20)
highlight_box_10.center = (text_all_rect[0] - card_rect[2] * .4 - 1, screen_rect.centery - card_rect[2] * 2)
highlight_box_11 = pygame.Rect(0, 0, 20, 20)
highlight_box_11.center = (text_all_rect[0] + card_rect[2] * .9 - 1, screen_rect.centery - card_rect[2] * 2)

highlight_box_12 = pygame.Rect(0, 0, 20, 20)
highlight_box_12.center = (text_all_rect[0] - card_rect[2] * 1.4 - 1, screen_rect.centery - card_rect[2])
highlight_box_13 = pygame.Rect(0, 0, 20, 20)
highlight_box_13.center = (text_all_rect[0] - card_rect[2] * .4 - 1, screen_rect.centery - card_rect[2])
highlight_box_14 = pygame.Rect(0, 0, 20, 20)
highlight_box_14.center = (text_all_rect[0] + card_rect[2] * .6 - 1, screen_rect.centery - card_rect[2])
highlight_box_15 = pygame.Rect(0, 0, 20, 20)
highlight_box_15.center = (text_all_rect[0] + card_rect[2] * 1.6 - 1, screen_rect.centery - card_rect[2])
highlight_box_16 = pygame.Rect(0, 0, 20, 20)
highlight_box_16.center = (text_all_rect[0] + card_rect[2] * 2.6 - 1, screen_rect.centery - card_rect[2])

highlight_box_17 = pygame.Rect(0, 0, 20, 20)
highlight_box_17.center = (text_all_rect[0] - card_rect[2] * 1.4 - 1, screen_rect.centery)
highlight_box_18 = pygame.Rect(0, 0, 20, 20)
highlight_box_18.center = (text_all_rect[0] - card_rect[2] * .4 - 1, screen_rect.centery)
highlight_box_19 = pygame.Rect(0, 0, 20, 20)
highlight_box_19.center = (text_all_rect[0] - card_rect[2] * 1.4 - 1, screen_rect.centery + card_rect[2])
highlight_box_20 = pygame.Rect(0, 0, 20, 20)
highlight_box_20.center = (text_all_rect[0] - card_rect[2] * .4 - 1, screen_rect.centery + card_rect[2])
highlight_box_21 = pygame.Rect(0, 0, 20, 20)
highlight_box_21.center = (text_all_rect[0] - card_rect[2] * 1.4 - 1, screen_rect.centery + card_rect[2] * 2)
highlight_box_22 = pygame.Rect(0, 0, 20, 20)
highlight_box_22.center = (text_all_rect[0] - card_rect[2] * .4 - 1, screen_rect.centery + card_rect[2] * 2)

