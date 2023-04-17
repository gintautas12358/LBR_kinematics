from sympy import symbols, diag
from simbolics import genExp

from Jcm.J1cmS import J1cmS
from Jcm.J2cmS import J2cmS
from Jcm.J3cmS import J3cmS
from Jcm.J4cmS import J4cmS
from Jcm.J5cmS import J5cmS
from Jcm.J6cmS import J6cmS
from Jcm.J7cmS import J7cmS

from links import m1, m2, m3, m4, m5, m6, m7

tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt1 tt2 tt3 tt4 tt5 tt6 tt7")

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

M11 = m1 * J1cmv.transpose() * J1cmv
M12 = m2 * J2cmv.transpose() * J2cmv
M13 = m3 * J3cmv.transpose() * J3cmv
M14 = m4 * J4cmv.transpose() * J4cmv
M15 = m5 * J5cmv.transpose() * J5cmv
M16 = m6 * J6cmv.transpose() * J6cmv
M17 = m7 * J7cmv.transpose() * J7cmv

for fk, expr_name in zip([M11, M12, M13, M14, M15, M16, M17], ["M1"+str(i+1) for i in range(7)]):
	genExp(expr_name, fk)
