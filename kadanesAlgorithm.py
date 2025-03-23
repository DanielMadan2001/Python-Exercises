"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

Given an integer array arr[]. You need to find the maximum sum of a subarray.
"""


class Solution:
    def maxSubArraySum(self, arr):
        return_val = arr[0]
        current_val = arr[0]
        for i in range(1, len(arr)):
            current_val = max(arr[i], current_val + arr[i])
            return_val = max(current_val, return_val)
        return return_val


#{
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends