import sys
input =sys.stdin.readline


N = int(input())

for _ in range(N):
    pString = [s for s in input().rstrip()]
    right = []
    result = "YES"

    while pString:
        now = pString.pop()
        if now == ")":
            right.append(now)
        else:
            if not right:
                result = "NO"
            else:
                right.pop()

    if len(right)>0:
        result = "NO"

    print(result)
                
