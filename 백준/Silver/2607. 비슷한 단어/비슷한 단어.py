import sys
input = sys.stdin.readline

N = int(input())
total = 0
base_str = list(input().rstrip())

for i in range(N-1):
    check = 0
    compare = base_str[:]
    now = list(input().rstrip())
    for n in now:
        if n in compare:
            compare.remove(n)
        else:
            check +=1
    
    if check <2 and len(compare)<2:
        total+=1


print(total)