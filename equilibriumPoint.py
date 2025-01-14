"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1

Given an array arr[] of non-negative numbers. The task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is
the same as the sum of elements after it. Return -1 if no such point exists.
"""


class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # sum of all elements left of the current index (1 by default)
        left_array = arr[0]
        # sum of all elements right of the current index
        right_array = sum(arr[2 : len(arr)])
        # iterate through the elements of arr from the second to second last
        for i in range(1, len(arr) - 1):
            # if equilibrium is found, return current element index
            if left_array == right_array:
                return i
            # add current element to left_array
            left_array += arr[i]
            # add subsequent element to right_array
            right_array -= arr[i + 1]
        # if equilibrium is not found, return -1
        return -1
        # code here


#{
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends