
from math import sin, cos, pi, sqrt
import numpy as np

def fk2(qpos):
	tt1, tt2, tt3, tt4, tt5, tt6, tt7 = qpos
	x = 1.36000000000000
	y = 1.36000000000000
	z = 1.36000000000000
	pos = np.array([x, y, z])
	mat = np.zeros((3,3))
	mat[0,0] = -sin(tt2) + sqrt(2)*sin(tt1 + pi/4)*cos(tt2)
	mat[0,1] = -sqrt(2)*sin(tt2)*sin(tt1 + pi/4) - cos(tt2)
	mat[0,2] = -sin(tt1) + cos(tt1)
	mat[1,0] = -sin(tt2) + sqrt(2)*sin(tt1 + pi/4)*cos(tt2)
	mat[1,1] = -sqrt(2)*sin(tt2)*sin(tt1 + pi/4) - cos(tt2)
	mat[1,2] = -sin(tt1) + cos(tt1)
	mat[2,0] = -sin(tt2) + sqrt(2)*sin(tt1 + pi/4)*cos(tt2)
	mat[2,1] = -sqrt(2)*sin(tt2)*sin(tt1 + pi/4) - cos(tt2)
	mat[2,2] = -sin(tt1) + cos(tt1)
	return pos, mat