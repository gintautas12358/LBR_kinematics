from transformations import H
from sympy import symbols
from simbolics import genExp

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
d0, d1, d2, d3, d4, d5, d6, d7 = symbols("d0 d1 d2 d3 d4 d5 d6 d7")
aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7 = symbols("aa0 aa1 aa2 aa3 aa4 aa5 aa6 aa7")
a0, a1, a2, a3, a4, a5, a6, a7 = symbols("a0 a1 a2 a3 a4 a5 a6 a7")

# # - | d | alpha | a
DH = [[tt0, d0, aa0, a0],
      [tt1, d1, aa1, a1],
      [tt2, d2, aa2, a2],
      [tt3, d3, aa3, a3],
      [tt4, d4, aa4, a4],
      [tt5, d5, aa5, a5],
      [tt6, d6, aa6, a6],
      [tt7, d7, aa7, a7]]

H01 = H(*DH[0])
H02 = H01 * H(*DH[1])
H03 = H02 * H(*DH[2])
H04 = H03 * H(*DH[3]) 
H05 = H04 * H(*DH[4])
H06 = H05 * H(*DH[5])
H07 = H06 * H(*DH[6])



genExp("H01", H01)
genExp("H02", H02)
genExp("H03", H03)
genExp("H04", H04)
genExp("H05", H05)
genExp("H06", H06)
genExp("H07", H07)


# print("simplify H01")
# H01 = simpLong(H01)
# outputExpr("H01", H01)

# print("simplify H01")
# H01 = simpLong(H01)
# outputExpr("H01", H01)

# print("simplify H02")
# H02 = simpLong(H02)
# outputExpr("H02", H02)

# print("simplify H03")
# outputExpr("H03", H03)
# H03 = simpLong(H03)

# print("simplify H04")
# H04 = simpLong(H04)
# outputExpr("H04", H04)

# print("simplify H05")
# H05 = simpLong(H05)
# outputExpr("H05", H05)

# print("simplify H06")
# H06 = simpLong(H06)
# outputExpr("H06", H06)

# print("simplify H07")
# H07 = simpLong(H07)
# outputExpr("H07", H07)

