"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/equal-to-product3836/1

Given an array, arr[] of distinct elements, and a number x, find if there is a pair in arr[] with a product equal to x.
Return true if there exists such pair otherwise false.
"""


class Solution:
    def isProduct(self, arr, x):
        # dictionary that will be progressively populated with elements from arr
        existing_elements = {}
        # iterate through all elements in arr
        for i in range(len(arr)):
            # if current element is zero, avoid following checks as zero cannot be divided
            if arr[i] == 0:
                if x == 0:
                    return True
            # if the product of x and an element in existing_elements creates x, return True
            elif (x / arr[i]) in existing_elements:
                return True
            # add element to existing_elements so it can be searched later
            else:
                existing_elements[arr[i]] = ""
        # no products found, return False
        return False