from sympy import symbols
from simbolics import outputExprLong, simpLong, diffLong

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")

from MS import MS

M = MS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

for tt, expr_name in zip([tt1, tt2, tt3, tt4, tt5, tt6, tt7], ["Mtt"+str(i+1) for i in range(7)]):
    print("M diff", tt)
    Mtt = diffLong(M,tt)
    Mtt =  simpLong(Mtt)
    outputExprLong(expr_name, Mtt)
