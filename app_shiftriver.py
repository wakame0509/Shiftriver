import streamlit as st
import eval7
import random
from itertools import combinations
from calculate_winrate_detailed_v2 import simulate_shift_river_average
from hand_list import all_starting_hands
from flop_generator import generate_flops_by_type
from opponent_25_combo import opponent_hand_combos  # 展開済み25%レンジ

st.title("ShiftRiver - ターン→リバー 勝率変動分析")

hand_str = st.selectbox("自分のハンドを選択", all_starting_hands)

flop_type = st.selectbox("フロップタイプを選択", [
    "ミドルペア＋2スート", "ノーヒット＋2スート", "ローカードドライ",
    "トップヒット＋スート", "ガットショット＋スート",
    "オーバーカード＋スート", "セミコネクター＋2スート"
])

num_flops = st.selectbox("使用するフロップの数", [10, 20, 30])

if st.button("ShiftRiverを実行"):
    # 自分のハンド展開
    ranks = hand_str[:2]
    suited = hand_str.endswith("s")
    offsuit = hand_str.endswith("o")
    combos = []

    suits = ['h', 'd', 'c', 's']
    if suited:
        for s in suits:
            combos.append([eval7.Card(ranks[0] + s), eval7.Card(ranks[1] + s)])
    elif offsuit:
        for s1 in suits:
            for s2 in suits:
                if s1 != s2:
                    combos.append([eval7.Card(ranks[0] + s1), eval7.Card(ranks[1] + s2)])
    else:  # ペア
        for i in range(len(suits)):
            for j in range(i + 1, len(suits)):
                combos.append([eval7.Card(ranks[0] + suits[i]), eval7.Card(ranks[0] + suits[j])])

    hero_hand = random.choice(combos)  # 代表として1組

    # フロップ抽出
    flops = generate_flops_by_type(flop_type)
    selected_flops = random.sample(flops, min(num_flops, len(flops)))

    # 各フロップに対してターンを展開
    flop_turn_combos = []
    for flop in selected_flops:
        used = set(flop + hero_hand)
        deck = [card for card in eval7.DECK if card not in used]
        for turn in deck:
            if turn not in flop:
                flop_turn_combos.append(flop + [turn])

    with st.spinner("ShiftRiver 計算中..."):
        results = simulate_shift_river_average(hero_hand, flop_turn_combos, [
            [eval7.Card(c1), eval7.Card(c2)] for c1, c2 in opponent_hand_combos
        ])

    for result in results:
        st.write(f"### フロップ＋ターン: {' '.join(result['base_board'])}")
        st.write(f"平均勝率: {result['avg_winrate']}")
        st.write("勝率上昇トップ10:")
        st.table(result['top10'])
        st.write("勝率下降ワースト10:")
        st.table(result['worst10'])
