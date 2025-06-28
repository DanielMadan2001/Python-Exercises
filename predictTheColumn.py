"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/predict-the-column/1

Given a matrix(2D array) M of size N*N consisting of 0s and 1s only. The task is to find the column with maximum number
of 0s. If more than one column exists, print the one which comes first. If the maximum number of 0s is 0 then return -1.
"""


class Solution:
    def columnWithMaxZeros(self,arr,N):
        # the current highest number of zeroes in a column
        max_num = 0
        # the column index with the highest number of zeroes, -1 by default
        return_val = -1
        # the dictionary which will contain the zero counts for each column
        columns = {}
        # iterate through every subarray in arr
        for i in range(len(arr)):
            # iterate through every element in arr[i]
            for j in range(len(arr[i])):
                # if dictionary element has not been created yet for i, set it as zero
                if j not in columns:
                        columns[j] = 0
                # if arr[i][j] is a zero, increase the zero count for the jth column
                if arr[i][j] == 0:
                    columns[j] += 1
        # iterate N times, which is the number of entries in columns
        for i in range(N):
            # if current dictionary entry is greater than max_num, i is the new top column
            if columns[i] > max_num:
                max_num = columns[i]
                return_val = i
        # return the final value, will be -1 if no column has had a zero in it
        return return_val
