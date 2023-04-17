from transformations import H
from sympy import symbols, pi, ones
from simbolics import genExp

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
# d0, d1, d2, d3, d4, d5, d6, d7 = symbols("d0 d1 d2 d3 d4 d5 d6 d7")
aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7 = symbols("aa0 aa1 aa2 aa3 aa4 aa5 aa6 aa7")
# a0, a1, a2, a3, a4, a5, a6, a7 = symbols("a0 a1 a2 a3 a4 a5 a6 a7")


l1 = 0.1575
l2 = 0.2025
l3 = 0.2045
l4 = 0.2155
l5 = 0.1845
l6 = 0.2155
l7 = 0.081


d0 = l1
d1 = l2
d2 = 0
d3 = l3+l4
d4 = 0
d5 = l5+l6
d6 = 0
d7 = 0



a0 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0

tt0 = 0

def subValues(expr):
	expr = expr.subs(aa0, 0)      
	expr = expr.subs(aa1, -pi/2)
	expr = expr.subs(aa2, pi/2)
	expr = expr.subs(aa3, pi/2)
	expr = expr.subs(aa4, -pi/2)
	expr = expr.subs(aa5, -pi/2)
	expr = expr.subs(aa6, pi/2)
	expr = expr.subs(aa7, 0)
	return expr

# # - | d | alpha | a
DH = [[tt0, d0, aa0, a0],
	[tt1, d1, aa1, a1],
	[tt2, d2, aa2, a2],
	[tt3, d3, aa3, a3],
	[tt4, d4, aa4, a4],
	[tt5, d5, aa5, a5],
	[tt6, d6, aa6, a6],
	[tt7, d7, aa7, a7]]

# names = ["H0"+str(i+1) for i in range(7)]
# print(names)

h = ones(4,4)
for dh, expr_name in zip(DH, ["H0"+str(i+1) for i in range(7)]):
	h *= H(*dh)
	h = subValues(h)
	h = genExp(expr_name, h)


# H01 = H(*DH[0])
# H01 = subValues(H01)
# H01 = genExp("H01", H01)

# H02 = H01 * H(*DH[1])
# H02 = subValues(H02)
# print(H02)
# H02 = genExp("H02", H02)



# H03 = H02 * H(*DH[2])
# H03 = genExp("H03", H03)

# H04 = H03 * H(*DH[3]) 
# H04 = genExp("H04", H04)

# H05 = H04 * H(*DH[4])
# H05 = genExp("H05", H05)

# H06 = H05 * H(*DH[5])
# H06 = genExp("H06", H06)

# H07 = H06 * H(*DH[6])
# H07 = genExp("H07", H07)







