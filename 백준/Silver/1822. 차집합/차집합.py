A,B = map(int,input().split())

set_A = set(map(int,input().split()))
set_B = set(map(int,input().split()))

diff = set_A - set_B
print(len(diff))
print(*sorted(diff))