def solution(n):

    odd_answer=sum([i for i in range(1,n+1) if i%2==n%2])
    even_answer=sum([i**2 for i in range(1,n+1) if i%2==n%2])
    return odd_answer if n%2 else even_answer