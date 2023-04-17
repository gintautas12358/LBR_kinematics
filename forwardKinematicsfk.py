from transformations import H
from sympy import symbols
from simbolics import outputExpr, simp, simpLong

from H01S import H01S
from H02S import H02S
from H03S import H03S
from H04S import H04S
from H05S import H05S
from H06S import H06S
from H07S import H07S

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
tt31, d31, aa31, a31 = symbols("tt31 d31 aa31 a31")
tt51, d51, aa51, a51 = symbols("tt51 d51 aa51 a51")
tt71, d71, aa71, a71 = symbols("tt71 d71 aa71 a71")

fk1 = H01S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt1, 0, 0, 0)
fk2 = H02S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt2, 0, 0, 0)
fk3 = H03S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt31, d31, aa31, a31) * H(tt3, 0, 0, 0)
fk4 = H04S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt4, 0, 0, 0)
fk5 = H05S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt51, d51, aa51, a51) * H(tt5, 0, 0, 0)
fk6 = H06S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt6, 0, 0, 0)
fk7 = H07S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt71, d71, aa71, a71) * H(tt7, 0, 0, 0)


print("simplify fk1")
fk1 = simpLong(fk1)
outputExpr("fk1", fk1)

print("simplify fk2")
fk2 = simpLong(fk2)
outputExpr("fk2", fk2)

print("simplify fk3")
fk3 = simpLong(fk3)
outputExpr("fk3", fk3)

print("simplify fk4")
fk4 = simpLong(fk4)
outputExpr("fk4", fk4)

print("simplify fk5")
fk5 = simpLong(fk5)
outputExpr("fk5", fk5)

print("simplify fk6")
fk6 = simpLong(fk6)
outputExpr("fk6", fk6)

print("simplify fk7")
fk7 = simpLong(fk7)
outputExpr("fk7", fk7)


