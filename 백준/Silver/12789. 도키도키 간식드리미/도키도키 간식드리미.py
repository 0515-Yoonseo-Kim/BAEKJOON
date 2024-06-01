from collections import deque
N = int(input())
lines = deque(list(map(int,input().split())))
stk = []

idx=1
while True:
    if not lines and not stk:
        print("Nice")
        break
    if idx in lines:
        now = lines.popleft()
    else:
        if stk and stk[-1]==idx:
            now = stk.pop()
        else:
            print("Sad")
            break

    if now == idx:
        idx+=1
        continue
    else:
        stk.append(now)
