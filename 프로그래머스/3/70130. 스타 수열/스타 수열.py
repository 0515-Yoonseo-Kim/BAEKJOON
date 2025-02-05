from collections import Counter

def solution(a):
    target_dict = Counter(a)
    max_length = 0

    for target in target_dict:
        if target_dict[target] * 2 <= max_length:
            continue
        length = 0
        i = 0
        while i < len(a) - 1:
            if (a[i] == target or a[i+1] == target) and a[i] != a[i+1]:
                length += 2
                i += 2
                continue
            i += 1

        max_length = max(max_length, length)

    return max_length
