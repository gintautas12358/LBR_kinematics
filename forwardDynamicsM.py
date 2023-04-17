from sympy import symbols
from simbolics import outputExprLong, simpLong

from Mparts.M11S import M11S
from Mparts.M12S import M12S
from Mparts.M13S import M13S
from Mparts.M14S import M14S
from Mparts.M15S import M15S
from Mparts.M16S import M16S
from Mparts.M17S import M17S

from Mparts.M21S import M21S
from Mparts.M22S import M22S
from Mparts.M23S import M23S
from Mparts.M24S import M24S
from Mparts.M25S import M25S
from Mparts.M26S import M26S
from Mparts.M27S import M27S


tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")

M11 = M11S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M12 = M12S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M13 = M13S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M14 = M14S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M15 = M15S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M16 = M16S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M17 = M17S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)

M21 = M21S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M22 = M22S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M23 = M23S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M24 = M24S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M25 = M25S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M26 = M26S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M27 = M27S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)


M1 = M11 +\
    M12 +\
    M13 +\
    M14 +\
    M15 +\
    M16 +\
    M17

M2 = M21 +\
    M22 +\
    M23 +\
    M24 +\
    M25 +\
    M26 +\
    M27

# print("simplify M1")
# M1 = simpLong(M1)
# outputExprLong("M1", M1)

# print("simplify M2")
# M2 = simpLong(M2)
# outputExprLong("M2", M2)

M = M1 + M2

print("simplify M")
M = simpLong(M)
outputExprLong("M", M)

