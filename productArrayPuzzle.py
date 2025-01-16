"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1

Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in
arr[] except arr[i]. Return this resultant array, res[].
Note: Each element is res[] lies inside the 32-bit integer range.
"""


class Solution:
    def productExceptSelf(self, arr):
        # array of all products found in arr, same length as arr
        res = [1] * len(arr)
        # product value, used in loops to find all leftmost and rightmost products of arr elements
        product = 1
        # iterate through arr (from first to last element)
        for i in range(len(arr)):
            # multiply current res element by the current product (which is the product of all leftmost values)
            res[i] *= product
            # update product to be the product of itself and current arr element
            product *= arr[i]
        # reset product before new loop starts
        product = 1
        # iterate through arr (from last to first element)
        for i in range(len(arr) - 1, -1, -1):
            # multiply current res element by the current product (which is the product of all rightmost values)
            res[i] *= product
            # update product to be the product of itself and current arr element
            product *= arr[i]
        # return res
        return res


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends