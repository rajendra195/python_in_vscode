class Opr:
    def __init__(self):
        pass

    def add(self, *args):
        return sum(list(args))
    
    def diff(self, n, m):
        return n - m
    
o = Opr()
q = o.diff(n=4, m=3)
print(q)
r = o.add(3, 32,33, 2, 47, 29, 10)
print(r)