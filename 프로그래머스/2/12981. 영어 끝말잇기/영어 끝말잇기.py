# 한 번 나왔던 단어는 다시 나와서는 안 됨 -> set
# idx를 알아야 함. -> enumerate
def solution(n, words):
    word_set = set()
    for idx, word in enumerate(words):
        if idx > 0:
            prev = words[idx-1]
            if word in word_set or prev[-1] != word[0]:
                return [(idx%n)+1,(idx//n)+1]
        word_set.add(word)
    return [0,0]