import sys
input = sys.stdin.readline

def check_palindreome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome(word):
    if len(word) == 1:
        return 0
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            if check_palindreome(word[left+1:right+1]) or check_palindreome(word[left:right]):
                return 1
            return 2
        left += 1
        right -= 1
    return 0
    

T = int(input())

for _ in range(T):
    print(is_palindrome(input().rstrip()))
