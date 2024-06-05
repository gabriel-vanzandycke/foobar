#  . . .
#  . O X
#  . X X


# . O . .
# . . O .
# . . . O
# O . . .

# O . O
# . O .
# O . O


# 0 .
# . 0
#====

# 0 . 0    0 . .    0 . .   0 . .   0 . .
# . . 0    . . .    . . 0   . . .   . . .
# . . .    . . 0    . . .   . 0 .   . . 0

# 0 . 0    0 . .    0 . .   0 . .   0 . .
# . . 0    . . .    . . 0   . . .   . . .
# 0 0 .    0 0 .    . . .   . 0 .   . . 0


# . 0
# . .

# . .
# . 0

# . .
# 0 .
import copy

def solution(g):
    W, H = len(g[0]), len(g)
    s = [[None]*(W+1)]*(H+1)
    for i in range(W+1):
        for j in range(H+1):
            if s[i][j] is not None:
                continue
            if g[i][j] == 1:

            s[i][j] = 1 if g[i][j] + g[i+1][j] + g[i][j+1] + g[i+1][j+1] == 1 else 0

from collections import defaultdict
d = defaultdict(list)
for i in range(2**(9+1)-1):
    key = tuple([((i & m) & (i & m -1) == 0) for m in [
        int('0b110110000', 2),
        int('0b011011000', 2),
        int('0b000110110', 2),
        int('0b000011011', 2),
    ]])
    print(key)
    d[key].append(i)

for k in d.keys():
    f = lambda b: "1" if b else "."
    print(f"{f(k[0])} {f(k[1])}\n{f(k[2])} {f(k[3])}\t{len(d[k])}\n")

print(bin(sum([len(d[k]) for k in d.keys()])))
