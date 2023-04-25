from sympy import symbols, expand, trigsimp, expand_trig, factor, sqrt, sin, cos, powsimp, collect
from simbolics import outputExprLong, simpLong

# from Mparts.M26S import M26S
# from Mparts.M27S import M27S
from M27S import M27S

tt0, tt1, tt2, tt3, tt4, tt5, tt6, tt7 = symbols("tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7", positive=True)


# M26 = M26S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
# M27 = M27S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
M = M27S( tt1, tt2, tt3, tt4, tt5, tt6, tt7)
for i in range(7):
    for j in range(7):
        m = M[i, j]
        with open(f"{i}_{j}.txt", "w") as f:
            

            print(len(str(m)))
            print()
            # m = expand(m)
            # print(len(str(m)))
            # print()
            # m = m.replace(cos, lambda a: sqrt(1-sin(a)**2))
            # print(len(str(m)))
            # print()
            # m = expand(m)
            # print(len(str(m)))
            # print()
            # print(1)
            # m = m.replace(sqrt(1-sin(tt1)**2), cos(tt1))
            # print(2)
            # m = m.replace(sqrt(1-sin(tt2)**2), cos(tt2))
            # print(3)
            # m = m.replace(sqrt(1-sin(tt3)**2), cos(tt3))
            # print(4)
            # m = m.replace(sqrt(1-sin(tt4)**2), cos(tt4))
            # print(5)
            # m = m.replace(sqrt(1-sin(tt5)**2), cos(tt5))
            # print(6)
            # m = m.replace(sqrt(1-sin(tt6)**2), cos(tt6))
            # print(7)
            # m = m.replace(sqrt(1-sin(tt7)**2), cos(tt7))
            # print(len(str(m)))
            # print()
            # m = expand(m)
            # print(len(str(m)))
            # print()
            m = trigsimp(m)
            print(len(str(m)))
            print()


            f.write(str(m))