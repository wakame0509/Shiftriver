import eval7
import random
from collections import Counter

def evaluate_hand_strength(hand, board, opponent_hands):
    wins = 0
    ties = 0
    total = 0

    hand_eval = hand + board
    hand_value = eval7.evaluate(hand_eval)

    for opp in opponent_hands:
        opp_eval = opp + board
        opp_value = eval7.evaluate(opp_eval)
        if hand_value > opp_value:
            wins += 1
        elif hand_value == opp_value:
            ties += 1
        total += 1

    return (wins + ties / 2) / total if total > 0 else 0

def simulate_shift_river_average(hand, flop_turn_combos, opponent_hands):
    from itertools import combinations

    shift_results = []

    for flop_turn in flop_turn_combos:
        used = set(flop_turn + hand)
        deck = [card for card in eval7.DECK if card not in used]

        river_cards = list(combinations(deck, 1))
        river_winrates = {}

        for river in river_cards:
            full_board = flop_turn + list(river)
            winrate = evaluate_hand_strength(hand, full_board, opponent_hands)
            river_card_str = river[0].__str__()
            river_winrates[river_card_str] = winrate

        # 現在のフロップ＋ターンにおける平均勝率
        avg_winrate = sum(river_winrates.values()) / len(river_winrates)

        # ランキング表示用の差分
        deltas = {
            card: round(win - avg_winrate, 4) for card, win in river_winrates.items()
        }

        sorted_deltas = sorted(deltas.items(), key=lambda x: x[1], reverse=True)
        top10 = sorted_deltas[:10]
        worst10 = sorted_deltas[-10:]

        shift_results.append({
            "base_board": [card.__str__() for card in flop_turn],
            "avg_winrate": round(avg_winrate, 4),
            "top10": top10,
            "worst10": worst10
        })

    return shift_results
