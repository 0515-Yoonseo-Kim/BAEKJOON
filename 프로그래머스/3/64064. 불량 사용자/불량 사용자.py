from itertools import permutations

def is_match(user, banned):
    """유저 ID가 밴 아이디 패턴과 매칭되는지 확인하는 함수"""
    if len(user) != len(banned):
        return False
    for uc, bc in zip(user, banned):
        if bc != '*' and uc != bc:
            return False
    return True

def solution(user_id, banned_id):
    possible_cases = {idx: set() for idx in range(len(banned_id))}
    
    # 각 banned_id에 해당하는 가능한 user_id 찾기
    for user in user_id:
        for idx, banned in enumerate(banned_id):
            if is_match(user, banned):
                possible_cases[idx].add(user)

    # 가능한 조합 찾기
    unique_sets = set()
    
    for perm in permutations(user_id, len(banned_id)):
        if all(perm[i] in possible_cases[i] for i in range(len(banned_id))):
            unique_sets.add(frozenset(perm))  # 중복 방지

    return len(unique_sets)
