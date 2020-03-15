from sympy.vector import CoordSys3D
from sympy.vector import functions
from sympy import *
from sympy.abc import *

N = CoordSys3D('N')
px, py, pz, qx, qy, qz = symbols('px,py,pz,qx,qy,qz')
P = px*N.i + py*N.j + pz*N.k
Q = qx*N.i + qy*N.j + qz*N.k

crossPQ = P.cross(Q)
normSqr = crossPQ.dot(crossPQ)
addExpr = px**2*qx**2 + py**2*qy**2 + pz**2*qz**2
normSqrExpr = collect(collect(factor(normSqr + addExpr),
                              (qx**2, qy**2, qz**2)),
                      (px**2 + py**2 + pz**2)) + -addExpr
expr0 = normSqrExpr.func()
expr1 = normSqrExpr.func()
# Break normSqrExpr as two subexpressions.
for exprArg in normSqrExpr.args:
    if (len([True for arg in exprArg.args if (arg
                                              == (px**2 + py**2 + pz**2))])
            != 0):
        expr0 = normSqrExpr.func(expr0, exprArg)
    else:
        expr1 = normSqrExpr.func(expr1, exprArg)

normSqrExpr = normSqrExpr.func(expr0, factor(expr1))
display(normSqrExpr)
