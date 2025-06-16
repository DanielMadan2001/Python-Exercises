"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/first-come-first-serve1328/1

You are given an array arr[], containing the IDs of users in chronological order of their occurrences. Find the first
user who has exactly k occurrences.

If no such user exists, return -1.
"""


class Solution:
    def firstElement(self, arr, k):
        # dictionary where all data collected from arr will be kept
        dic = {}
        # iterate through every element in arr
        for i in arr:
            # if current element has not been found yet, create dictionary element
            if i not in dic:
                dic[i] = 1
            # otherwise, find existing dictionary element and increase its value by 1
            else:
                dic[i] += 1
        # iterate through every element in dic
        for i in dic:
            # if current element has a value equal to k, return it
            if dic[i] == k:
                return i
        # no elements appear exactly k times, return -1
        return -1