"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/boolean-matrix-problem-1587115620/1

Given a boolean matrix mat[], where each cell contains either 0 or 1, modify it such that if a matrix cell matrix[i][j]
is 1 then all the cells in its ith row and jth column will become 1.
"""


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(mat):
    # dictionaries of x and y indexes, True/False depending on if an item in the row/column is 1
    x_indexes = { }
    y_indexes = { }
    # populate dictionaries with False by default
    for i in range(0, len(mat)):
        x_indexes[i] = False
    for i in range(0, len(mat[0])):
        y_indexes[i] = False
    # iterate through all items in matrix
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            # update x and y indexes using element[i][j] of matrix
            x_indexes[i] = x_indexes[i] or (mat[i][j] == 1)
            y_indexes[j] = y_indexes[j] or (mat[i][j] == 1)
    # iterate through all items in matrix, now with an updated list of indexes
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            # if x or y value of element is True (1 is in row or column), change element to be 1
            if x_indexes[i] == True or y_indexes[j] == True:
                mat[i][j] = 1
    # return updated matrix
    return mat
    # code here


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r = int(input())
        c = int(input())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()

        print("~")

# } Driver Code Ends