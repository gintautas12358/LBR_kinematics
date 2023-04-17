from sympy import symbols, diag
from simbolics import simpLong, outputExprLong

from fkcm.fk1cmS import fk1cmS
from fkcm.fk2cmS import fk2cmS
from fkcm.fk3cmS import fk3cmS
from fkcm.fk4cmS import fk4cmS
from fkcm.fk5cmS import fk5cmS
from fkcm.fk6cmS import fk6cmS
from fkcm.fk7cmS import fk7cmS

from Jcm.J1cmS import J1cmS
from Jcm.J2cmS import J2cmS
from Jcm.J3cmS import J3cmS
from Jcm.J4cmS import J4cmS
from Jcm.J5cmS import J5cmS
from Jcm.J6cmS import J6cmS
from Jcm.J7cmS import J7cmS

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")

def split(J):
    return J[:3, :], J[:3, :]

J1cm = J1cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
J2cm = J2cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
J3cm = J3cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
J4cm = J4cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
J5cm = J5cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
J6cm = J6cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
J7cm = J7cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

(J1cmv, J1cmw), (J2cmv, J2cmw), (J3cmv, J3cmw), (J4cmv, J4cmw), (J5cmv, J5cmw), (J6cmv, J6cmw), (J7cmv, J7cmw) = split(J1cm), split(J2cm), split(J3cm), split(J4cm), split(J5cm), split(J6cm), split(J7cm)

fk1cm = fk1cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk2cm = fk2cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk3cm = fk3cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk4cm = fk4cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk5cm = fk5cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk6cm = fk6cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk7cm = fk7cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

R1cm = fk1cm[:3,:3]
R2cm = fk2cm[:3,:3]
R3cm = fk3cm[:3,:3]
R4cm = fk4cm[:3,:3]
R5cm = fk5cm[:3,:3]
R6cm = fk6cm[:3,:3]
R7cm = fk7cm[:3,:3]

I1cm = diag(0.033, 0.0333, 0.0123)
I2cm = diag(0.0305, 0.0304, 0.011)
I3cm = diag(0.025, 0.0238, 0.0076)
I4cm = diag(0.017, 0.0164, 0.006)
I5cm = diag(0.01, 0.0087, 0.00449)
I6cm = diag(0.0049, 0.0047, 0.0036)
I7cm = diag(0.001, 0.001, 0.001)

def simpMul(core_expr, le, re):
    expr = core_expr

    for i in range(len(le)):
        print("left wing")
        print("member", i)
        expr = le[len(le)-1 - i] * expr
        expr = simpLong(expr)

    for i in range(len(re)):
        print("right wing")
        print("member", i)
        expr = expr * re[i] 
        expr = simpLong(expr)
    
    return expr

for Jcmw, Rcm, expr_name in zip([J1cmw, J2cmw, J3cmw, J4cmw, J5cmw, J6cmw, J7cmw], [R1cm, R2cm, R3cm, R4cm, R5cm, R6cm, R7cm], ["M2"+str(i+1) for i in range(7)]):
    print("simplify", expr_name)
    fk = simpMul(I1cm, [Jcmw.transpose(), Rcm], [Rcm.transpose(), Jcmw ])
    outputExprLong(expr_name, fk)


