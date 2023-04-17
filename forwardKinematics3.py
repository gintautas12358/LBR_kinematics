from transformations import H
from sympy import pprint, symbols, pi, pretty, Matrix, diag, shape, zeros, simplify
# from sympy.physics.vector import cross

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
d0, d1, d2, d3, d4, d5, d6, d7 = symbols("d0 d1 d2 d3 d4 d5 d6 d7")
aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7 = symbols("aa0 aa1 aa2 aa3 aa4 aa5 aa6 aa7")
a0, a1, a2, a3, a4, a5, a6, a7 = symbols("a0 a1 a2 a3 a4 a5 a6 a7")
tt31, d31, aa31, a31 = symbols("tt31 d31 aa31 a31")
tt51, d51, aa51, a51 = symbols("tt51 d51 aa51 a51")
tt71, d71, aa71, a71 = symbols("tt71 d71 aa71 a71")
tt1cm, tt2cm, tt3cm, tt4cm, tt5cm, tt6cm, tt7cm = symbols("tt1cm tt2cm tt3cm tt4cm tt5cm tt6cm tt7cm")
d1cm, d2cm, d3cm, d4cm, d5cm, d6cm, d7cm = symbols("d1cm d2cm d3cm d4cm d5cm d6cm d7cm")
aa1cm, aa2cm, aa3cm, aa4cm, aa5cm, aa6cm, aa7cm = symbols("aa1cm aa2cm aa3cm aa4cm aa5cm aa6cm aa7cm")
a1cm, a2cm, a3cm, a4cm, a5cm, a6cm, a7cm = symbols("a1cm a2cm a3cm a4cm a5cm a6cm a7cm")
a5cm1 = symbols("a5cm1")
gz = symbols("gz")
m1, m2, m3, m4, m5, m6, m7 = symbols("m1, m2, m3, m4, m5, m6, m7")

# def subValues(expr):

#     l1 = 0.1575
#     l2 = 0.2025
#     l3 = 0.2045
#     l4 = 0.2155
#     l5 = 0.1845
#     l6 = 0.2155
#     l7 = 0.081

#     l1cm = 0.12
#     l2cm = 0.042
#     l3cm = 0.13
#     l4cm = 0.034
#     l5cm = 0.076
#     l6cm = 0.0004
#     l7cm = 0.02

#     h1cm = -0.03
#     h2cm = -0.059
#     h3cm = 0.03
#     h4cm = 0.067
#     h5cm = -0.021
#     h6cm = 0.0006
#     h7cm = 0.0

#     m5cm = -0.0001

#     expr = expr.subs(tt0, 0)
#     expr = expr.subs(tt31, 0)
#     expr = expr.subs(tt51, 0)
#     expr = expr.subs(tt71, 0)

#     expr = expr.subs(d0, l1)
#     expr = expr.subs(d1, l2)
#     expr = expr.subs(d2, 0)
#     expr = expr.subs(d3, l3+l4)
#     expr = expr.subs(d4, 0)
#     expr = expr.subs(d5, l5+l6)
#     expr = expr.subs(d6, 0)
#     expr = expr.subs(d7, 0)

#     expr = expr.subs(d31, l3)
#     expr = expr.subs(d51, l5)
#     expr = expr.subs(d71, l7)

#     expr = expr.subs(aa0, 0)
#     expr = expr.subs(aa1, -pi/2)
#     expr = expr.subs(aa2, pi/2)
#     expr = expr.subs(aa3, pi/2)
#     expr = expr.subs(aa4, -pi/2)
#     expr = expr.subs(aa5, -pi/2)
#     expr = expr.subs(aa6, pi/2)
#     expr = expr.subs(aa7, 0)

#     expr = expr.subs(aa31, 0)
#     expr = expr.subs(aa51, 0)
#     expr = expr.subs(aa71, 0)

#     expr = expr.subs(a0, 0)
#     expr = expr.subs(a1, 0)
#     expr = expr.subs(a2, 0)
#     expr = expr.subs(a3, 0)
#     expr = expr.subs(a4, 0)
#     expr = expr.subs(a5, 0)
#     expr = expr.subs(a6, 0)
#     expr = expr.subs(a7, 0)

#     expr = expr.subs(a31, 0)
#     expr = expr.subs(a51, 0)
#     expr = expr.subs(a71, 0)

