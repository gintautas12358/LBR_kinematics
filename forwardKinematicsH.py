from transformations import H
from sympy import symbols, pi, ones
from simbolics import genExp
from links import l1, l2, l3, l4, l5, l6, l7 

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7 = symbols("aa0 aa1 aa2 aa3 aa4 aa5 aa6 aa7")

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

h = ones(4,4)
for dh, expr_name in zip(DH, ["H0"+str(i+1) for i in range(7)]):
	h *= H(*dh)
	h = subValues(h)
	h = genExp(expr_name, h)
