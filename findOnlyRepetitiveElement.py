"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/find-repetitive-element-from-1-to-n-1/1

Given an array arr[] of size n, filled with numbers from 1 to n-1 in random order. The array has only one repetitive
element. Your task is to find the repetitive element.

Note: It is guaranteed that there is a repeating element present in the array.
"""


class Solution:
    def findDuplicate(self, arr):
        # sort arr to be in ascending order
        arr.sort()
        # iterate through each element in arr
        for i in range(len(arr) - 1):
            # if current element is the same as its successor, one is the repetitive element and is returned
            if arr[i] == arr[i + 1]:
                return arr[i]
        return 0
        #code here