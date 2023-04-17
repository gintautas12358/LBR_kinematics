
from math import sin, cos
import numpy as np


def G(qpos):
	tt1, tt2, tt3, tt4, tt5, tt6, tt7 = qpos
	m = np.zeros((7,1))
	m[0,0] = 0
	m[1,0] = (-1.1783772*(sin(tt2)*sin(tt4) + cos(tt2)*cos(tt3)*cos(tt4))*cos(tt5) + 1.1783772*sin(tt3)*sin(tt5)*cos(tt2))*sin(tt6) + (0.0034335*sin(tt2)*sin(tt4) + 0.0034335*cos(tt2)*cos(tt3)*cos(tt4))*cos(tt5) - (0.7139718*sin(tt2)*sin(tt4) + 0.7139718*cos(tt2)*cos(tt3)*cos(tt4))*sin(tt5) - (1.1783772*sin(tt2)*cos(tt4) - 1.1783772*sin(tt4)*cos(tt2)*cos(tt3))*cos(tt6) - 23.0167125*sin(tt2)*cos(tt4) - 56.362374*sin(tt2) - 0.0034335*sin(tt3)*sin(tt5)*cos(tt2) - 0.7139718*sin(tt3)*cos(tt2)*cos(tt5) - 0.13734*sin(tt3)*cos(tt2) + 23.0167125*sin(tt4)*cos(tt2)*cos(tt3)
	m[2,0] = ((1.1783772*sin(tt3)*cos(tt4)*cos(tt5) + 1.1783772*sin(tt5)*cos(tt3))*sin(tt6) - 1.1783772*sin(tt3)*sin(tt4)*cos(tt6) - 23.0167125*sin(tt3)*sin(tt4) + 0.7139718*sin(tt3)*sin(tt5)*cos(tt4) - 0.0034335*sin(tt3)*cos(tt4)*cos(tt5) - 0.0034335*sin(tt5)*cos(tt3) - 0.7139718*cos(tt3)*cos(tt5) - 0.13734*cos(tt3))*sin(tt2)
	m[3,0] = -(0.0034335*sin(tt2)*sin(tt4)*cos(tt3) + 0.0034335*cos(tt2)*cos(tt4))*cos(tt5) + (0.7139718*sin(tt2)*sin(tt4)*cos(tt3) + 0.7139718*cos(tt2)*cos(tt4))*sin(tt5) + (1.1783772*sin(tt2)*sin(tt4)*cos(tt3) + 1.1783772*cos(tt2)*cos(tt4))*sin(tt6)*cos(tt5) + (1.1783772*sin(tt2)*cos(tt3)*cos(tt4) - 1.1783772*sin(tt4)*cos(tt2))*cos(tt6) + 23.0167125*sin(tt2)*cos(tt3)*cos(tt4) - 23.0167125*sin(tt4)*cos(tt2)
	m[4,0] = (1.1783772*(sin(tt2)*cos(tt3)*cos(tt4) - sin(tt4)*cos(tt2))*sin(tt5) + 1.1783772*sin(tt2)*sin(tt3)*cos(tt5))*sin(tt6) - (0.0034335*sin(tt2)*cos(tt3)*cos(tt4) - 0.0034335*sin(tt4)*cos(tt2))*sin(tt5) - (0.7139718*sin(tt2)*cos(tt3)*cos(tt4) - 0.7139718*sin(tt4)*cos(tt2))*cos(tt5) + 0.7139718*sin(tt2)*sin(tt3)*sin(tt5) - 0.0034335*sin(tt2)*sin(tt3)*cos(tt5)
	m[5,0] = (-1.1783772*(sin(tt2)*cos(tt3)*cos(tt4) - sin(tt4)*cos(tt2))*cos(tt5) + 1.1783772*sin(tt2)*sin(tt3)*sin(tt5))*cos(tt6) - (1.1783772*sin(tt2)*sin(tt4)*cos(tt3) + 1.1783772*cos(tt2)*cos(tt4))*sin(tt6)
	m[6,0] = 0
	return m