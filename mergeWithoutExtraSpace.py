"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without
using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m
elements.
"""


class Solution:
    def mergeArrays(self, a, b):
        # get n and m values
        n = len(a)
        m = len(b)
        # create a merged array of a and b called c
        c = a + b
        # sort c so it is in ascending order
        c.sort()
        # for the first n elements c, replace the ith element of a[i] with c[i]
        for i in range(n):
            a[i] = c[i]
        # for the remaining elements, replace the ith element of b[i] with c[n + i]
        for i in range(m):
            b[i] = c[n + i]