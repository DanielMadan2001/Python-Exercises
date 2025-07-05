"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/even-and-odd-elements-at-even-and-odd-positions1342/1

Given an array arr[], the task is to arrange the array such that odd elements occupy the odd positions and even elements
occupy the even positions. The order of elements must remain the same. Consider zero-based indexing. After printing
according to conditions, if remaining, print the remaining elements as it is.
"""


class Solution:
    def arrangeOddAndEven(self, arr):
        # the array that will be populated with sorted elements
        return_arr = []
        # all even elements in arr
        evens = []
        # all odd elements in arr
        odds = []
        # iterate through all elements in arr
        for i in range(len(arr)):
            # if arr[i] is even, add it to the array of even elements
            if arr[i] % 2 == 0:
                evens.append(arr[i])
            # otherwise, add it to the array of odd elements
            else:
                odds.append(arr[i])
        # find which subarray has more elements in it
        iterations = max(len(evens), len(odds))
        # iterate through all elements of larger subarray
        for i in range(iterations):
            # check if evens[i] is an element that exists
            if i < len(evens):
                # add evens[i] to return_arr in an even position (or an odd if evens is larger than odds)
                return_arr.append(evens[i])
            # same process with odds[i]
            if i < len(odds):
                return_arr.append(odds[i])
        # return final sorted array
        return return_arr