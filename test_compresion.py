from sympy import symbols, shape, simplify

from MS import MS
# from CS import CS
from J7cmS import J7cmS

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7 = symbols("dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7")

M  = J7cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

# print("element lengths")
# s = shape(M)
# for i in range(s[0]):
#     for j in range(s[1]):
#         size = len(str(M[i,j]))
#         print(i, j, size)

expr = M[2,6]
print("size:", len(str(expr)))

print("size:", len(str(simplify(expr))))
