import sys
input = sys.stdin.readline


def gcd(a,b):
    # 유클리우드 호제법
    while b!=0:
        a,b = b, a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)

N = int(input())
trees = []

for _ in range(N):
    trees.append(int(input()))
trees.sort()
diff = []
for i in range(N-1):
    diff.append(trees[i+1]-trees[i])

gcd_now = gcd(diff[0],diff[1])

for i in range(N-1):

    gcd_now = gcd(gcd_now,diff[i])


cnt = 0
for d in diff:
    cnt+=(d//gcd_now-1)

print(cnt)