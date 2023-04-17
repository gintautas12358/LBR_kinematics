from transformations import H
from sympy import symbols, pi
from simbolics import genExp
from links import l1cm, l2cm, l3cm, l4cm, l5cm, l6cm, l7cm 
from links import h1cm, h2cm, h3cm, h4cm, h5cm, h6cm, h7cm, m5cm


from fk.fk1S import fk1S
from fk.fk2S import fk2S
from fk.fk3S import fk3S
from fk.fk4S import fk4S
from fk.fk5S import fk5S
from fk.fk6S import fk6S
from fk.fk7S import fk7S

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
tt1cm, tt2cm, tt3cm, tt4cm, tt5cm, tt6cm, tt7cm = symbols("tt1cm tt2cm tt3cm tt4cm tt5cm tt6cm tt7cm")

d1cm = l1cm
d2cm = l2cm
d3cm = l3cm
d4cm = l4cm
d5cm = l5cm
d6cm = l6cm
d7cm = l7cm

a5cm1 = m5cm

a1cm = h1cm
a2cm = h2cm
a3cm = h3cm
a4cm = h4cm
a5cm = h5cm
a6cm = h6cm
a7cm = h7cm

aa1cm = 0
aa2cm = 0
aa3cm = 0
aa4cm = 0
aa5cm = 0
aa6cm = 0
aa7cm = 0


def subValues(expr):
    expr = expr.subs(tt1cm, pi/2)
    expr = expr.subs(tt2cm, pi/2)
    expr = expr.subs(tt3cm, pi/2)
    expr = expr.subs(tt4cm, pi/2)
    expr = expr.subs(tt5cm, pi/2)
    expr = expr.subs(tt6cm, pi/2)
    expr = expr.subs(tt7cm, pi/2)
    return expr

fk1cm = fk1S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt1cm, d1cm, aa1cm, a1cm)
fk2cm = fk2S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt2cm, d2cm, aa2cm, a2cm)
fk3cm = fk3S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt3cm, d3cm, aa3cm, a3cm)
fk4cm = fk4S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt4cm, d4cm, aa4cm, a4cm) 
fk5cm = fk5S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(0, 0, 0, a5cm1) * H(tt5cm, d5cm, aa5cm, a5cm)
fk6cm = fk6S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt6cm, d6cm, aa6cm, a6cm)
fk7cm = fk7S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt7cm, d7cm, aa7cm, a7cm)

for fkcm, expr_name in zip([fk1cm, fk2cm, fk3cm, fk4cm, fk5cm, fk6cm, fk7cm], ["fk"+str(i+1)+"cm" for i in range(7)]):
    fkcm = subValues(fkcm)
    genExp(expr_name, fkcm)

