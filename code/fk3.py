
from math import sin, cos, pi, sqrt
import numpy as np

def fk3(qpos):
	tt1, tt2, tt3, tt4, tt5, tt6, tt7 = qpos
	x = 0.2045*sqrt(2)*sin(tt2)*sin(tt1 + pi/4) + 0.2045*cos(tt2) + 1.36
	y = 0.2045*sqrt(2)*sin(tt2)*sin(tt1 + pi/4) + 0.2045*cos(tt2) + 1.36
	z = 0.2045*sqrt(2)*sin(tt2)*sin(tt1 + pi/4) + 0.2045*cos(tt2) + 1.36
	pos = np.array([x, y, z])
	mat = np.zeros((3,3))
	mat[0,0] = (-sin(tt2) + sqrt(2)*sin(tt1 + pi/4)*cos(tt2))*cos(tt3) + sqrt(2)*sin(tt3)*cos(tt1 + pi/4)
	mat[0,1] = (sin(tt2) - sqrt(2)*sin(tt1 + pi/4)*cos(tt2))*sin(tt3) + sqrt(2)*cos(tt3)*cos(tt1 + pi/4)
	mat[0,2] = sqrt(2)*sin(tt2)*sin(tt1 + pi/4) + cos(tt2)
	mat[1,0] = (-sin(tt2) + sqrt(2)*sin(tt1 + pi/4)*cos(tt2))*cos(tt3) + sqrt(2)*sin(tt3)*cos(tt1 + pi/4)
	mat[1,1] = (sin(tt2) - sqrt(2)*sin(tt1 + pi/4)*cos(tt2))*sin(tt3) + sqrt(2)*cos(tt3)*cos(tt1 + pi/4)
	mat[1,2] = sqrt(2)*sin(tt2)*sin(tt1 + pi/4) + cos(tt2)
	mat[2,0] = (-sin(tt2) + sqrt(2)*sin(tt1 + pi/4)*cos(tt2))*cos(tt3) + sqrt(2)*sin(tt3)*cos(tt1 + pi/4)
	mat[2,1] = (sin(tt2) - sqrt(2)*sin(tt1 + pi/4)*cos(tt2))*sin(tt3) + sqrt(2)*cos(tt3)*cos(tt1 + pi/4)
	mat[2,2] = sqrt(2)*sin(tt2)*sin(tt1 + pi/4) + cos(tt2)
	return pos, mat