"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1

You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.
"""

class Solution:

    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        # array has only one int value
        if len(arr) == 1:
            # if only number is one, return the next largest positive integer
            if arr[0] == 1:
                return 2
            # otherwise, return the first positive integer
            else:
                return 1
        # sort array in ascending order
        arr.sort()
        # check to ensure that 1 has been found
        one_check = True
        # iterates through array
        for i in range(len(arr) - 1):
            # ignore all array items that are not positive integers
            if arr[i] > 0:
                # for first positive integer of array, check if it is equal to 1
                if one_check:
                    # if not, return 1
                    if arr[i] != 1:
                        return 1
                    # otherwise, set as False to prevent it from being called again
                    else:
                        one_check = False
                # check if next item is not a duplicate of the current one and is exactly 1 higher
                if arr[i + 1] > arr[i] and arr[i + 1] != arr[i] + 1:
                    return arr[i] + 1
        # if 1 has still not been found, check last item of array
        if one_check:
            # if largest item is array is not 1, return 1
            if arr[len(arr) - 1] != 1:
                return 1
        # return final array element + 1
        return arr[len(arr) - 1] + 1


# {
# Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends