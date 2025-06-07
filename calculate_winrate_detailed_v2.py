import eval7
import random
import pandas as pd
from opponent_hand_combos import opponent_hand_combos
from hand_utils import convert_hand_notation, classify_card_features

def simulate_winrate(hero_hand, board, num_simulations=500):
    hero = convert_hand_notation(hero_hand)
    wins = 0

    for _ in range(num_simulations):
        deck = eval7.Deck()
        used = set(hero + board)
        deck.cards = [card for card in deck.cards if str(card) not in used]

        opp_hand = random.choice(opponent_hand_combos)
        opp = [eval7.Card(c) for c in opp_hand if c not in used]
        if len(opp) != 2:
            continue

        full_board = [eval7.Card(c) for c in board]
        deck.shuffle()
        while len(full_board) < 5:
            next_card = deck.peek()
            if str(next_card) in used:
                deck.shuffle()
                continue
            full_board.append(next_card)

        hero_score = eval7.evaluate(hero + full_board)
        opp_score = eval7.evaluate(opp + full_board)
        if hero_score > opp_score:
            wins += 1
        elif hero_score == opp_score:
            wins += 0.5

    return 100 * wins / num_simulations

def simulate_shift_river_and_save(hero_hand, flop_type, num_flops=10):
    from flop_generator import generate_flops_by_type

    flops = generate_flops_by_type(flop_type, num_flops)
    results = []

    for flop in flops:
        deck = eval7.Deck()
        used = set(hero_hand) | set(flop)
        deck.cards = [card for card in deck.cards if str(card) not in used]
        deck.shuffle()

        turn_card = None
        for card in deck:
            if str(card) not in used:
                turn_card = str(card)
                break

        four_board = flop + [turn_card]
        river_candidates = [str(c) for c in deck if str(c) not in four_board]

        for river in river_candidates:
            full_board = four_board + [river]
            winrate = simulate_winrate(hero_hand, full_board, num_simulations=500)
            features = classify_card_features(river, hero_hand, full_board[:-1])
            results.append({
                'river': river,
                'winrate': winrate,
                'feature': features,
                'flop': " ".join(flop),
                'turn': turn_card
            })

    df = pd.DataFrame(results)
    avg_shift = df['winrate'].mean()
    df.to_csv(f"shift_river_{hero_hand}_{flop_type}.csv", index=False)
    return avg_shift, df
