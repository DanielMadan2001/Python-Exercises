"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1

You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This
array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return
the missing element.
"""


class Solution:
    def missingNum(self, arr):
        # sort the list so that each element is in ascending order
        arr.sort()
        # iterate through all elements of the list
        for i in range(len(arr)):
            # if current element is not equal to iteration number (+1), then it is the missing element and is returned
            if arr[i] != (i + 1):
                return i + 1
        # all elements are present, return the element that should be next
        return len(arr) + 1


#{
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends