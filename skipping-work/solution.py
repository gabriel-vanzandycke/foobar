def solution(x, y):
    x = set(x)
    y = set(y)
    return ((y-x) or (x-y)).pop()
