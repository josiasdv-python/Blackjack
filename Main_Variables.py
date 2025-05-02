
# Define starting cash
player_coins = 500
high_score = 500

# Define bet current, next, and cycle
bet_current = 10
bet_next = 10
bet_cycle = [25, 50, 10]

# Define animation speed
animation_speed = 60
animation_cycle = [90, 30, 60]

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
