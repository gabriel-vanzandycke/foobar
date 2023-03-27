import math

def bellman_ford(times, s):
    N = len(times)
    nodes = range(N)
    distance = [math.inf]*N
    path = [[] for _ in nodes]
    distance[s] = 0
    for i in range((N*(N-1))//2, 0, -1):
        for x in nodes:
            for y in nodes:
                w = times[x][y]
                if distance[x] + w < distance[y]:
                    if i == 1:
                        return None
                    distance[y] = distance[x] + w
                    path[y].append(x)
    return distance, path

def solution(times, time_limit):
    N = len(times)
    visited = set()
    missing = set(range(1, N-1))
    nodes = range(N)
    output = zip(*[bellman_ford(times, s) for s in nodes])
    if output is None:
        return [n-1 for n in missing]
    times, paths = output
    
    start = 0
    bulkhead = N-1
    while missing:
        node, time = min({n: times[start][n] + times[n][bulkhead] for n in missing}.items(), key=lambda kv: kv[1])
        if time_limit - time < 0:
            break
        path = set([b for b in paths[start][node] + [node] if 0 < b < bulkhead])
        visited = visited.union(path)
        missing -= path
        time_limit -= times[start][node]
        start = node
    return [n-1 for n in visited]

assert solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1) == [1, 2]
assert solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3) == [0, 1]

