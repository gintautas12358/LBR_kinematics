from sympy import symbols, Matrix
from simbolics import genExp

from PS import PS

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")

P = PS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

G = Matrix([[P.diff(tt1)],
            [P.diff(tt2)],
            [P.diff(tt3)],
            [P.diff(tt4)],
            [P.diff(tt5)],
            [P.diff(tt6)],
            [P.diff(tt7)]])

genExp("G", G)
