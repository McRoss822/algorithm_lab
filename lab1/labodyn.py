
import unittest


def zigzag_traversal(matrix):
    
    m, n = len(matrix), len(matrix[0])
    resulting_list = []
    going_up = True
    count_of_iterations = m + n - 1

    for i in range(count_of_iterations):
        if going_up:
            if i < m:
                row, column = i, 0
            else:
                row, column = m - 1, i - m + 1
            while row >= 0 and column < n:
                resulting_list.append(matrix[row][column])
                row -= 1
                column += 1
        else:
            if i < n:
                row, column = 0, i
            else:
                row, column = i - n + 1, n - 1
            while row < m and column >= 0:
                resulting_list.append(matrix[row][column])
                row += 1
                column -= 1

        going_up = not going_up

    return resulting_list
