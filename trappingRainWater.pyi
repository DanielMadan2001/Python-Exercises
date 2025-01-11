"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1

Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1,
compute how much water can be trapped between the blocks during the rainy season.
"""


class Solution:
    def maxWater(self, arr):
        # sum of all water that can fit in blocks of arr
        return_val = 0
        for i in range(1, len(arr) - 1):
            # find the largest element to the left of arr[i]
            left_bound = max(arr[0: i])
            # find the largest element to the right of arr[i]
            right_bound = max(arr[i + 1: len(arr)])
            # if the current element is greater than both bounds, it would not have water in it
            if arr[i] > left_bound or arr[i] > right_bound:
                continue
            # if the left bound is smaller than the right, then that is the maximum amount of water that can exist in
            # that area. add it to return_val while subtracting the amount of blocks that are at the bottom
            elif left_bound < right_bound:
                return_val += left_bound - arr[i]
            # same as before, but using the right bound to determine maximum water capacity
            else:
                return_val += right_bound - arr[i]
        # return sum of water
        return return_val


import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends