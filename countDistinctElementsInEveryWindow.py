"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1

Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.
"""


class Solution:
    def countDistinct(self, arr, k):
        # the array that will return the number of unique elements for every k elements in arr
        return_array = []
        # iterate through arr until every k window is checked
        for i in range(0, len(arr) - k + 1):
            # create an array of elements in arr between i and i + k
            current_array = arr[i : i + k]
            # use the set() function to eliminate duplicate elements
            unique_elements = set(current_array)
            # add the length of the array (number of unique elements) to the return array
            return_array.append(len(unique_elements))
        # return the return_array
        return return_array


#{
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends