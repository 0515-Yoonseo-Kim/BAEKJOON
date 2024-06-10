def solution(n, times):
    max_time = max(times)*n
    left, right=0, max_time
    while left<=right:
        mid = (left+right)//2
        total = sum([mid//time for time in times])
        
        if total < n:
            left = mid +1
        else:
            right = mid -1        
    return left