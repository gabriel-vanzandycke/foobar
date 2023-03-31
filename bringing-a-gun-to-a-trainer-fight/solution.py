import math as fractions
from tqdm.auto import tqdm

def evaluate(offsetx, offsety, positions, distance):
    for x, y in positions:
        x, y = x + offsetx, y + offsety
        if x**2 + y**2 <= distance**2:
            yield x, y

def simplify(u, v):
    gcd = abs(fractions.gcd(u, v)) or 1
    return u//gcd, v//gcd

def solution(dimensions, your_position, trainer_position, distance):
    w, h = dimensions
    W, H = w*2, h*2
    x, y = your_position
    positive_positions = [
        (  trainer_position[0]-x ,   trainer_position[1]-y ),
        (W-trainer_position[0]-x ,   trainer_position[1]-y ),
        (  trainer_position[0]-x , H-trainer_position[1]-y ),
        (W-trainer_position[0]-x , H-trainer_position[1]-y ),
    ]
    negative_positions = [(0, 0), (W-2*x, 0), (0, H-2*y), (W-2*x, H-2*y)]

    m = distance // W + 1
    n = distance // H + 1
    candidates = dict()
    for i in tqdm(range(-m, m)):
        for j in range(-n, n):
            for v in evaluate(i*W, j*H, positive_positions, distance):
                u = simplify(*v)
                _, w = candidate = candidates.setdefault(u, [True, v])
                candidates[u] = (True, v) if abs(v[0]) < abs(w[0]) or abs(v[1]) < abs(w[1]) else candidate
            for v in evaluate(i*W, j*H, negative_positions, distance):
                u = simplify(*v)
                _, w = candidate = candidates.setdefault(u, [False, v])
                candidates[u] = (False, v) if abs(v[0]) < abs(w[0]) or abs(v[1]) < abs(w[1]) else candidate
    return sum(map(lambda bw: bw[0], candidates.values()))


s = solution([3,2], [1,1], [2,1], 4)
assert s == 7, s
s = solution([300,275], [150,150], [185,100], 500)
assert s == 9, s
