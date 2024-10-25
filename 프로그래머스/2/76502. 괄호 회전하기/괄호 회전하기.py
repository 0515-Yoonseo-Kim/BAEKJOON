def is_correct(string):
    stack = []
    paren_combi = {")": "(", "]": "[", "}": "{"}
    for s in string:
        if s in paren_combi.values():  # 열린 괄호일 때
            stack.append(s)
        elif s in paren_combi.keys():  # 닫는 괄호일 때
            if stack and stack[-1] == paren_combi[s]:
                stack.pop()  # 스택에서 짝이 맞는 괄호 제거
            else:
                return False
    return len(stack) == 0  # 모든 괄호가 짝을 이루었는지 확인

def solution(string):
    answer = 0
    for i in range(len(string)):
        case_string = string[i:] + string[:i]
        if is_correct(case_string):
            answer += 1
    return answer
