"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1

You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0, all the
elements in the i-th row and j-th column are set to 0 and do it in constant space complexity.
"""


# User function Template for python3

class Solution:

    def setMatrixZeroes(self, mat):
        # lists that will contain the indexes of rows and columns that contain a 0
        changed_rows = []
        changed_columns = []
        # iterate through all rows of mat
        for i in range(len(mat)):
            # iterate through all columns of row i
            for j in range(len(mat[i])):
                # if the jth element of row i is 0, add i to row list and j to column list
                if mat[i][j] == 0:
                    changed_rows.append(i)
                    changed_columns.append(j)
        # iterate through all elements in mat
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                # if row or column appears in change lists, change current element to 0
                if (i in changed_rows) or (j in changed_columns):
                    mat[i][j] = 0
        # returned changed mat
        return mat


# {
# Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends