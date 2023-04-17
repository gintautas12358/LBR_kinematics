from sympy import symbols, Matrix, zeros
from simbolics import outputExpr, simp, simpLong

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

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")

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

fk1 = fk1S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk2 = fk2S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk3 = fk3S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk4 = fk4S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk5 = fk5S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk6 = fk6S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk7 = fk7S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

t1  = fk1 [:3,3]
t2  = fk2 [:3,3]
t3  = fk3 [:3,3]
t4  = fk4 [:3,3]
t5  = fk5 [:3,3]
t6  = fk6 [:3,3]
t7  = fk7 [:3,3]

z0 = Matrix([[0], [0], [1]])
z1 = fk1[:3,2]
z2 = fk2[:3,2]
z3 = fk3[:3,2]
z4 = fk4[:3,2]
z5 = fk5[:3,2]
z6 = fk6[:3,2]
z7 = fk7[:3,2]


J1cm = Matrix([z0.cross(t1cm), z0]).row_join(zeros(6,6))

J2cm = Matrix([z0.cross(t2cm), z0])\
        .row_join(Matrix([z1.cross(t2cm - t1), z1])).row_join(zeros(6,5))

J3cm = Matrix([z0.cross(t3cm), z0])\
    .row_join(Matrix([z1.cross(t3cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t3cm - t2), z2])).row_join(zeros(6,4))

J4cm = Matrix([z0.cross(t4cm), z0])\
    .row_join(Matrix([z1.cross(t4cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t4cm - t2), z2]))\
    .row_join(Matrix([z3.cross(t4cm - t3), z3])).row_join(zeros(6,3))

J5cm = Matrix([z0.cross(t5cm), z0])\
    .row_join(Matrix([z1.cross(t5cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t5cm - t2), z2]))\
    .row_join(Matrix([z3.cross(t5cm - t3), z3]))\
    .row_join(Matrix([z4.cross(t5cm - t4), z4])).row_join(zeros(6,2))


J6cm = Matrix([z0.cross(t6cm), z0])\
    .row_join(Matrix([z1.cross(t6cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t6cm - t2), z2]))\
    .row_join(Matrix([z3.cross(t6cm - t3), z3]))\
    .row_join(Matrix([z4.cross(t6cm - t4), z4]))\
    .row_join(Matrix([z5.cross(t6cm - t5), z5])).row_join(zeros(6,1))


J7cm = Matrix([z0.cross(t7cm), z0])\
    .row_join(Matrix([z1.cross(t7cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t7cm - t2), z2]))\
    .row_join(Matrix([z3.cross(t7cm - t3), z3]))\
    .row_join(Matrix([z4.cross(t7cm - t4), z4]))\
    .row_join(Matrix([z5.cross(t7cm - t5), z5]))\
    .row_join(Matrix([z6.cross(t7cm - t6), z6]))


print("simplify J1cm")
J1cm = simpLong(J1cm)
outputExpr("J1cm", J1cm)

print("simplify J2cm")
J2cm = simpLong(J2cm)
outputExpr("J2cm", J2cm)

print("simplify J3cm")
J3cm = simpLong(J3cm)
outputExpr("J3cm", J3cm)

print("simplify J4cm")
J4cm = simpLong(J4cm)
outputExpr("J4cm", J4cm)

print("simplify J5cm")
J5cm = simpLong(J5cm)
outputExpr("J5cm", J5cm)

print("simplify J6cm")
J6cm = simpLong(J6cm)
outputExpr("J6cm", J6cm)

print("simplify J7cm")
J7cm = simpLong(J7cm)
outputExpr("J7cm", J7cm)