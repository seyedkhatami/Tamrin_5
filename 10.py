class A:
    pass

class B:
    pass

class C:
    pass

class D:
    pass

class E:
    pass

class K1(A, B, C):
    pass

class K2(D, B, E):
    pass

class K3(D, A):
    pass

class Z(K1, K2, K3):
    pass


#mro :

"""
L(Z) = Z + merg(L(K1), L(K2), L(K3), K1, K2, K3)
     = Z + merg(K1ABCO, K2DBEO, K3DAO, K1, K2, K3)
     = Z + K1 + merg(ABCO, K2DBEO, K3DAO, K2, K3)
     = Z + K1 + A + merg(BCO, K2DBEO, K3DAO, K2, K3)
     = Z + K1 + A + B + merg(CO, K2DBEO, K3DAO, K2, K3)
     = Z + K1 + A + B + C + merg(O, K2DBEO, K3DAO, K2, K3)
     = Z + K1 + A + B + C + K2 + merg(O, DBEO, K3DAO, K3)
     = Z + K1 + A + B + C + K2 + D + merg(O, BEO, K3DAO, K3)
     = Z + K1 + A + B + C + K2 + D + B + merg(O, EO, K3DAO, K3)
     = Z + K1 + A + B + C + K2 + D + B + E + merg(O, O, K3DAO, K3)
     = Z + K1 + A + B + C + K2 + D + B + E + K3 + merg(O, O, DAO)
     = Z + K1 + A + B + C + K2 + D + B + E + K3 + D + merg(O, O, AO)
     = Z + K1 + A + B + C + K2 + D + B + E + K3 + D + A + O
     = ZK1ABCK2DBEK3DAO
     
L(K1) = K1 + merg(L(A), L(B), L(C), A, B, C))
      = K1 + merg(AO, BO, CO, A, B, C)
      = K1 + A + merg(O, BO, CO, B, C)
      = K1 + A + B + merg(O, O, CO, C)
      = K1 + A + B + C + O
      = K1ABCO

L(K2) = K2 + merg(L(D), L(B), L(E), D, B, E)
      = K2 + merg(DO, BO, EO, D, B, E)
      = K2 + D + merg(O, BO, EO, B, E)
      = K2 + D + B + merg(O, O, EO, E)
      = K2 + D + B + E + merg(O, O, O)
      = K2 + D + B + E + O
      = K2DBEO

L(K3) = K3 + merg(L(D), L(A), D, A)
      = K3 + merg(DO, AO, D, A)
      = K3 + D + merg(O, AO, A)
      = K3 + D + A + O
      = K3DAO
"""

