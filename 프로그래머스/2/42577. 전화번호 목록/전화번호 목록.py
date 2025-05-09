# phobe_book 딕셔너리를 생성
# 앞글자 같은 것끼리 묶기 -> 정렬 필요함.
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True