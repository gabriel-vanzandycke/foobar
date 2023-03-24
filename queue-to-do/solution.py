# 17 18 19 20 /
# 21 22 23 / 24
# 25 26 / 27 28
# 29 / 30 31 32

# 0 1 2 /
# 3 4 / 5
# 6 / 7 8

#  0  1  2  3  4  /
#  5  6  7  8  /  9
# 10 11 12  / 13 14
# 15 16  / 17 18 19
# 20  / 21 22 23 24

def f(i):
    if (i+0) % 4 == 0: return i
    if (i+1) % 4 == 0: return 0
    if (i+2) % 4 == 0: return i+1
    if (i+3) % 4 == 0: return 1

def solution(start, length):
    total = 0
    for i in range(length, 0, -1):
        total = total^f(start-1+i)^f(start-1)
        start += length
    return total
print(solution(17, 4))
print(solution(0, 3))
print(0^1^2^3^4^6)
