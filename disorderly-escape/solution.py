import itertools
# disordered-escape
w, h = 2, 2
s = 3
def solution(w, h, s):
    cache = {}
    def f(w, h, s, verbose=False):
        count = 0
        if s in cache:
            return cache[s]
        for c in itertools.combinations_with_replacement(range(s), w*h):
            print(c)
            l = len(set(c))
            if l == 1:
                count += 1
                continue
            counts = list(sorted([c.count(x) for x in range(s)]))
            if l == 2 and counts[0] == 1:
                count += 1
            elif l == 3 and counts[0] == 1 and counts[1] == 1:
                count += 3
            elif l != s:
                count += f(w, h, l)
            else:
                not verbose or print(c)
        cache[s] = count
        print("caching", cache)
        return count
    count = 0
    for s2 in range(1, s):
        count += f(w, h, s2, True)
    return count
solution(w, h, s)


#  0 0
#  0 0

#  0 0   0 0   0 1   1 0   # 4 equivalent states
#  0 1   1 0   0 0   0 0

#  0 0   1 1    # 2 equivalent states
#  1 1   0 0

#  0 1   1 0    # 2 equivalent states
#  1 0   0 1

#  0 1   1 0    # 2 equivalent states
#  0 1   1 0

#  1 1   1 1   1 0   0 1   # 4 equivalent states
#  0 1   1 0   1 1   1 1

#  1 1
#  1 1


