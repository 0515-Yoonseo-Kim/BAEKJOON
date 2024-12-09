import sys,math
from collections import Counter
input = sys.stdin.readline

N = int(input())

num_li = [int(input()) for _ in range(N)]
num_li.sort()
print(round(sum(num_li)/N))
print(num_li[N//2])
num_freq = Counter(num_li)
max_freq = max(Counter(num_li).values())
max_freq_keys = [k for k,v in num_freq.items() if v == max_freq]
max_freq_keys.sort()
if len(max_freq_keys) > 1:
    print(max_freq_keys[1])
else:
    print(max_freq_keys[0])
print(max(num_li)-min(num_li))