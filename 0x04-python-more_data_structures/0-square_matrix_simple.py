#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	rows = len(matrix)
	colums = len(matrix[0])
	new_matrix = [[value ** 2 for value in row] for row in matrix]
	for no_in_row in range(rows):
		for no_in_colums in range(colums):
			new_matrix[no_in_row][no_in_colums] = matrix[no_in_row][no_in_colums] ** 2
		return new_matrix
