def solution(src, dest):
    if src == dest:
        return 0
    
    def reachable(x):
        # 00 01 02 03 04 05 06 07
        # 10 11 12 13 14 15 16 17
        # 20 21 22 23 24 25 26 27
        # 30 31 32 33 34 35 36 37
        # 40 41 42 43 44 45 46 47
        # 50 51 52 53 54 55 56 57
        # 60 61 62 63 64 65 66 67
        # 70 71 72 73 74 75 76 77
        octal = str(x//8)+str(x%8) # `oct` is annoying when x < 8
        vmoves = [-2, -1, 1, 2]
        hmoves = [-2, -1, 1, 2]
        for i, moves in {0: vmoves, 1: hmoves}.items():
            octal[i] > '1' or moves.remove(-2)
            octal[i] > '0' or moves.remove(-1)
            octal[i] < '6' or moves.remove( 2)
            octal[i] < '7' or moves.remove( 1)
        for vmove in vmoves:
            for hmove in hmoves:
                if abs(vmove) == abs(hmove):
                    continue
                yield x + vmove*8+hmove
    
    candidates = [src]
    distances = {src: 0}
    for i in range(64):
        for x in reachable(candidates[i]):
            distances[x] = distances[candidates[i]]+1
            if x == dest:
                return distances[x]
            if x not in candidates:
                candidates.append(x)
           

