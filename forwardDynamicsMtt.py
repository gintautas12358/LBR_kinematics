from sympy import symbols
from simbolics import outputExprLong, simpLong, diffLong

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")

from MS import MS

M = MS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

print("M diff tt1")
Mtt1 = diffLong(M,tt1)
print("M diff tt2")
Mtt2 = diffLong(M,tt2)
print("M diff tt3")
Mtt3 = diffLong(M,tt3)
print("M diff tt4")
Mtt4 = diffLong(M,tt4)
print("M diff tt5")
Mtt5 = diffLong(M,tt5)
print("M diff tt6")
Mtt6 = diffLong(M,tt6)
print("M diff tt7")
Mtt7 = diffLong(M,tt7)

print("simplify Mtt1")
Mtt1 =  simpLong(Mtt1)
outputExprLong("Mtt1", Mtt1)

print("simplify Mtt2")
Mtt2 =  simpLong(Mtt2)
outputExprLong("Mtt2", Mtt2)

print("simplify Mtt3")
Mtt3 =  simpLong(Mtt3)
outputExprLong("Mtt3", Mtt3)

print("simplify Mtt4")
Mtt4 =  simpLong(Mtt4)
outputExprLong("Mtt4", Mtt4)

print("simplify Mtt5")
Mtt5 =  simpLong(Mtt5)
outputExprLong("Mtt5", Mtt5)

print("simplify Mtt6")
Mtt6 =  simpLong(Mtt6)
outputExprLong("Mtt6", Mtt6)

print("simplify Mtt7")
Mtt7 =  simpLong(Mtt7)
outputExprLong("Mtt7", Mtt7)