#     expr = expr.subs(tt1cm, pi/2)
#     expr = expr.subs(tt2cm, pi/2)
#     expr = expr.subs(tt3cm, pi/2)
#     expr = expr.subs(tt4cm, pi/2)
#     expr = expr.subs(tt5cm, pi/2)
#     expr = expr.subs(tt6cm, pi/2)
#     expr = expr.subs(tt7cm, pi/2)

#     expr = expr.subs(d1cm, l1cm)
#     expr = expr.subs(d2cm, l2cm)
#     expr = expr.subs(d3cm, l3cm)
#     expr = expr.subs(d4cm, l4cm)
#     expr = expr.subs(d5cm, l5cm)
#     expr = expr.subs(d6cm, l6cm)
#     expr = expr.subs(d7cm, l7cm)

#     expr = expr.subs(a1cm, h1cm)
#     expr = expr.subs(a2cm, h2cm)
#     expr = expr.subs(a3cm, h3cm)
#     expr = expr.subs(a4cm, h4cm)
#     expr = expr.subs(a5cm, h5cm)
#     expr = expr.subs(a6cm, h6cm)
#     expr = expr.subs(a7cm, h7cm)
#     expr = expr.subs(a5cm1, m5cm)

#     expr = expr.subs(aa1cm, 0)
#     expr = expr.subs(aa2cm, 0)
#     expr = expr.subs(aa3cm, 0)
#     expr = expr.subs(aa4cm, 0)
#     expr = expr.subs(aa5cm, 0)
#     expr = expr.subs(aa6cm, 0)
#     expr = expr.subs(aa7cm, 0)

#     return expr

# # - | d | alpha | a
# DH = [[tt0, d0, aa0, a0],
#       [tt1, d1, aa1, a1],
#       [tt2, d2, aa2, a2],
#       [tt3, d3, aa3, a3],
#       [tt4, d4, aa4, a4],
#       [tt5, d5, aa5, a5],
#       [tt6, d6, aa6, a6],
#       [tt7, d7, aa7, a7]]

# H01 = H(*DH[0])
# print("simplify H01")
# # H01 = simplify(H01)
# H02 = H01 * H(*DH[1])
# print("simplify H02")
# # H02 = simplify(H02)
# H03 = H02 * H(*DH[2])
# print("simplify H03")
# # H03 = simplify(H03)
# H04 = H03 * H(*DH[3]) 
# print("simplify H04")
# # H04 = simplify(H04)
# H05 = H04 * H(*DH[4])
# print("simplify H05")
# # H05 = simplify(H05)
# H06 = H05 * H(*DH[5])
# print("simplify H06")
# # H06 = simplify(H06)
# H07 = H06 * H(*DH[6])
# print("simplify H07")
# # H07 = simplify(H07)

# from s import tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7
# from s import d0, d1, d2, d3, d4, d5, d6, d7
# from s import aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7
# from s import a0, a1, a2, a3, a4, a5, a6, a7

# from H01 import H01
# from H02 import H02
# from H03 import H03
# from H04 import H04
# from H05 import H05
# from H06 import H06
# from H07 import H07



# fk1 = H01(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt1, 0, 0, 0)
# fk2 = H02(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt2, 0, 0, 0)
# fk3 = H03(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt31, d31, aa31, a31) * H(tt3, 0, 0, 0)
# fk4 = H04(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt4, 0, 0, 0)
# fk5 = H05(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt51, d51, aa51, a51) * H(tt5, 0, 0, 0)
# fk6 = H06(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt6, 0, 0, 0)
# fk7 = H07(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt71, d71, aa71, a71) * H(tt7, 0, 0, 0)


# print("simplify fk1")
# # fk1 = simplify(fk1)
# print("simplify fk2")
# # fk2 = simplify(fk2)
# print("simplify fk3")
# # fk3 = simplify(fk3)
# print("simplify fk4")
# # fk4 = simplify(fk4)
# print("simplify fk5")
# # fk5 = simplify(fk5)
# print("simplify fk6")
# # fk6 = simplify(fk6)
# print("simplify fk7")
# # fk7 = simplify(fk7)

# from fk1 import fk1
# from fk2 import fk2
# from fk3 import fk3
# from fk4 import fk4
# from fk5 import fk5
# from fk6 import fk6
# from fk7 import fk7


