"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/pascal-triangle0652/1

Given a positive integer n, return the nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
"""


#User function Template for python3
class Solution:

    def nthRowOfPascalTriangle(self,n):
        # previous line in triangle (1st line by default)
        old_arr = [1]
        # current line in triangle
        new_arr = [1]
        # correct line has been found when its length is equal to n
        while len(new_arr) < n:
            # current line always begins with 1, so it is added automatically
            new_arr = [1]
            # for every element between the first and last, add the ith and (i-1)th elements from previous line
            for i in range(1, len(old_arr)):
                new_arr.append(old_arr[i - 1] + old_arr[i])
            # current line always ends with 1
            new_arr.append(1)
            # set previous line to current line in case of next iteration
            old_arr = new_arr
        # return current line
        return new_arr


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
        print("~")
# } Driver Code Ends