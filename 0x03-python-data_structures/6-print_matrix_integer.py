#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints the matrix of an integer"""
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" ")
        print()
