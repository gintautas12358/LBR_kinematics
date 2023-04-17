from sympy import symbols, shape

# from H01S import H01S
# from H02S import H02S
# from H03S import H03S
# from H04S import H04S
# from H05S import H05S
# from H06S import H06S
# from H07S import H07S

from fk.fk1S import fk1S
from fk.fk2S import fk2S
from fk.fk3S import fk3S
from fk.fk4S import fk4S
from fk.fk5S import fk5S
from fk.fk6S import fk6S
from fk.fk7S import fk7S

# from fk1cmS import fk1cmS
# from fk2cmS import fk2cmS
# from fk3cmS import fk3cmS
# from fk4cmS import fk4cmS
# from fk5cmS import fk5cmS
# from fk6cmS import fk6cmS
# from fk7cmS import fk7cmS

# from GS import GS
# from MS import MS
# from CS import CS


def outputTransformCode(name, expr):

    with open(f"code/{name}.py", "w") as f:
        f.write(f"""
from math import sin, cos, pi, sqrt
import numpy as np

def {name}(qpos):
""")
        
        f.write("\ttt1, tt2, tt3, tt4, tt5, tt6, tt7 = qpos\n")
        f.write("\tx = " + str(expr[0,3]) + "\n")
        f.write("\ty = " + str(expr[1,3]) + "\n")
        f.write("\tz = " + str(expr[2,3]) + "\n")
        f.write("\tpos = np.array([x, y, z])\n")
        f.write("\tmat = np.zeros((3,3))\n")
        for i in range(3):
            for j in range(3):
                f.write(f"\tmat[{i},{j}] = " + str(expr[i, j]) + "\n")
        f.write("\treturn pos, mat")


def outputCodeTemplate(name, expr, inputs, params):
    with open(f"code/{name}.py", "w") as f:
        f.write(f"""
from math import sin, cos
import numpy as np


""")    
        f.write(f"def {name}(")
        for i, ii in enumerate(inputs):
            f.write(f"{ii}")
            if i != len(inputs)-1:
                f.write(",")
        f.write("):\n")


        for i, p in zip(inputs, params):
            f.write(f"\t{p} = {i}\n")

        s = shape(expr)
        f.write(f"\tm = np.zeros(({s[0]},{s[1]}))\n")
        for i in range(s[0]):
            for j in range(s[1]):
                print(f"{s[0]*s[1]} / {i*s[0]+j}")
                f.write(f"\tm[{i},{j}] = " + str(expr[i,j]) + "\n")
        f.write("\treturn m")

def outputMatrixCode(name, expr):
    return outputCodeTemplate(name, expr, ["qpos"], ["tt1, tt2, tt3, tt4, tt5, tt6, tt7"])

def outputCCode(name, expr):
    return outputCodeTemplate(name, expr, ["qpos", "qvel"], ["tt1, tt2, tt3, tt4, tt5, tt6, tt7", "dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7"])


tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7")
# dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7 = symbols("dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7")


fk1 = fk1S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk2 = fk2S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk3 = fk3S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk4 = fk4S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk5 = fk5S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk6 = fk6S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
fk7 = fk7S(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

print("writing fk...")
for i, j in zip(range(7), [fk1, fk2, fk3, fk4, fk5, fk6, fk7]):
    outputTransformCode(f"fk{i+1}", j)


# fk1cm = fk1cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
# fk2cm = fk2cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
# fk3cm = fk3cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
# fk4cm = fk4cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
# fk5cm = fk5cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
# fk6cm = fk6cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)
# fk7cm = fk7cmS(tt1, tt2, tt3, tt4, tt5, tt6, tt7)

# print("writing fkcm...")
# for i, j in zip(range(7), [fk1cm, fk2cm, fk3cm, fk4cm, fk5cm, fk6cm, fk7cm]):
#     outputTransformCode(f"fk{i+1}cm", j)

# print("writing G...")
# outputMatrixCode("G", GS(tt1, tt2, tt3, tt4, tt5, tt6, tt7))
# print("writing M...")
# outputMatrixCode("M", MS(tt1, tt2, tt3, tt4, tt5, tt6, tt7))
# print("writing C...")
# outputCCode("C", CS(tt1, tt2, tt3, tt4, tt5, tt6, tt7, dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7))
# print("done")

