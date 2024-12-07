N = int(input())

now = 1
stk = []
operation_stk = []
success = True

for _ in range(N):
    goal = int(input())
    while now<=goal:
        stk.append(now)
        now += 1
        operation_stk.append("+")
    if stk and stk[-1] == goal:
        stk.pop()
        operation_stk.append("-")
    else:
        success=False
        break
if stk:
    print("NO")
else:
    for operation in operation_stk:
        print(operation)