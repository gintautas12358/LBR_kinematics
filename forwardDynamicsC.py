from sympy import symbols
from simbolics import outputCLong,  simpLong, zeros

from Mtt.Mtt1S import Mtt1S
from Mtt.Mtt2S import Mtt2S
from Mtt.Mtt3S import Mtt3S
from Mtt.Mtt4S import Mtt4S
from Mtt.Mtt5S import Mtt5S
from Mtt.Mtt6S import Mtt6S
from Mtt.Mtt7S import Mtt7S

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")


Mtt = []
for MttS, expr_name in zip([Mtt1S, Mtt2S, Mtt3S, Mtt4S, Mtt5S, Mtt6S, Mtt7S], ["Mtt"+str(i+1) for i in range(7)]):
    print("Loading", expr_name)
    Mtt.append(MttS(tt1, tt2, tt3, tt4, tt5, tt6, tt7))

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

