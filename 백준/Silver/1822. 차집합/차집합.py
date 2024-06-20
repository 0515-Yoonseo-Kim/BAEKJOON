A,B = map(int,input().split())

set_A = set(input().split())
set_B = set(input().split())

diff = set_A - set_B
print(len(diff))
print(*sorted([int(i) for i in diff]))