class F:
    pass

class E:
    pass

class D:
    pass

class C(D, F):
    pass

class B(D, E):
    pass

class A(B, C):
    pass

#mro :

"""
L(A) = A + merg(L(B), L(C), B, C)
     = A + merg(BDEO, CDFO, B, C)
     = A + B + merg(DEO, CDFO, C)
     = A + B + D + merg(EO, CDFO, C)
     = A + B + D + E + merg(O, CDFO, C)
     = A + B + D + E + C + merg(O, DFO)
     = A + B + D + E + C + D + merg(O, FO)
     = A + B + D + E + C + D + F + O
     = ABDECDFO

L(B) = B + merg(L(D), L(E), D, E)
     = B + merg(DO, EO, D, E)
     = B + D merg(O, EO, E)
     = B + D + E + O
     = BDEO

L(C) = C + merg(L(D), L(F), D, F)
     = C + merg(DO, FO, D, F)
     = C + D + merg(O, FO, F)
     = C + D + F + O
     = CDFO
"""