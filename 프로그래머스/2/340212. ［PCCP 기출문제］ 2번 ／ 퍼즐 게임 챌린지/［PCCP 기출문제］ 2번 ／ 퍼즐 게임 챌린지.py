from typing import List
def puzzle_time(diffs:List[int],times:List[int],level: int) -> int:
    time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            time += times[i]
        else:
            time += (diffs[i]-level)*(times[i]+times[i-1]) + times[i]   
    return time

def solution(diffs, times, limit):
    left,right = 0, 100000
    total = 0
    while left+1 < right:
        mid = (left+right)//2
        total = puzzle_time(diffs,times,mid)
        if total < limit:
            right = mid
        elif total > limit:
            left = mid
        else:
            return mid
    return right