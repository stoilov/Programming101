def sudoku_solved(sudoku):
	
	# This function checks if a matrix' rows have repeating numbers
	def repeat_check(matrix):
		for row in range(len(matrix)):
			if len(set(matrix[row])) < 9:
				return False
			else:
				return True
	
	# Check if the numbers in the rows of the sudoku are unique.	
	solved = repeat_check(sudoku)
	
	# First the columns are transformed into rows
	columns = []
	for i in range(len(sudoku)):
		columns.append([row[i] for row in sudoku])
	
	# Check if the numbers in the cols of the sudoku are unique.
	solved = repeat_check(columns)
			
	# The 3x3 grids are transformed into rows
	grids = []
	grid = []
	slice_beginning = 0
	slice_end = 3
	for i in list(range(9)) * 3:
		for x in sudoku[i][slice_beginning:slice_end]:
			grid.append(x)
		
		if i in [2, 5, 8]:
			grids.append(grid)
			grid = []
			
		if i == 8:
			slice_beginning += 3
			slice_end += 3
			
	# Check if the numbers in 3x3 grids are unique
	solved = repeat_check(grids)
	
	return solved