"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/minimum-sum4058/1

Given an array arr[] such that each element is in the range [0 - 9], find the minimum possible sum of two numbers formed
using the elements of the array. All digits in the given array must be used to form the two numbers. Return a string
without leading zeroes.
"""

class Solution:

    def minSum(self, arr):
        # if length of array is 0, return 0
        if len(arr) == 0:
            return 0
        # if length of array is 1, return first element
        elif len(arr) == 1:
            return int(arr[0])

        # two strings that elements from arr will be added to
        str1 = ""
        str2 = ""
        # sort arr so integer values appear in ascending order
        arr.sort()
        # go through all elements of arr
        for i in range(len(arr)):
            # for even numbered elements, turn them into strings and add their value to str1
            if (i % 2) == 0:
                str1 += str(arr[i])
            # same process for odd numbered elements
            else:
                str2 += str(arr[i])
        # convert strings into integers
        return_int1 = int(str1)
        return_int2 = int(str2)
        # return the sum of both integers
        return return_int1 + return_int2


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends