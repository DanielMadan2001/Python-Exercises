"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1

Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the
subsequence are consecutive integers, the consecutive numbers can be in any order.
"""


# User function Template for python3

class Solution:

    # arr[] : the input array

    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        # sort arr so elements are in ascending order
        arr.sort()
        # value that is highest consecutive substring value
        return_val = 1
        # current consecutive substring value
        current_val = 1
        # iterate through arr, starting with second element
        for i in range(1, len(arr)):
            # if current element is identical to previous element, ignore
            if arr[i] == arr[i - 1]:
                pass
            # if current element is exactly one higher than previous element, increase the current value
            elif (arr[i] - 1) == arr[i - 1]:
                current_val += 1
                # if current value is higher than the record, replace it
                if current_val > return_val:
                    return_val = current_val
            # if current and previous elements are not consecutive, reset current value
            else:
                current_val = 1
        # return highest consecutive substring value
        return return_val


# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends