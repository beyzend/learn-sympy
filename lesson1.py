from sympy.vector import CoordSys3D
from sympy.vector import functions
from sympy import *
from sympy.abc import *

N = CoordSys3D('N')
px, py, pz, qx, qy, qz = symbols('px,py,pz,qx,qy,qz')
P = px*N.i + py*N.j + pz*N.k
Q = qx*N.i + qy*N.j + qz*N.k

crossPQ = P.cross(Q)
normSqr = crossPQ.dot(CrossPQ)
expandNormSqr = expand(normSqr)
collectNormSqr = collect(expandNormSqr, (qx**2, qy**2, qz**2))
addExpr = px**2*qx**2 + py**2*qy**2 + pz**2*qz**2
UnevalAddExpr = UnevaluatedExpr(-addExpr)
normSqrExpr = expandNormSqr + addExpr + UnevalAddExpr
collectExpr = collect(normSqrExpr, (qx**2, qy**2, qz**2))




