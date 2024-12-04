from collections import defaultdict
S = input()
P = input()

cnt = 1
temp = ""

for p in P:
    temp += p
    if temp in S:
        continue
    else:
        temp = p
        cnt += 1


print(cnt)