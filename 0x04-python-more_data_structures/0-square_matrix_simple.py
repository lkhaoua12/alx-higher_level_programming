#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[i ** 2 for i in row] for row in matrix]
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
