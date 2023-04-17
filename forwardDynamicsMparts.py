from sympy import symbols, diag
from simbolics import outputExprLong, simp, simpLong

from fk1cmS import fk1cmS
from fk2cmS import fk2cmS
from fk3cmS import fk3cmS
from fk4cmS import fk4cmS
from fk5cmS import fk5cmS
from fk6cmS import fk6cmS
from fk7cmS import fk7cmS

from fk1S import fk1S
from fk2S import fk2S
from fk3S import fk3S
from fk4S import fk4S
from fk5S import fk5S
from fk6S import fk6S
from fk7S import fk7S

from J1cmS import J1cmS
from J2cmS import J2cmS
from J3cmS import J3cmS
from J4cmS import J4cmS
from J5cmS import J5cmS
from J6cmS import J6cmS
from J7cmS import J7cmS

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
m1, m2, m3, m4, m5, m6, m7 = symbols("m1, m2, m3, m4, m5, m6, m7")

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

# M11 = m1 * J1cmv.transpose() * J1cmv
# M12 = m2 * J2cmv.transpose() * J2cmv
# M13 = m3 * J3cmv.transpose() * J3cmv
# M14 = m4 * J4cmv.transpose() * J4cmv
# M15 = m5 * J5cmv.transpose() * J5cmv
# M16 = m6 * J6cmv.transpose() * J6cmv
# M17 = m7 * J7cmv.transpose() * J7cmv

def subValues(expr):
    expr = expr.subs(m1, 5.76)
    expr = expr.subs(m2, 6.35)
    expr = expr.subs(m3, 3.5)
    expr = expr.subs(m4, 3.5)
    expr = expr.subs(m5, 3.5)
    expr = expr.subs(m6, 1.8)
    expr = expr.subs(m7, 1.2)
    return expr

# M11 = subValues(M11)
# M12 = subValues(M12)
# M13 = subValues(M13)
# M14 = subValues(M14)
# M15 = subValues(M15)
# M16 = subValues(M16)
# M17 = subValues(M17)

# print("simplify M11")
# M11 = simpLong(M11)
# outputExprLong("M11", M11)

# print("simplify M12")
# M12 = simpLong(M12)
# outputExprLong("M12", M12)

# print("simplify M13")
# M13 = simpLong(M13)
# outputExprLong("M13", M13)

# print("simplify M14")
# M14 = simpLong(M14)
# outputExprLong("M14", M14)

# print("simplify M15")
# M15 = simpLong(M15)
# outputExprLong("M15", M15)

# print("simplify M16")
# M16 = simpLong(M16)
# outputExprLong("M16", M16)

# print("simplify M17")
# M17 = simpLong(M17)
# outputExprLong("M17", M17)
         

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

M21 = (J1cmw.transpose() * R1cm * I1cm * R1cm.transpose()  *J1cmw) 
M22 = (J2cmw.transpose() * R2cm * I2cm * R2cm.transpose()  *J2cmw) 
M23 = (J3cmw.transpose() * R3cm * I3cm * R3cm.transpose()  *J3cmw) 
M24 = (J4cmw.transpose() * R4cm * I4cm * R4cm.transpose()  *J4cmw) 
M25 = (J5cmw.transpose() * R5cm * I5cm * R5cm.transpose()  *J5cmw) 
M26 = (J6cmw.transpose() * R6cm * I6cm * R6cm.transpose()  *J6cmw) 
M27 = (J7cmw.transpose() * R7cm * I7cm * R7cm.transpose()  *J7cmw)

# M21 = subValues(M21)
# M22 = subValues(M22)
# M23 = subValues(M23)
# M24 = subValues(M24)
# M25 = subValues(M25)
# M26 = subValues(M26)
# M27 = subValues(M27)

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

print("simplify M21")
M21 = simpMul(I1cm, [J1cmw.transpose(), R1cm], [R1cm.transpose(), J1cmw ])
outputExprLong("M21", M21)

print("simplify M22")
M22 = simpMul(I2cm, [J2cmw.transpose(), R2cm], [R1cm.transpose(), J2cmw ])
outputExprLong("M22", M22)

print("simplify M23")
M23 = simpMul(I3cm, [J3cmw.transpose(), R3cm], [R3cm.transpose(), J3cmw ])
outputExprLong("M23", M23)

print("simplify M24")
M24 = simpMul(I4cm, [J4cmw.transpose(), R4cm], [R4cm.transpose(), J4cmw ])
outputExprLong("M24", M24)

print("simplify M25")
M25 = simpMul(I5cm, [J5cmw.transpose(), R5cm], [R5cm.transpose(), J5cmw ])
outputExprLong("M25", M25)

print("simplify M26")
M26 = simpMul(I6cm, [J6cmw.transpose(), R6cm], [R6cm.transpose(), J6cmw ])
outputExprLong("M26", M26)

print("simplify M27")
M27 = simpMul(I7cm, [J7cmw.transpose(), R7cm], [R7cm.transpose(), J7cmw ])
outputExprLong("M27", M27)