# fk1cm = fk1(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt1cm, d1cm, aa1cm, a1cm)
# fk2cm = fk2(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt2cm, d2cm, aa2cm, a2cm)
# fk3cm = fk3(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt3cm, d3cm, aa3cm, a3cm)
# fk4cm = fk4(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt4cm, d4cm, aa4cm, a4cm) 
# fk5cm = fk5(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(0, 0, 0, a5cm1) * H(tt5cm, d5cm, aa5cm, a5cm)
# fk6cm = fk6(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt6cm, d6cm, aa6cm, a6cm)
# fk7cm = fk7(tt1, tt2, tt3, tt4, tt5, tt6, tt7) * H(tt7cm, d7cm, aa7cm, a7cm)

# print("simplify fk1cm")
# # fk1cm = simplify(fk1cm)
# print("simplify fk2cm")
# # fk2cm = simplify(fk2cm)
# print("simplify fk3cm")
# # fk3cm = simplify(fk3cm)
# print("simplify fk4cm")
# # fk4cm = simplify(fk4cm)
# print("simplify fk5cm")
# # fk5cm = simplify(fk5cm)
# print("simplify fk6cm")
# # fk6cm = simplify(fk6cm)
# print("simplify fk7cm")
# # fk7cm = simplify(fk7cm)





# def outputFK(name, calc):
#     calc = subValues(calc)

#     with open(f"{name}.py", "w") as f:
#         f.write(f"""
# from math import sin, cos
# import numpy as np

# def {name}(qpos):
# """)
        
#         f.write("\ttt1, tt2, tt3, tt4, tt5, tt6, tt7 = qpos\n")
#         f.write("\tx = " + str(calc[0,3]) + "\n")
#         f.write("\ty = " + str(calc[1,3]) + "\n")
#         f.write("\tz = " + str(calc[2,3]) + "\n")
#         f.write("\tpos = np.array([x, y, z])\n")
#         f.write("\tmat = np.zeros((3,3))\n")
#         for i in range(3):
#             for j in range(3):
#                 f.write(f"\tmat[{i},{j}] = " + str(calc[i, j]) + "\n")
#         f.write("\treturn pos, mat")

# for i, j in zip(range(7), [fk1, fk2, fk3, fk4, fk5, fk6, fk7]):
#     outputFK(f"fk{i+1}", j)


# for i, j in zip(range(7), [fk1cm, fk2cm, fk3cm, fk4cm, fk5cm, fk6cm, fk7cm]):
#     outputFK(f"fk{i+1}cm", j)

fk1cm = subValues(fk1cm)
fk2cm = subValues(fk2cm)
fk3cm = subValues(fk3cm)
fk4cm = subValues(fk4cm)
fk5cm = subValues(fk5cm)
fk6cm = subValues(fk6cm)
fk7cm = subValues(fk7cm)



t1cm = fk1cm[:3,3]
t2cm = fk2cm[:3,3]
t3cm = fk3cm[:3,3]
t4cm = fk4cm[:3,3]
t5cm = fk5cm[:3,3]
t6cm = fk6cm[:3,3]
t7cm = fk7cm[:3,3]

R1cm = fk1cm[:3,:3]
R2cm = fk2cm[:3,:3]
R3cm = fk3cm[:3,:3]
R4cm = fk4cm[:3,:3]
R5cm = fk5cm[:3,:3]
R6cm = fk6cm[:3,:3]
R7cm = fk7cm[:3,:3]


t1  = fk1 [:3,3]
t2  = fk2 [:3,3]
t3  = fk3 [:3,3]
t4  = fk4 [:3,3]
t5  = fk5 [:3,3]
t6  = fk6 [:3,3]
t7  = fk7 [:3,3]

g = Matrix([0, 0, gz])
# pprint(g)
# pprint(fk1cm)
# pprint(t1cm)

P = g.transpose() * (m1 * t1cm +\
                    m2 * t2cm  +\
                    m3 * t3cm  +\
                    m4 * t4cm  +\
                    m5 * t5cm  +\
                    m6 * t6cm  +\
                    m7 * t7cm)

# pprint(P)

G = Matrix([[P.diff(tt1)],
            [P.diff(tt2)],
            [P.diff(tt3)],
            [P.diff(tt4)],
            [P.diff(tt5)],
            [P.diff(tt6)],
            [P.diff(tt7)]])

G = G.subs(gz, 9.81)
G = G.subs(m1, 5.76)
G = G.subs(m2, 6.35)
G = G.subs(m3, 3.5)
G = G.subs(m4, 3.5)
G = G.subs(m5, 3.5)
G = G.subs(m6, 1.8)
G = G.subs(m7, 1.2)

