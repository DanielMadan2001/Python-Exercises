"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1

Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the
matrix or not.
Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row
(i!=0) is greater than the last element of the (i-1)th row.
"""


# User function Template for python3

class Solution:

    # Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x):
        # search all rows
        for i in mat:
            # search each element in row i
            for j in i:
                # if j element of row i equals x, return True
                if j == x:
                    return True
        # element has not been found, return False
        return False


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends