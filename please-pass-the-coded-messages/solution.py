import itertools
def solution(l):
    l = sorted(l)[::-1]
    for length in range(len(l), 0, -1):
        for l2 in itertools.combinations(l, length):
            if sum(l2) % 3 == 0:
                return int(''.join(map(str, sorted(l2)[::-1])))
    return 0
