def matrix_bombing_plan(m):
	result = {}

	indexes = []
	for index1, row in enumerate(m):
		for index2, element in enumerate(row):
			neighbours = 8
			indexes.append((index1, index2))
			if index1 - 1 != 0 and type(row[index1 - 1]) == "int":
				if row[index1 - 1] >= element:
					row[index1 - 1] = 0
				else:
					row[index1 - 1] -= element


print(matrix_bombing_plan([[1,2,3], [4,5,6], [7,8,9]]))