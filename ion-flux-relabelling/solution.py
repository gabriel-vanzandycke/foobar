#                     31
#       15                            30
#   7          14             22              29
# 3   6    10     13      18      21      25      28
#1 2 4 5  8  9  11  12  16  17  19  20  23  24  26  27

def solution(n):
    if (n+1) & n == 0:      # top left tree:  n+1 is a power of 2
        return (n << 1) + 1
    if (n+2) & (n+1) == 0:  # top right tree: n+2 is a power of 2
        return n+1
    p = 2**((n+1).bit_length()-1)-1 # greatest power of 2 minus 1 below n
    return solution((n & p) +1) + p # solution of same position on the left tree

tests = {1: 3, 2: 3, 3: 7, 4: 6, 5: 6, 6: 7, 7: 15, 8: 10, 9: 10, 10: 14, 11: 13, 12: 13, 13: 14, 14: 15, 15: 31, 16: 18, 17: 18, 18: 22, 19: 21, 20: 21, 21: 22, 22: 30, 23: 25, 24: 25, 25: 29, 26: 28, 27: 28, 28: 29, 29: 30, 30: 31}
for n, s in tests.items():
    assert solution(n) == s, f"Failed for solution({n}) == {s}. Received {solution(n)}"
