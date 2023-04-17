from sympy import simplify, symbols, pi, shape, zeros, expand
import time

sim_on = True

def simp(expr):
    if not sim_on:
        print("simplification skiped")
        return expr
    size0 = len(str(expr))
    expr = simplify(expr)
    size1 = len(str(expr))
    print("Compresed from", size0, "to", size1)
    return expr

def simpLong(expr):
    if not sim_on:
        print("simplification skiped")
        return expr
    
    start = time.time()
    total_size0, total_size1 = 0, 0 
    size0 = len(str(expr))
    s = shape(expr)
    n_expr = zeros(*s)
    for i in range(s[0]):
        for j in range(s[1]):
            print(f"{s[0]*s[1]} / {i*s[0]+j}")
            size0 = len(str(expr[i,j]))
            n_expr[i,j] = simplify(expr[i,j])
            size1 = len(str(n_expr[i,j]))
            print("Compresed from", size0, "to", size1)
            total_size0 += size0
            total_size1 += size1
    print("In total compresed from", total_size0, "to", total_size1)
    print("Simplifiction duration:", time.time() - start)
    return n_expr

def genExp(expr_name, expr): 
      print(f"simplify {expr_name}")
      expr = simpLong(expr)
      outputExprLong(expr_name, expr)
      return expr

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

def subValues(expr):

    l1 = 0.1575
    l2 = 0.2025
    l3 = 0.2045
    l4 = 0.2155
    l5 = 0.1845
    l6 = 0.2155
    l7 = 0.081

    l1cm = 0.12
    l2cm = 0.042
    l3cm = 0.13
    l4cm = 0.034
    l5cm = 0.076
    l6cm = 0.0004
    l7cm = 0.02

    h1cm = -0.03
    h2cm = -0.059
    h3cm = 0.03
    h4cm = 0.067
    h5cm = -0.021
    h6cm = 0.0006
    h7cm = 0.0

    m5cm = -0.0001

    expr = expr.subs(tt0, 0)
    expr = expr.subs(tt31, 0)
    expr = expr.subs(tt51, 0)
    expr = expr.subs(tt71, 0)

    expr = expr.subs(d0, l1)
    expr = expr.subs(d1, l2)
    expr = expr.subs(d2, 0)
    expr = expr.subs(d3, l3+l4)
    expr = expr.subs(d4, 0)
    expr = expr.subs(d5, l5+l6)
    expr = expr.subs(d6, 0)
    expr = expr.subs(d7, 0)

    expr = expr.subs(d31, l3)
    expr = expr.subs(d51, l5)
    expr = expr.subs(d71, l7)

    expr = expr.subs(aa0, 0)
    expr = expr.subs(aa1, -pi/2)
    expr = expr.subs(aa2, pi/2)
    expr = expr.subs(aa3, pi/2)
    expr = expr.subs(aa4, -pi/2)
    expr = expr.subs(aa5, -pi/2)
    expr = expr.subs(aa6, pi/2)
    expr = expr.subs(aa7, 0)

    expr = expr.subs(aa31, 0)
    expr = expr.subs(aa51, 0)
    expr = expr.subs(aa71, 0)

    expr = expr.subs(a0, 0)
    expr = expr.subs(a1, 0)
    expr = expr.subs(a2, 0)
    expr = expr.subs(a3, 0)
    expr = expr.subs(a4, 0)
    expr = expr.subs(a5, 0)
    expr = expr.subs(a6, 0)
    expr = expr.subs(a7, 0)

    expr = expr.subs(a31, 0)
    expr = expr.subs(a51, 0)
    expr = expr.subs(a71, 0)

    expr = expr.subs(tt1cm, pi/2)
    expr = expr.subs(tt2cm, pi/2)
    expr = expr.subs(tt3cm, pi/2)
    expr = expr.subs(tt4cm, pi/2)
    expr = expr.subs(tt5cm, pi/2)
    expr = expr.subs(tt6cm, pi/2)
    expr = expr.subs(tt7cm, pi/2)

    expr = expr.subs(d1cm, l1cm)
    expr = expr.subs(d2cm, l2cm)
    expr = expr.subs(d3cm, l3cm)
    expr = expr.subs(d4cm, l4cm)
    expr = expr.subs(d5cm, l5cm)
    expr = expr.subs(d6cm, l6cm)
    expr = expr.subs(d7cm, l7cm)

    expr = expr.subs(a1cm, h1cm)
    expr = expr.subs(a2cm, h2cm)
    expr = expr.subs(a3cm, h3cm)
    expr = expr.subs(a4cm, h4cm)
    expr = expr.subs(a5cm, h5cm)
    expr = expr.subs(a6cm, h6cm)
    expr = expr.subs(a7cm, h7cm)
    expr = expr.subs(a5cm1, m5cm)

    expr = expr.subs(aa1cm, 0)
    expr = expr.subs(aa2cm, 0)
    expr = expr.subs(aa3cm, 0)
    expr = expr.subs(aa4cm, 0)
    expr = expr.subs(aa5cm, 0)
    expr = expr.subs(aa6cm, 0)
    expr = expr.subs(aa7cm, 0)

    return expr

def outputExpr(name, expr):
    expr = subValues(expr)
    with open(f"{name}S.py", "w") as f:
        f.write("from sympy import Matrix, cos, sin\n")
        f.write(f"def {name}S(tt1, tt2, tt3, tt4, tt5, tt6, tt7):\n")
        if sim_on:
            f.write("\t#simplified\n")
        f.write(f"\treturn  " + str(expr) + "\n")

def outputTemplate(name, expr, param):
    start = time.time()
    with open(f"{name}S.py", "w") as f:
        f.write("from sympy import Matrix, cos, sin, zeros, shape, pi, sqrt\n")
        f.write(f"def {name}S({param}):\n")
        s = shape(expr)
        f.write(f"\texpr = zeros({s[0]},{s[1]})\n")
        for i in range(s[0]):
            for j in range(s[1]):
                print(f"{s[0]*s[1]} / {i*s[0]+j}")
                f.write(f"\texpr[{i},{j}] = " + str(expr[i,j]) +"\n")

        if sim_on:
            f.write("\t#simplified\n")
        print("Output duration:", time.time() - start)
        f.write(f"\treturn  expr\n")

def outputExprLong(name, expr):
    return outputTemplate(name, expr, "tt1, tt2, tt3, tt4, tt5, tt6, tt7")

def outputCLong(name, expr):
    return outputTemplate(name, expr, "tt1, tt2, tt3, tt4, tt5, tt6, tt7, dtt1, dtt2, dtt3, dtt4, dtt5, dtt6, dtt7")

def diffLong(expr, x):
    s = shape(expr)
    n_expr = zeros(*s)
    for i in range(s[0]):
        for j in range(s[1]):
            print(f"{s[0]*s[1]} / {i*s[0]+j}")
            n_expr[i,j] = expr[i,j].diff(x)
    return n_expr

