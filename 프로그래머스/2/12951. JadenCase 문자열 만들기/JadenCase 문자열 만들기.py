def convert_to_jaden(word: str):
    word = word.lower()
    if word and word[0].isalpha():
        word = word[0].upper() + word[1:]
    return word

def solution(s):
    words = s.split(" ")  # split with " " to keep all spaces
    answer = " ".join(convert_to_jaden(word) for word in words)
    return answer
