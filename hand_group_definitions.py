# スターティングハンドを12のハンドグループに分類
hand_groups = {
    "High Pair": ["AA", "KK", "QQ", "JJ"],
    "Mid Pair": ["TT", "99", "88", "77"],
    "Low Pair": ["66", "55", "44", "33", "22"],

    "Broadway Suited": ["AKs", "AQs", "AJs", "ATs", "KQs", "KJs", "QJs", "JTs"],
    "Broadway Offsuit": ["AKo", "AQo", "AJo", "KQo", "KJo", "QJo", "JTo"],

    "Suited Connectors": ["T9s", "98s", "87s", "76s", "65s", "54s"],
    "Offsuit Connectors": ["T9o", "98o", "87o", "76o", "65o", "54o"],

    "Suited One-Gappers": ["97s", "86s", "75s", "64s", "53s"],
    "Offsuit One-Gappers": ["97o", "86o", "75o", "64o", "53o"],

    "Suited Aces": ["A5s", "A4s", "A3s", "A2s"],
    "Offsuit Aces": ["A5o", "A4o", "A3o", "A2o"],

    "Others": ["K9s", "Q9s", "J9s", "T8s", "96s", "85s", "74s", "63s", "52s", "42s", "32s"]
}

def classify_hand(hand):
    """
    169通りのハンド（例：AKs, 87oなど）をグループ名に分類して返す
    """
    for group_name, hands in hand_groups.items():
        if hand in hands:
            return group_name
    return "Others"
