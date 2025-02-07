N = int(input())

num_li = list(map(int,input().split()))
stk = []
answer = []
for i in range(N-1,-1,-1):

    while stk and num_li[i] >= stk[-1]:
        stk.pop()

    if not stk:
        answer.append(-1)
    else:
        answer.append(stk[-1])
    stk.append(num_li[i])

print(*answer[::-1])