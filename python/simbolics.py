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


def outputExpr(name, expr):
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

