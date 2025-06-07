from itertools import combinations
import random

def generate_flop_turn_combinations(num_flops=10):
    """
    指定された数のフロップ（3枚）と、それぞれに対するターン（1枚）を生成し、
    フロップ＋ターン（合計4枚）の組み合わせリストを返す。
    num_flops: 使用するフロップ数（10, 20, 30など）
    """
    ranks = '23456789TJQKA'
    suits = 'hdcs'
    deck = [r + s for r in ranks for s in suits]

    flop_turn_sets = []

    attempts = 0
    max_attempts = 10000

    while len(flop_turn_sets) < num_flops and attempts < max_attempts:
        attempts += 1
        flop = random.sample(deck, 3)
        remaining = [c for c in deck if c not in flop]
        turn = random.choice(remaining)
        flop_turn = flop + [turn]

        # 重複排除
        if sorted(flop_turn) not in [sorted(ft) for ft in flop_turn_sets]:
            flop_turn_sets.append(flop_turn)

    return flop_turn_sets
