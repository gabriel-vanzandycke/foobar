# shortest path algorithm in a directed graph with negative edge weights
def bellman_ford(times, s):
    N = len(times)
    distances = [None]*N
    path = [[] for _ in distances]
    distances[s] = 0
    for i in range((N*(N-1))//2-1, 0, -1):
        for x, xdist in enumerate(distances):
            if xdist is None:
                continue
            for y, ydist in enumerate(distances):
                w = times[x][y]
                if  ydist is None or xdist + w < ydist:
                    if i == 1:
                        raise
                    distances[y] = xdist + w
                    path[y].append(x)
    return distances, path

def solution(times, time_limit):
    N = len(times)
    visited = set()
    missing = set(range(1, N-1))
    nodes = range(N)
    try:
        times, paths = zip(*[bellman_ford(times, s) for s in nodes])
    except:
        return [n-1 for n in missing]
    
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

