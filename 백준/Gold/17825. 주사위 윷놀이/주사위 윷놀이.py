board = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

scores = [0, 2, 4, 6, 8,
          10, 12, 14, 16, 18,
          20, 22, 24, 26, 28,
          30, 32, 34, 36, 38,
          40, 13, 16, 19, 25,
          22, 24, 28, 27, 26,
          30, 35, 0]

dice_rolls = list(map(int, input().split()))
max_score = 0


def move(current_pos, dice_value):
    if current_pos == 32:
        return 32

    # 첫 이동
    next_pos = board[current_pos][1] if len(board[current_pos]) == 2 else board[current_pos][0]

    # 남은 주사위 값만큼 이동
    for _ in range(1, dice_value):
        if next_pos == 32:  # 도착 지점 도달
            break
        next_pos = board[next_pos][0]

    return next_pos


def backtracking(turn, current_score, piece_positions):
    global max_score

    if turn == len(dice_rolls):
        max_score = max(max_score, current_score)
        return

    dice_value = dice_rolls[turn]

    for i in range(4):  # 각 말을 선택
        current_pos = piece_positions[i]
        if current_pos == 32:  # 이미 도착한 경우 이동 불가
            continue
        next_pos = move(current_pos, dice_value)
        if next_pos != 32 and next_pos in piece_positions:
            continue

        # 상태 갱신 후 백트래킹 호출
        previous_pos = piece_positions[i]
        piece_positions[i] = next_pos
        backtracking(turn + 1, current_score + scores[next_pos], piece_positions)

        # 상태 복원
        piece_positions[i] = previous_pos


backtracking(0, 0, [0, 0, 0, 0])
print(max_score)
