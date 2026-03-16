import random

HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]

def flip_coin():
    return random.choice(COIN_VALUES)

def play_martingale(starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_lose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        #print("=======")
        steps_to_lose += 1
        current_funds -= current_bet
        #print(f"current_funds {current_funds} current_bet {current_bet}")
        flip_coin_value = flip_coin()
        if flip_coin_value == HEADS:
            win = current_bet * 2
            #print(f"{win=}")
            current_funds += win
            current_bet = min_bet
        else:
            #print('loose')
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
        #print("=======")
    return steps_to_lose

def simulate_martingale_for_n_players(starting_funds, min_bet, max_bet, n_games) -> float:
    total_steps_to_lose = 0
    for i in range(n_games):
        steps_to_lose = play_martingale(starting_funds, min_bet, max_bet)
        total_steps_to_lose += steps_to_lose

    return total_steps_to_lose / n_games

print(simulate_martingale_for_n_players(10, 100000, 1, 100000))