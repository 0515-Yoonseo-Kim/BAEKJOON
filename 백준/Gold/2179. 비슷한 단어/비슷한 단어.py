import sys
input = sys.stdin.readline
N = int(input())
word_dict = {input().rstrip() : 0 for _ in range(N)} # word_dict : k -> word , value -> 겹치는 접두사의 최대 길이

word_sorted_list = sorted([word for word in word_dict])

def word_compare(w1,w2):
    l = min(len(w1), len(w2))
    cnt = 0
    for i in range(l):
        if w1[i] == w2[i]:
            cnt += 1
        else:
            return cnt
    return cnt

max_cnt = 0

for i in range(N-1):
    w1, w2 = word_sorted_list[i], word_sorted_list[i+1]
    cnt = word_compare(w1,w2)
    word_dict[w1] = max(word_dict[w1],cnt)
    word_dict[w2] = max(word_dict[w2],cnt)
    max_cnt = max(max_cnt,cnt)
            
max_words = list(filter(lambda item: item[1] == max_cnt, word_dict.items()))
word1 = max_words[0][0]
word2 = ""

for word in max_words[1:]:
    word = word[0]
    if word1[:max_cnt] == word[:max_cnt]:
        word2 = word
        break
print(word1)
print(word2)