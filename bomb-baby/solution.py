def solution(M, F):
    def f(M, F): # m < f
        if M == 1: return F-1
        if M < 0: raise
        d = F // M
        m = F % M
        return f(min(M,m), max(M,m)) + d
    F = int(F)
    M = int(M)
    try:
        return str(f(min(F,M), max(F,M)))
    except:
        return 'impossible'
    
