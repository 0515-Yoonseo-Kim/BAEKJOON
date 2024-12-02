'''def solution(dots):
    x_set, y_set = set(), set()
    for dot in dots:
        x,y = dot
        x_set.add(x)
        y_set.add(y)
    return abs(x_set.pop()-x_set.pop())*abs(y_set.pop()-y_set.pop())'''

def solution(dots):
    x_diff = max(dots)[0]-min(dots)[0]
    y_diff = max(dots)[1]-min(dots)[1]
    return x_diff*y_diff