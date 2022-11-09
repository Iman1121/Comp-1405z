import math


def mult_scalar(matrix, scale):
	new_list = []
	for x in matrix:
		column = []
		for y in x:
			column.append(y*scale)
		new_list.append(column)
	return new_list

def mult_matrix(a, b):
	new_list = []
	for x in a:
		column = []
		for y in b[0]:
			column.append(0)
		new_list.append(column)	
	for idx_x,x in enumerate(a):
		for idx_y,y in enumerate(b[0]):
			for idx_z,z in enumerate(b):				
				new_list[idx_x][idx_y] += a[idx_x][idx_z] * b[idx_z][idx_y] 

	return new_list

	
def euclidean_dist(a,b):
	answer = 0
	if(len(a[0]) != len(b[0])):
		return None
	for idx_x,x in enumerate(a[0]):
		value = (x-b[0][idx_x]) ** 2
		answer += value
	return math.sqrt(answer)

