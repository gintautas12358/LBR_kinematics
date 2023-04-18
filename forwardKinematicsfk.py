from transformations import H
from sympy import symbols
from simbolics import genExp
from links import l1, l2, l3, l4, l5, l6, l7 


from H.H01S import H01S
from H.H02S import H02S
from H.H03S import H03S
from H.H04S import H04S
from H.H05S import H05S
from H.H06S import H06S
from H.H07S import H07S

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")

tt31 = 0
tt51 = 0
tt71 = 0

d31 = l3
d51 = l5
d71 = l7

aa31 = 0
aa51 = 0
aa71 = 0

a31 = 0
a51 = 0
a71 = 0


fk1 = H01S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt1, 0, 0, 0)
fk2 = H02S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt2, 0, 0, 0)
fk3 = H03S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt31, d31, aa31, a31) * H(tt3, 0, 0, 0)
fk4 = H04S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt4, 0, 0, 0)
fk5 = H05S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt51, d51, aa51, a51) * H(tt5, 0, 0, 0)
fk6 = H06S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt6, 0, 0, 0)
fk7 = H07S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt71, d71, aa71, a71) * H(tt7, 0, 0, 0)

for fk, expr_name in zip([fk1, fk2, fk3, fk4, fk5, fk6, fk7], ["fk"+str(i+1) for i in range(7)]):
	genExp(expr_name, fk)

