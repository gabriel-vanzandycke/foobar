import fractions
# +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
# |           |           |           |           |           |
# +   Z   o   +   o   Z   +   Z   o   +       X   +   X       +
# |           |           |           |           |           |
# +---+---+---+===+===+===+===+===+===+---+---+---+---+---+---+
# |           |           |           |           |           |
# +   Z   o   +   O   Z   +   Z   o   +       X   +   X       +
# |           |           |           |           |           |
# +---+---+---+===+===+===+===+===+===+---+---+---+---+---+---+
# |           |           |           |           |           |
# +   Z   o   +   o   Z   +   Z   o   +       X   +   X       +
# |           |           |           |           |           |
# +---+---+---+===+===+===+===+===+===+---+---+---+---+---+---+
# |           |           |           |           |           |
# +   X   o   +   o   X   +   X   o   +       X   +   X       +
# |           |           |           |           |           |
# +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

def evaluate(offsetx, offsety, positions, distance, candidates):
    for x, y in positions:
        u, v = x + offsetx, y + offsety
        if u**2 + v**2 <= distance**2:
            gcd = 1 if u == v == 0 else fractions.gcd(abs(u), abs(v))
            candidates.add((u//gcd, v//gcd))

def solution(dimensions, your_position, trainer_position, distance):
    """
        dimensions: an array of two integers of the width and height of the room
        your_position:    x and y coordinates of your position
        trainer_position: x and y coordinates of the trainer
        distance: maximum distance that the gun can fire

        return: an integer of the number of distinct directions that you can fire to hit the elite trainer
    """
    w, h = dimensions
    W, H = w*2, h*2
    x, y = your_position
    trainer_positions = set([
        (   trainer_position[0] -x ,    trainer_position[1] -y ),
        ((W-trainer_position[0])-x ,    trainer_position[1] -y ),
        (   trainer_position[0] -x , (H-trainer_position[1])-y ),
        ((W-trainer_position[0])-x , (H-trainer_position[1])-y ),
    ])
    clone_positions = set([(0, 0), (W-2*x, 0), (0, H-2*y), (W-2*x, H-2*y)])

    m = distance // W + 1
    n = distance // H + 1
    candidates = set()
    clones = set()

    for i in range(-m, m+1):
        for j in range(-n, n+1):
            if fractions.gcd(abs(i), abs(j)) == 1 or i == j == 0:
                evaluate(i*W, j*H, trainer_positions, distance, candidates)
                evaluate(i*W, j*H, clone_positions, distance//2, clones)
    return len(candidates-clones)

s = solution([3,2], [1,1], [2,1], 4)
assert s == 7, s
s = solution([300,275], [150,150], [185,100], 500)
assert s == 9, s
