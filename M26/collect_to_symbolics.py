import time 

def read_from(i, j):
    s = ""
    with open(f"{i}_{j}.txt") as f:
        s = f.read()
    
    return s

name = "M26"
param = "tt1, tt2, tt3, tt4, tt5, tt6, tt7"
sim_on = True

start = time.time()
with open(f"{name}S.py", "w") as f:
    f.write("from sympy import Matrix, cos, sin, zeros, shape, pi, sqrt\n")
    f.write(f"def {name}S({param}):\n")
    s = (7,7)
    f.write(f"\texpr = zeros({s[0]},{s[1]})\n")
    for i in range(s[0]):
        for j in range(s[1]):
            print(f"{s[0]*s[1]} / {i*s[0]+j}")
            f.write(f"\texpr[{i},{j}] = " + str(read_from(i,j)) +"\n")

    if sim_on:
        f.write("\t#simplified\n")
    print("Output duration:", time.time() - start)
    f.write(f"\treturn  expr\n")