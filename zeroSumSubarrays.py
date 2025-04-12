"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/zero-sum-subarrays1825/1

You are given an array arr[] of integers. Find the total count of subarrays with their sum equal to 0.
"""

class Solution:
    def findSubarray(self, arr):
        # the value that is returned at the end
        return_val = 0
        # the current sum of previously found values
        sum = 0
        # a dictionary of all existing sums
        subarray_sums = {}
        # iterate through all elements of arr
        for i in range(len(arr)):
            # add current element to sum
            sum += arr[i]
            # if sum is 0, then this (and all previous elements) have been 0
            if sum == 0:
                return_val += 1
            # if sum has not already been found, then the current element is not part of sum 0 substring (or is the
            # first element)
            if sum not in subarray_sums:
                # set the number of elements in this new substring to 1
                subarray_sums[sum] = 1
            # if sum has already been found, then this element equalizes a subarray it has been apart of
            else:
                # add the number of prior elements to the returning value, as they are now part of an equal substring
                return_val += subarray_sums[sum]
                # increase the amount of elements in this substring by 1
                subarray_sums[sum] = subarray_sums[sum] + 1
        # return the amount
        return return_val


#{
 # Driver Code Starts
def main():
    t = int(input())  # Number of test cases

    for _ in range(t):
        arr = list(map(int,
                       input().split())
                   )  # Input array as a space-separated list of integers
        solution = Solution()
        print(solution.findSubarray(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends