from itertools import permutations

def solution(k, dungeons):
    max_count = 0

    for perm in permutations(dungeons):
        fatigue = k
        count = 0
        for need, use in perm:
            if fatigue >= need:
                fatigue -= use
                count += 1
            else:
                break
        max_count = max(max_count, count)

    return max_count
