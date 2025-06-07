import random
import itertools

ranks = "23456789TJQKA"
suits = "cdhs"

def card_str(card_tuple):
    return card_tuple[0] + card_tuple[1]

def generate_all_flops():
    deck = [r + s for r in ranks for s in suits]
    flops = list(itertools.combinations(deck, 3))
    return [list(flop) for flop in flops]

def generate_flops_by_type(flop_type, sample_count):
    all_flops = generate_all_flops()
    filtered = []

    for flop in all_flops:
        ranks_only = [card[0] for card in flop]
        suits_only = [card[1] for card in flop]
        unique_ranks = set(ranks_only)
        unique_suits = set(suits_only)

        sorted_ranks = sorted([ranks.index(r) for r in ranks_only])
        is_connected = max(sorted_ranks) - min(sorted_ranks) <= 4
        is_paired = len(unique_ranks) <= 2
        is_monotone = len(unique_suits) == 1
        is_suited = len(unique_suits) == 2
        is_rainbow = len(unique_suits) == 3
        high = any(r in 'AKQJT' for r in ranks_only)
        middle = all(r in '89T' for r in ranks_only)
        low = all(r in '23456' for r in ranks_only)

        if flop_type == "High Card / Rainbow" and high and is_rainbow and not is_connected:
            filtered.append(flop)
        elif flop_type == "High Card / Suited" and high and is_suited:
            filtered.append(flop)
        elif flop_type == "Middle Connected / Rainbow" and is_connected and middle and is_rainbow:
            filtered.append(flop)
        elif flop_type == "Middle Connected / Suited" and is_connected and middle and is_suited:
            filtered.append(flop)
        elif flop_type == "Low Card Dry" and low and is_rainbow and not is_connected:
            filtered.append(flop)
        elif flop_type == "Paired Board" and is_paired:
            filtered.append(flop)
        elif flop_type == "Monotone" and is_monotone:
            filtered.append(flop)

    return random.sample(filtered, min(sample_count, len(filtered)))
