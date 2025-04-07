# 크기가 같은 거를 최대한 많이 쓰고 싶음.
from collections import Counter
def solution(k, tangerine):
    tangerine_count = Counter(tangerine)
    kind = 0
    cnt = 0
    for v in sorted(tangerine_count.values(),reverse=True):
        cnt += v
        kind += 1
        if cnt >= k:
            break
    return kind