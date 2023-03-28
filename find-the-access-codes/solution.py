from collections import defaultdict
def solution(l):
    count = 0
    cache = defaultdict(list)
    for i in range(len(l)):
        for j in cache.get(i, range(i+1, len(l))):
            if l[j] % l[i] == 0:
                if j in cache:
                    count += len(cache[j])
                else:
                    for k in range(j+1, len(l)):
                        if l[k] % l[j] == 0:
                            count += 1
                            cache[j].append(k)
    return count
