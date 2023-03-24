def solution(xs):
    xs_positives = [x for x in xs if x > 0]
    xs_negatives = list(sorted([-x for x in xs if x < 0]))
    xs_negatives_length = len(xs_negatives)
    if not xs_positives:
        if xs_negatives_length == 0:
            return str(0)
        if xs_negatives_length == 1:
            return str(max(xs))

    if xs_negatives_length % 2:
        xs_negatives = xs_negatives[1:]
    
    result = 1
    for x in xs_positives:
        result *= x
    for x in xs_negatives:
        result *= x
    return str(result)
