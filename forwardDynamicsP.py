from sympy import symbols, Matrix
from simbolics import outputExpr, simp, simpLong

from fkcm.fk1cmS import fk1cmS
from fkcm.fk2cmS import fk2cmS
from fkcm.fk3cmS import fk3cmS
from fkcm.fk4cmS import fk4cmS
from fkcm.fk5cmS import fk5cmS
from fkcm.fk6cmS import fk6cmS
from fkcm.fk7cmS import fk7cmS

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
gz = symbols("gz")
m1, m2, m3, m4, m5, m6, m7 = symbols("m1, m2, m3, m4, m5, m6, m7")

fk1cm = fk1cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk2cm = fk2cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk3cm = fk3cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk4cm = fk4cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk5cm = fk5cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk6cm = fk6cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk7cm = fk7cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

t1cm = fk1cm[:3,3]
t2cm = fk2cm[:3,3]
t3cm = fk3cm[:3,3]
t4cm = fk4cm[:3,3]
t5cm = fk5cm[:3,3]
t6cm = fk6cm[:3,3]
t7cm = fk7cm[:3,3]

R1cm = fk1cm[:3,:3]
R2cm = fk2cm[:3,:3]
R3cm = fk3cm[:3,:3]
R4cm = fk4cm[:3,:3]
R5cm = fk5cm[:3,:3]
R6cm = fk6cm[:3,:3]
R7cm = fk7cm[:3,:3]

g = Matrix([0, 0, gz])

P = g.transpose() * (m1 * t1cm +\
                    m2 * t2cm  +\
                    m3 * t3cm  +\
                    m4 * t4cm  +\
                    m5 * t5cm  +\
                    m6 * t6cm  +\
                    m7 * t7cm)

P = P.subs(gz, 9.81)
P = P.subs(m1, 5.76)
P = P.subs(m2, 6.35)
P = P.subs(m3, 3.5)
P = P.subs(m4, 3.5)
P = P.subs(m5, 3.5)
P = P.subs(m6, 1.8)
P = P.subs(m7, 1.2)

print("simplify P")
P = simpLong(P)
outputExpr("P", P)

