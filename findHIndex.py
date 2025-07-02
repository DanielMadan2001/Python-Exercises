"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/find-h-index--165609/1

Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith
paper. The task is to find the H-index.

H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times.
"""


class Solution:
    def hIndex(self, citations):
        # the value representing the H-Index
        return_val = 0
        # sort citations in ascending order
        citations.sort()
        # dictionary to keep track of what elements of citations have already been found
        dic = {}
        # iterate through all elements in citations
        for i in range(len(citations)):
            # skip all zeroes
            if citations[i] == 0:
                continue
            # get number of elements remaining after citations[i]
            remaining = len(citations) - i
            # if current element has not been found yet
            if citations[i] not in dic:
                # add current element to dictionary for future reference
                dic[citations[i]] = 0
                # if current element is not higher than remaining elements (at least H papers that have been cited at
                # least H times)
                if citations[i] <= remaining:
                    # H-Index will be changed if current element is higher than existing H-Index
                    return_val = max(return_val, citations[i])
            # if the remaining elements are not less than the current element, there are remaining elements higher than
            # citations[i]
            if remaining <= citations[i]:
                # H-Index will be changed if current element is higher than existing H-Index
                return_val = max(return_val, remaining)
        # return H-Index
        return return_val