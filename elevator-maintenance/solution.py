def solution(l):
    return sorted(l, key=lambda val: [int(section) for section in val.split(".")])

assert(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"])
assert(solution(["1.1.2", "1", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == ["1", "1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"])
