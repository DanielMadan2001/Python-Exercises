"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing
order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row
exists, return -1.
"""


class Solution:
    def rowWithMax1s(self, arr):
        # the value representing which row has the earliest 1 element, -1 by default
        return_val = -1
        # the current earliest instance of a 1 element, final element + 1 by default
        current_min = len(arr[0])
        # iterate through all subarrays of arr
        for i in range(len(arr)):
            # value representing column index in which 1 appears in arr[i]
            current_val = -1
            # try to find 1 element in arr[i]
            try:
                # get column index of 1 element
                current_val = arr[i].index(1)
                # if return_val is still default or current column index is smaller than the previous best
                if return_val == -1 or current_val < current_min:
                    # update the earliest column index to be the current
                    current_min = current_val
                    # update the row index in which it was found
                    return_val = i
            # no 1 element in arr[i], does nothing
            except:
                current_val = -1
        # return the row index with the earliest 1 element
        return return_val