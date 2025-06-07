def extract_river_features(board, hand, river_card):
    """
    リバーのカードによって変化する特徴量を抽出する
    """
    features = []

    # セットが完成する（手札のペアと同じカードがリバーに落ちた）
    if hand[0][0] == hand[1][0] and river_card[0] == hand[0][0]:
        features.append("Set")

    # フルハウス/フォーカードの可能性（ボードで2ペアやスリーカード）
    ranks_on_board = [card[0] for card in board] + [river_card[0]]
    rank_counts = {rank: ranks_on_board.count(rank) for rank in set(ranks_on_board)}
    if any(count >= 3 for count in rank_counts.values()):
        features.append("FullHouseOrQuads")

    # ストレート完成（簡易チェック：A2345〜TJQKA）
    straight_sequences = [
        "A2345", "23456", "34567", "45678", "56789",
        "6789T", "789TJ", "89TJQ", "9TJQK", "TJQKA"
    ]
    ranks_order = "A23456789TJQK"
    all_ranks = set(card[0] for card in board + [river_card] + hand)
    for seq in straight_sequences:
        if all(rank in all_ranks for rank in seq):
            features.append("Straight")
            break

    # フラッシュ完成
    suits = [card[1] for card in board] + [river_card]
    for suit in "hdcs":
        if suits.count(suit) >= 5:
            features.append("Flush")
            break

    # オーバーカード（リバーに手札よりも高いランクのカード）
    hand_ranks = sorted([card[0] for card in hand], key=lambda x: "23456789TJQKA".index(x))
    if river_card[0] > max(hand_ranks, key=lambda x: "23456789TJQKA".index(x)):
        features.append("Overcard")

    return features
