from itertools import combinations, product
from bisect import bisect_left

# 6**5 = 7776
def dice_sum_combination(dice_list):
    return [sum(p) for p in product(*dice_list)]
    
def solution(dice):
    N = len(dice)
    # 10C5 = 252
    dice_combination_lists = list(combinations(list(range(N)),N//2))
    
    max_winnings = 0
    max_combinations = []
    
    for combination in dice_combination_lists:
        a_dice_sum = dice_sum_combination(list(map(lambda i: dice[i], combination)))
        b_dice_sum = sorted(dice_sum_combination(list(map(lambda i: dice[i], filter(lambda x: x not in combination, range(N))))))
        
        wins = sum(bisect_left(b_dice_sum, a_sum) for a_sum in a_dice_sum)
        if wins > max_winnings:
            max_winnings = wins
            max_combinations = combination
    
    return [idx + 1 for idx in max_combinations]