import sys
input = sys.stdin.readline

#N,M-> 두 집합의 원소의 개수 
string = input().rstrip()
string_len = len(string)
set_str = set()
for i in range(1,string_len+1):
    for j in range(string_len+1-i):
        set_str.add(string[j:j+i])
        

print(len(set_str))