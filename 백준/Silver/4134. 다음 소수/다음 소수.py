import sys
import math
input = sys.stdin.readline

T = int(input())

def not_prime(N):
    check = int(math.sqrt(N))+1
    for i in range(2,check):
        if N%i==0:
            return True
    return False


for _ in range(T):
    N = int(input())
    if N == 0 or N == 1:
        N = 2
    else:
        while not_prime(N):
            N+=1
    print(N)
            