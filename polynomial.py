class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            left = "( " + repr(self.p1) + " )"
        else:
            left = repr(self.p1)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            right = "( " + repr(self.p2) + " )"
        else:
            right = repr(self.p2)
        return left + " - " + right
    
class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            left = "( " + repr(self.p1) + " )"
        else:
            left = repr(self.p1)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            right = "( " + repr(self.p2) + " )"
        else:
            right = repr(self.p2)
        return left + " * " + right
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub) or isinstance(self.p1, Mul):
            left = "( " + repr(self.p1) + " )"
        else:
            left = repr(self.p1)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Mul) or isinstance(self.p2, Div):
            right = "( " + repr(self.p2) + " )"
        else:
            right = repr(self.p2)
        return left + " / " + right


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

expressions = [
    Sub(Add(Int(4), Int(3)), Int(2)),
    Add(Int(4), Mul(Int(3), Int(2))),
    Div(Sub(Int(4), Int(3)), Int(2)),
    Mul(Add(Int(4), Int(3)), Sub(Int(2), Div(Int(1), X()))),
    Mul(Int(4), Div(Int(3), Mul(Int(2), X()))),
    Div(Add(X(), Mul(Int(1), Sub(Int(4), Int(2)))), Sub(Mul(Int(3), X()), Add(Int(1), Int(2))))
]

for ex in expressions:
    print(repr(ex))