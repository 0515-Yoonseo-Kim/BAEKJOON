from collections import deque
import sys
input = sys.stdin.readline

card = deque([i for i in range(1,int(input())+1)])
while card:
    now = card.popleft()
    if not card:
        print(now)
    if card:
        top = card.popleft()
        card.append(top)


