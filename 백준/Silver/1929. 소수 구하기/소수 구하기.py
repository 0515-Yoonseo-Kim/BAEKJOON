import sys
import math
input = sys.stdin.readline

M, N = map(int,input().split())
if M == 1:
    M = 2
def is_prime(num):
    check = int(math.sqrt(num))+1
    for i in range(2,check):
        if num%i == 0:
            return False
    return True
prime_list = []

for num in range(M,N+1):
    if is_prime(num):
        prime_list.append(num)
        
for prime in prime_list:
    print(prime)
