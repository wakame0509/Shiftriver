import eval7
import random
from itertools import combinations

def generate_flops_by_type(flop_type):
    deck = list(eval7.DECK)
    flops = []

    for combo in combinations(deck, 3):
        ranks = [card.rank for card in combo]
        suits = [card.suit for card in combo]
        unique_ranks = set(ranks)
        unique_suits = set(suits)

        if flop_type == "ミドルペア＋2スート":
            if len(unique_ranks) == 2 and max(ranks) <= 'J' and len(unique_suits) == 2:
                flops.append(list(combo))

        elif flop_type == "ノーヒット＋2スート":
            if len(unique_ranks) == 3 and len(unique_suits) == 2 and all(r < 'J' for r in ranks):
                flops.append(list(combo))

        elif flop_type == "ローカードドライ":
            if len(unique_ranks) == 3 and len(unique_suits) == 3 and all(r in '5432' for r in ranks):
                flops.append(list(combo))

        elif flop_type == "トップヒット＋スート":
            if len(unique_ranks) == 3 and 'A' in ranks and len(unique_suits) == 2:
                flops.append(list(combo))

        elif flop_type == "ガットショット＋スート":
            int_ranks = [card._rank for card in combo]
            int_ranks.sort()
            if len(set(int_ranks)) == 3 and int_ranks[2] - int_ranks[0] == 4 and len(unique_suits) == 2:
                flops.append(list(combo))

        elif flop_type == "オーバーカード＋スート":
            if all(r in 'AKQJ' for r in ranks) and len(unique_suits) == 2:
                flops.append(list(combo))

        elif flop_type == "セミコネクター＋2スート":
            int_ranks = sorted([card._rank for card in combo])
            if int_ranks[2] - int_ranks[0] == 2 and len(unique_suits) == 2:
                flops.append(list(combo))

    return flops
