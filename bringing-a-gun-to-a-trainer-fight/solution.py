import fractions

def evaluate(offsetx, offsety, positions, distance, candidates):
    for x, y in positions:
        u, v = x + offsetx, y + offsety
        if u**2 + v**2 <= distance**2:
            candidates.append((u, v))

def simplify(u, v):
    gcd = abs(fractions.gcd(u, v)) or 1
    return u//gcd, v//gcd

def solution(dimensions, your_position, trainer_position, distance):
    w, h = dimensions
    W, H = w*2, h*2
    x, y = your_position
    trainer_positions = [
        (  trainer_position[0]-x ,   trainer_position[1]-y ),
        (W-trainer_position[0]-x ,   trainer_position[1]-y ),
        (  trainer_position[0]-x , H-trainer_position[1]-y ),
        (W-trainer_position[0]-x , H-trainer_position[1]-y ),
    ]
    clone_positions = [(0, 0), (W-2*x, 0), (0, H-2*y), (W-2*x, H-2*y)]

    m = distance // W + 1
    n = distance // H + 1
    positives = list()
    negatives = list()
    for i in range(-m, m):
        for j in range(-n, n):
            evaluate(i*W, j*H, trainer_positions, distance, positives)
            evaluate(i*W, j*H, clone_positions, distance, negatives)

    candidates = set()
    for trainer in positives:
        for clone in negatives:
            if simplify(*clone) == simplify(*trainer):
                if abs(trainer[0]) > abs(clone[0]) or abs(trainer[1]) > abs(clone[1]):
                    break
        else:
            candidates.add(simplify(*trainer))
    return len(candidates)


s = solution([3,2], [1,1], [2,1], 4)
assert s == 7, s
s = solution([300,275], [150,150], [185,100], 500)
assert s == 9, s


