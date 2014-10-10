def magic_square(matrix):

	def find_sum_rows(current_matrix, sum_to_get):
		is_equal = False
		for i in range(len(current_matrix)):
			current_sum = 0
			for j in range(len(current_matrix)):
				current_sum += current_matrix[i][j]
			
			if current_sum == sum_to_get:
				is_equal = True
		
		return is_equal
		

	result = True
	sum = 0

	for i in range(len(matrix)):
		sum += matrix[0][i]


	columns = []
	first_diagonal_sum = 0
	second_diagonal_sum = 0

	for i in range(len(matrix)):
		columns.append([row[i] for row in matrix])
		first_diagonal_sum += matrix[i][i]

		for j in reversed(range(len(matrix))):
			second_diagonal_sum += matrix[i][j]

	result = find_sum_rows(matrix, sum) and find_sum_rows(columns, sum)
	if first_diagonal_sum == sum and second_diagonal_sum == sum:
		result = result and True

	return result