def matrix_bombing_plan(m):
	result = {}

	indexes = []
	neigbours = 8
	def check_neighbours(m, j, k, neigbours):
		if i - 1 < 0 or i + 2 > len(m):
			if y - 1 < 0 or i + 2 > len(m):
				neigbours -= 5
			else:
				neigbours -= 3
		else:
			if y - 1 < 0 or i + 2 > len(m):
				neigbours -= 3

	def bomb_matrix(m):
		for i, row in enumerate(m):
			for j, element in enumerate(row):




print(matrix_bombing_plan([[1,2,3], [4,5,6], [7,8,9]]))