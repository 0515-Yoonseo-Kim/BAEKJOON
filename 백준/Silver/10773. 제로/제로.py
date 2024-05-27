
N = int(input())
stk = []

for _ in range(N):
    now = int(input())
    if now == 0:
        stk.pop()
    else:
        stk.append(now)

print(sum(stk))

