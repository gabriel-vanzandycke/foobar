
def solution(n):
    stringify = lambda n: "{0:b}".format(n)
    def f(s):
        if s in ['1', '']:
            return 0
        if s == '11':
            return 2
        if s[-1] == '0':
            index = s.rfind('1')
            return f(s[:index+1]) + len(s) - (index+1)
        if set(s) == {'1'}:
            return len(s) + 1
        if s[-2] == '1':
            index = s.rfind('0')
            #print(f"f({s}) = f({s[0:index]+'1'}) + {len(s) - (index+1) + 1} operations")
            return f(s[0:index]+'1') + len(s) - (index+1) + 1
        if s[-2] == '0':
            return f(s[:-1]) + 2

    return f(stringify(int(n)))

assert solution(7) == 4,  print(solution(7), "\t7 8 4 2 1 = 4")
assert solution(15) == 5, print(solution(15), "\t15 16 8 4 2 1 = 5")
assert solution(11) == 5, print(solution(11), "\t11 12 6 3 2 1 = 5")   # 1 0 1 1     index=1   "1" + (4 - (1+1)) + 1
assert solution(1) == 0,  print(solution(1), "\t1 = 0")                # 1 1 0 0
