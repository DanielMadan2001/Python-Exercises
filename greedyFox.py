"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/greedy-fox1555/1

You are given an array of integers arr, where arr[i] represents the denomination of the ith coin placed on a road. The
fox wants to collect coins in a specific pattern: it can only collect a contiguous subarray of coins that are in
strictly increasing order of their denominations. Determine the maximum sum of coins that the fox can collect following
this pattern.
"""


class Solution:
    # Function to find the largest sum of the longest increasing subarray
    def largestSum(self, arr):
        # sum of highest found substring, begins with first value of arr
        return_val = arr[0]
        # current sum of highest substring
        current_val = arr[0]
        # iterate through every element of arr
        for i in range(1, len(arr)):
            # if current element is higher than previous element, add current element to current sum
            if arr[i] > arr[i - 1]:
                current_val += arr[i]
                # if current sum is higher than the highest overall sum, change it
                if current_val > return_val:
                    return_val = current_val
            # otherwise, set new current sum to value of current element
            else:
                current_val = arr[i]
        # return the highest substring sum in arr
        return return_val



#{
 # Driver Code Starts
def main():
    T = int(input())
    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().largestSum(a))
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends