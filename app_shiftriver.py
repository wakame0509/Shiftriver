import streamlit as st
from calculate_winrate_detailed_v2 import simulate_shift_river
from flop_generator import generate_flops_by_type
import pandas as pd

st.title("ShiftRiver（リバーの勝率変動分析）")

# 169通りのスターティングハンド（自分用）
all_starting_hands = [
    f"{r1}{r2}s" if i < j else f"{r1}{r2}o" if i > j else f"{r1}{r2}"
    for i, r1 in enumerate("AKQJT98765432")
    for j, r2 in enumerate("AKQJT98765432")
]

# 自分のハンド選択
hand = st.selectbox("自分のハンドを選択", all_starting_hands)

# フロップタイプ選択
flop_type = st.selectbox(
    "フロップタイプを選択",
    [
        "High Card Dry",
        "High Card Wet",
        "Middle Connected",
        "Paired Board",
        "Monotone",
        "Two Tone",
        "Low Card Dry",
    ]
)

# フロップの枚数選択（10枚 / 20枚 / 30枚）
num_flops = st.selectbox("使用するフロップの数を選択", [10, 20, 30])

# 実行ボタン
if st.button("ShiftRiverを実行"):
    st.write("計算中です。少々お待ちください...")

    # 指定されたタイプに基づいてランダムなフロップを生成
    selected_flops = generate_flops_by_type(flop_type, num_flops)

    # シミュレーション実行
    result_df = simulate_shift_river(hand, selected_flops)

    # 結果表示
    st.dataframe(result_df)

    # CSV保存リンク
    csv = result_df.to_csv(index=False).encode('utf-8')
    st.download_button("CSVとして保存", csv, f"shift_river_{hand}_{flop_type}.csv", "text/csv")
