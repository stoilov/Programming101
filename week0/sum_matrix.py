def sum_matrix(m):
    result = 0
    for row in m:
        for element in row:
            result += element

    return result
