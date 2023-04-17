from transformations import H
from sympy import symbols
from simbolics import outputExpr, simp, simpLong

from fk1S import fk1S
from fk2S import fk2S
from fk3S import fk3S
from fk4S import fk4S
from fk5S import fk5S
from fk6S import fk6S
from fk7S import fk7S

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
tt1cm, tt2cm, tt3cm, tt4cm, tt5cm, tt6cm, tt7cm = symbols("tt1cm tt2cm tt3cm tt4cm tt5cm tt6cm tt7cm")
d1cm, d2cm, d3cm, d4cm, d5cm, d6cm, d7cm = symbols("d1cm d2cm d3cm d4cm d5cm d6cm d7cm")
aa1cm, aa2cm, aa3cm, aa4cm, aa5cm, aa6cm, aa7cm = symbols("aa1cm aa2cm aa3cm aa4cm aa5cm aa6cm aa7cm")
a1cm, a2cm, a3cm, a4cm, a5cm, a6cm, a7cm = symbols("a1cm a2cm a3cm a4cm a5cm a6cm a7cm")
a5cm1 = symbols("a5cm1")

fk1cm = fk1S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt1cm, d1cm, aa1cm, a1cm)
fk2cm = fk2S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt2cm, d2cm, aa2cm, a2cm)
fk3cm = fk3S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt3cm, d3cm, aa3cm, a3cm)
fk4cm = fk4S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt4cm, d4cm, aa4cm, a4cm) 
fk5cm = fk5S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(0, 0, 0, a5cm1) * H(tt5cm, d5cm, aa5cm, a5cm)
fk6cm = fk6S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt6cm, d6cm, aa6cm, a6cm)
fk7cm = fk7S(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt7cm, d7cm, aa7cm, a7cm)

print("simplify fk1cm")
fk1cm = simpLong(fk1cm)
outputExpr("fk1cm", fk1cm)

print("simplify fk2cm")
fk2cm = simpLong(fk2cm)
outputExpr("fk2cm", fk2cm)

print("simplify fk3cm")
fk3cm = simpLong(fk3cm)
outputExpr("fk3cm", fk3cm)

print("simplify fk4cm")
fk4cm = simpLong(fk4cm)
outputExpr("fk4cm", fk4cm)

print("simplify fk5cm")
fk5cm = simpLong(fk5cm)
outputExpr("fk5cm", fk5cm)

print("simplify fk6cm")
fk6cm = simpLong(fk6cm)
outputExpr("fk6cm", fk6cm)

print("simplify fk7cm")
fk7cm = simpLong(fk7cm)
outputExpr("fk7cm", fk7cm)




