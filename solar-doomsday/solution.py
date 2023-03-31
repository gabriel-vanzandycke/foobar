def solution(area):
    output = []
    while area:
        side = int(area ** 0.5)
        square = side ** 2
        area -= square
        output.append(square)
    return output
