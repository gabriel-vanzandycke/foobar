def solution(s):
    r = 0
    count = 0
    for c in s:
        if c == '>':
            r += 1
        if c == '<':
            count += r
    return count * 2

assert solution("--->-><-><-->-") == 10
assert solution("<>") == 0
assert solution("<<>><") == 4
assert solution(">----<") == 2
