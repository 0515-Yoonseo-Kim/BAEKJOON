import sys
input = sys.stdin.readline

T = int(input())
def gcd(a,b):
    common=1
    max_common = 1
    while common<=a and common<=b:
        if a%common == 0 and b%common == 0:
            max_common = common
        common+=1
    return max_common
def lcm(a,b):
    gcd__ = gcd(a,b)
    a = a//gcd__
    b = b//gcd__
    return a*b*gcd__

for _ in range(T):
    A, B = map(int,input().split())
    print(lcm(A,B))
    pass
