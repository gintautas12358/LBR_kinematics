from sympy import symbols
from simbolics import outputCLong,  simpLong, zeros

from Mtt1S import Mtt1S
from Mtt2S import Mtt2S
from Mtt3S import Mtt3S
from Mtt4S import Mtt4S
from Mtt5S import Mtt5S
from Mtt6S import Mtt6S
from Mtt7S import Mtt7S

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")

print("Loading Mtt1")
Mtt1 = Mtt1S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
print("Loading Mtt2")
Mtt2 = Mtt2S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
print("Loading Mtt3")
Mtt3 = Mtt3S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
print("Loading Mtt4")
Mtt4 = Mtt4S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
print("Loading Mtt5")
Mtt5 = Mtt5S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
print("Loading Mtt6")
Mtt6 = Mtt6S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
print("Loading Mtt7")
Mtt7 = Mtt7S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

Mtt = [Mtt1, Mtt2, Mtt3, Mtt4, Mtt5, Mtt6, Mtt7]

dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7 = symbols("dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7")
dtt = [dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7]

def chrisSym(k, j):
    c = 0
    for i in range(7):
        c += (Mtt[i][k,j] - 1/2*Mtt[k][i, j]) * dtt[i]
    return c

C = zeros(7,7)
for k in range(7):
    for j in range(7):
        print(7**2, 7*k+j)
        C[k, j] = chrisSym(k, j)

print("simplify C")
C =  simpLong(C)
outputCLong("C", C)