def outputG():
    with open(f"G.py", "w") as f:
        f.write(f"""
from math import sin, cos
import numpy as np

def G(qpos):
""")
        
        f.write("\ttt1, tt2, tt3, tt4, tt5, tt6, tt7 = qpos\n")
        f.write("\tg = np.zeros(7)\n")
        for i in range(7):
            f.write(f"\tg[{i}] = " + str(G[i]) + "\n")
        f.write("\treturn g")

# outputG()

# Jcm I t

z0 = Matrix([[0], [0], [1]])
z1 = fk1[:3,2]
z2 = fk2[:3,2]
z3 = fk3[:3,2]
z4 = fk4[:3,2]
z5 = fk5[:3,2]
z6 = fk6[:3,2]
z7 = fk7[:3,2]

# J1cm = Matrix([[z0.cross(t1cm), 0, 0, 0, 0, 0, 0],
#               [z0, 0, 0, 0, 0, 0, 0]])

J1cm = Matrix([z0.cross(t1cm), z0]).row_join(zeros(6,6))


# J2cm = Matrix([[z0.cross(t2cm), z1.cross((t2cm - t1)), 0, 0, 0, 0, 0],
#               [z0, z1, 0, 0, 0, 0, 0]])

J2cm = Matrix([z0.cross(t2cm), z0])\
        .row_join(Matrix([z1.cross(t2cm - t1), z1])).row_join(zeros(6,5))


# J3cm = Matrix([[z0.cross(t3cm), z1.cross((t3cm - t1)), z2.cross((t3cm - t2)), 0, 0, 0, 0],
#               [z0, z1, z2, 0, 0, 0, 0]])

J3cm = Matrix([z0.cross(t3cm), z0])\
    .row_join(Matrix([z1.cross(t3cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t3cm - t2), z2])).row_join(zeros(6,4))

# J4cm = Matrix([[z0.cross(t4cm), z1.cross((t4cm - t1)), z2.cross((t4cm - t2)), z3.cross((t4cm - t3)), 0, 0, 0],
#               [z0, z1, z2, z3, 0, 0, 0]])

J4cm = Matrix([z0.cross(t4cm), z0])\
    .row_join(Matrix([z1.cross(t4cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t4cm - t2), z2]))\
    .row_join(Matrix([z3.cross(t4cm - t3), z3])).row_join(zeros(6,3))

# J5cm = Matrix([[z0.cross(t5cm), z1.cross((t5cm - t1)), z2.cross((t5cm - t2)), z3.cross((t5cm - t3)), z4.cross((t5cm - t4)), 0, 0],
#               [z0, z1, z2, z3, z4, 0, 0]])

J5cm = Matrix([z0.cross(t5cm), z0])\
    .row_join(Matrix([z1.cross(t5cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t5cm - t2), z2]))\
    .row_join(Matrix([z3.cross(t5cm - t3), z3]))\
    .row_join(Matrix([z4.cross(t5cm - t4), z4])).row_join(zeros(6,2))

# J6cm = Matrix([[z0.cross(t6cm), z1.cross((t6cm - t1)), z2.cross((t6cm - t2)), z3.cross((t6cm - t3)), z4.cross((t6cm - t4)), z5.cross((t6cm - t5)), 0],
#               [z0, z1, z2, z3, z4, z5, 0]])

J6cm = Matrix([z0.cross(t6cm), z0])\
    .row_join(Matrix([z1.cross(t6cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t6cm - t2), z2]))\
    .row_join(Matrix([z3.cross(t6cm - t3), z3]))\
    .row_join(Matrix([z4.cross(t6cm - t4), z4]))\
    .row_join(Matrix([z5.cross(t6cm - t5), z5])).row_join(zeros(6,1))

# J7cm = Matrix([[z0.cross(t7cm), z1.cross((t7cm - t1)), z2.cross((t7cm - t2)), z3.cross((t7cm - t3)), z4.cross((t7cm - t4)), z5.cross((t7cm - t5)), z6.cross((t7cm - t6))],
#               [z0, z1, z2, z3, z4, z5, z6]])

J7cm = Matrix([z0.cross(t7cm), z0])\
    .row_join(Matrix([z1.cross(t7cm - t1), z1]))\
    .row_join(Matrix([z2.cross(t7cm - t2), z2]))\
    .row_join(Matrix([z3.cross(t7cm - t3), z3]))\
    .row_join(Matrix([z4.cross(t7cm - t4), z4]))\
    .row_join(Matrix([z5.cross(t7cm - t5), z5]))\
    .row_join(Matrix([z6.cross(t7cm - t6), z6]))


