# 한 번 나왔던 단어는 다시 나와서는 안 됨 -> set
# idx를 알아야 함. -> enumerate
def solution(n, words):
    word_set = set()
    last_word=""
    for idx,word in enumerate(words):
        if idx == 0:
            word_set.add(word)
            last_word=word[-1]
            continue
        if last_word != word[0] or word in word_set:
            return idx%n + 1, idx//n+1
        word_set.add(word)
        last_word=word[-1]
    return [0,0]