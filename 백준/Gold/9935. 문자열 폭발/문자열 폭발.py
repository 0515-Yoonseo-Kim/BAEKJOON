# 백준 / 문자열 폭발(9935)
import sys
import re
input = sys.stdin.readline

string = input().rstrip()
explosion = list(input().rstrip())
target = len(explosion)
stk = []

for s in string:
    stk.append(s)
    
    while len(stk)>=target and stk[-target:]==explosion:
        del stk[-target:]

print("".join(stk) if stk else "FRULA")