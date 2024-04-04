import sys
import math
input = sys.stdin.readline

N = int(input())
num = 1
while num**2 <= N:
    
    num+=1
    
print(num-1)