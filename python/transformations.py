from sympy import sin, cos, Matrix

def Rz(angle):
    return Matrix([[cos(angle), -sin(angle), 0, 0],
                    [sin(angle), cos(angle), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

def Ry(angle):
    return Matrix([[cos(angle), 0, sin(angle), 0],
                    [0, 1, 0, 0],
                    [-sin(angle), 0, cos(angle), 0],
                    [0, 0, 0, 1]])

def Rx(angle):
    return Matrix([[1, 0, 0, 0],
                    [0, cos(angle), -sin(angle), 0],
                    [0, sin(angle), cos(angle), 0],
                    [0, 0, 0, 1]])

def Tz(distance):
    return Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, distance],
                    [0, 0, 0, 1]])

def Ty(distance):
    return Matrix([[1, 0, 0, 0],
                    [0, 1, 0, distance],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

def Tx(distance):
    return Matrix([[1, 0, 0, distance],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

def H(tt, d, aa, a):
    return Rz(tt)*Tz(d)*Rx(aa)*Tx(a)

