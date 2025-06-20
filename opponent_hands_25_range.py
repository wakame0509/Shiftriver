# opponent_hand_combos_25_range.py

opponent_hand_combos = [
    # Pocket Pairs (10 hands × 6 combos = 60)
    ['Ah', 'Ad'], ['Ah', 'Ac'], ['Ah', 'As'], ['Ad', 'Ac'], ['Ad', 'As'], ['Ac', 'As'],
    ['Kh', 'Kd'], ['Kh', 'Kc'], ['Kh', 'Ks'], ['Kd', 'Kc'], ['Kd', 'Ks'], ['Kc', 'Ks'],
    ['Qh', 'Qd'], ['Qh', 'Qc'], ['Qh', 'Qs'], ['Qd', 'Qc'], ['Qd', 'Qs'], ['Qc', 'Qs'],
    ['Jh', 'Jd'], ['Jh', 'Jc'], ['Jh', 'Js'], ['Jd', 'Jc'], ['Jd', 'Js'], ['Jc', 'Js'],
    ['Th', 'Td'], ['Th', 'Tc'], ['Th', 'Ts'], ['Td', 'Tc'], ['Td', 'Ts'], ['Tc', 'Ts'],
    ['9h', '9d'], ['9h', '9c'], ['9h', '9s'], ['9d', '9c'], ['9d', '9s'], ['9c', '9s'],
    ['8h', '8d'], ['8h', '8c'], ['8h', '8s'], ['8d', '8c'], ['8d', '8s'], ['8c', '8s'],
    ['7h', '7d'], ['7h', '7c'], ['7h', '7s'], ['7d', '7c'], ['7d', '7s'], ['7c', '7s'],
    ['6h', '6d'], ['6h', '6c'], ['6h', '6s'], ['6d', '6c'], ['6d', '6s'], ['6c', '6s'],
    ['5h', '5d'], ['5h', '5c'], ['5h', '5s'], ['5d', '5c'], ['5d', '5s'], ['5c', '5s'],

    # Suited Hands (14 hands × 4 = 56)
    ['Ah', 'Kh'], ['Ad', 'Kd'], ['Ac', 'Kc'], ['As', 'Ks'],
    ['Ah', 'Qh'], ['Ad', 'Qd'], ['Ac', 'Qc'], ['As', 'Qs'],
    ['Ah', 'Jh'], ['Ad', 'Jd'], ['Ac', 'Jc'], ['As', 'Js'],
    ['Ah', 'Th'], ['Ad', 'Td'], ['Ac', 'Tc'], ['As', 'Ts'],
    ['Kh', 'Qh'], ['Kd', 'Qd'], ['Kc', 'Qc'], ['Ks', 'Qs'],
    ['Kh', 'Jh'], ['Kd', 'Jd'], ['Kc', 'Jc'], ['Ks', 'Js'],
    ['Qh', 'Jh'], ['Qd', 'Jd'], ['Qc', 'Jc'], ['Qs', 'Js'],
    ['Jh', 'Th'], ['Jd', 'Td'], ['Jc', 'Tc'], ['Js', 'Ts'],
    ['Th', '9h'], ['Td', '9d'], ['Tc', '9c'], ['Ts', '9s'],
    ['9h', '8h'], ['9d', '8d'], ['9c', '8c'], ['9s', '8s'],
    ['8h', '7h'], ['8d', '7d'], ['8c', '7c'], ['8s', '7s'],
    ['7h', '6h'], ['7d', '6d'], ['7c', '6c'], ['7s', '6s'],
    ['6h', '5h'], ['6d', '5d'], ['6c', '5c'], ['6s', '5s'],
    ['5h', '4h'], ['5d', '4d'], ['5c', '4c'], ['5s', '4s'],

    # Offsuit Hands (7 hands × 13 = 92)
    ['Ah', 'Kd'], ['Ah', 'Kc'], ['Ah', 'Ks'], ['Ad', 'Kh'], ['Ad', 'Kc'], ['Ad', 'Ks'], ['Ac', 'Kh'], ['Ac', 'Kd'], ['Ac', 'Ks'], ['As', 'Kh'], ['As', 'Kd'], ['As', 'Kc'], ['Kd', 'Ah'],
    ['Ah', 'Qd'], ['Ah', 'Qc'], ['Ah', 'Qs'], ['Ad', 'Qh'], ['Ad', 'Qc'], ['Ad', 'Qs'], ['Ac', 'Qh'], ['Ac', 'Qd'], ['Ac', 'Qs'], ['As', 'Qh'], ['As', 'Qd'], ['As', 'Qc'], ['Qd', 'Ah'],
    ['Ah', 'Jd'], ['Ah', 'Jc'], ['Ah', 'Js'], ['Ad', 'Jh'], ['Ad', 'Jc'], ['Ad', 'Js'], ['Ac', 'Jh'], ['Ac', 'Jd'], ['Ac', 'Js'], ['As', 'Jh'], ['As', 'Jd'], ['As', 'Jc'], ['Jd', 'Ah'],
    ['Kh', 'Qd'], ['Kh', 'Qc'], ['Kh', 'Qs'], ['Kd', 'Qh'], ['Kd', 'Qc'], ['Kd', 'Qs'], ['Kc', 'Qh'], ['Kc', 'Qd'], ['Kc', 'Qs'], ['Ks', 'Qh'], ['Ks', 'Qd'], ['Ks', 'Qc'], ['Qd', 'Kh'],
    ['Kh', 'Jd'], ['Kh', 'Jc'], ['Kh', 'Js'], ['Kd', 'Jh'], ['Kd', 'Jc'], ['Kd', 'Js'], ['Kc', 'Jh'], ['Kc', 'Jd'], ['Kc', 'Js'], ['Ks', 'Jh'], ['Ks', 'Jd'], ['Ks', 'Jc'], ['Jd', 'Kh'],
    ['Qh', 'Jd'], ['Qh', 'Jc'], ['Qh', 'Js'], ['Qd', 'Jh'], ['Qd', 'Jc'], ['Qd', 'Js'], ['Qc', 'Jh'], ['Qc', 'Jd'], ['Qc', 'Js'], ['Qs', 'Jh'], ['Qs', 'Jd'], ['Qs', 'Jc'], ['Jd', 'Qh'],
    ['Jh', 'Td'], ['Jh', 'Tc'], ['Jh', 'Ts'], ['Jd', 'Th'], ['Jd', 'Tc'], ['Jd', 'Ts'], ['Jc', 'Th'], ['Jc', 'Td'], ['Jc', 'Ts'], ['Js', 'Th'], ['Js', 'Td'], ['Js', 'Tc'], ['Td', 'Jh'],
]