print("simplifying J...")
print("simpllify J1cm")
# J1cm = simplify(J1cm)
print("simpllify J2cm")
# J2cm = simplify(J2cm)
print("simpllify J3cm")
# J3cm = simplify(J3cm)
print("simpllify J4cm")
# J4cm = simplify(J4cm)
print("simpllify J5cm")
# J5cm = simplify(J5cm)
print("simpllify J6cm")
# J6cm = simplify(J6cm)
print("simpllify J7cm")
# J7cm = simplify(J7cm)
print("simplifying J end")


def split(J):
    return J[:3, :], J[:3, :]

(J1cmv, J1cmw), (J2cmv, J2cmw), (J3cmv, J3cmw), (J4cmv, J4cmw), (J5cmv, J5cmw), (J6cmv, J6cmw), (J7cmv, J7cmw) = split(J1cm), split(J2cm), split(J3cm), split(J4cm), split(J5cm), split(J6cm), split(J7cm)


I1cm = diag(0.033, 0.0333, 0.0123)
I2cm = diag(0.0305, 0.0304, 0.011)
I3cm = diag(0.025, 0.0238, 0.0076)
I4cm = diag(0.017, 0.0164, 0.006)
I5cm = diag(0.01, 0.0087, 0.00449)
I6cm = diag(0.0049, 0.0047, 0.0036)
I7cm = diag(0.001, 0.001, 0.001)

tt = Matrix([tt1, tt2, tt3, tt4, tt5, tt6, tt7])


M1 = (m1 * J1cmv.transpose() * J1cmv) +\
    (m2 * J2cmv.transpose() * J2cmv) +\
    (m3 * J3cmv.transpose() * J3cmv) +\
    (m4 * J4cmv.transpose() * J4cmv) +\
    (m5 * J5cmv.transpose() * J5cmv) +\
    (m6 * J6cmv.transpose() * J6cmv) +\
    (m7 * J7cmv.transpose() * J7cmv)

M2 = (J1cmw.transpose() * R1cm * I1cm * R1cm.transpose()  *J1cmw) +\
    (J2cmw.transpose() * R2cm * I2cm * R2cm.transpose()  *J2cmw) +\
    (J3cmw.transpose() * R3cm * I3cm * R3cm.transpose()  *J3cmw) +\
    (J4cmw.transpose() * R4cm * I4cm * R4cm.transpose()  *J4cmw) +\
    (J5cmw.transpose() * R5cm * I5cm * R5cm.transpose()  *J5cmw) +\
    (J6cmw.transpose() * R6cm * I6cm * R6cm.transpose()  *J6cmw) +\
    (J7cmw.transpose() * R7cm * I7cm * R7cm.transpose()  *J7cmw)

print("simplifying...")
# M1 = simplify(M1)
# M2 = simplify(M2)
M = M1 + M2
# M = simplify(M)
# print(M)
print("simplifying end")


def outputM():
    with open(f"M.py", "w") as f:
        f.write(f"""
from math import sin, cos
import numpy as np

def M(qpos):
""")
        
        f.write("\ttt1, tt2, tt3, tt4, tt5, tt6, tt7 = qpos\n")
        f.write("\tm = np.zeros((7,7))\n")
        for i in range(7):
            for j in range(7):
                print(i, j)
                f.write(f"\tm[{i},{j}] = " + str(M[i,j]) + "\n")
        f.write("\treturn m")

# outputM()

print("M diff tt1")
Mtt1 = M.diff(tt1)
print("M diff tt2")
Mtt2 = M.diff(tt2)
print("M diff tt3")
Mtt3 = M.diff(tt3)
print("M diff tt4")
Mtt4 = M.diff(tt4)
print("M diff tt5")
Mtt5 = M.diff(tt5)
print("M diff tt6")
Mtt6 = M.diff(tt6)
print("M diff tt7")
Mtt7 = M.diff(tt7)

MM = [Mtt1, Mtt2, Mtt3, Mtt4, Mtt5, Mtt6, Mtt7]

dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7 = symbols("dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7")
dtt = [dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7]

def chrisSym(k, j):
    c = 0
    for i in range(7):
        c = (MM[i][k,j] - 1/2*MM[k][i, j]) * dtt[i]
    return c

C = zeros((7,7))
for k in range(7):
    for j in range(7):
        print(k, j)
        C[k, j] = chrisSym(k, j)

# K = 1/2*tt.transpose()*M*tt
# pprint(K)
print("done")