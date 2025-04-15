from collections import defaultdict
from math import prod
def solution(clothes):
    closet = defaultdict(int)
    for v,k in clothes:
        closet[k] += 1
    closet_values = list(map(lambda x: x+1,closet.values()))
    return prod(closet_values) - 1