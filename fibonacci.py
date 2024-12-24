"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/is-it-fibonacci--170647/1

Geek just learned about Fibonacci numbers.

    The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    where the next number is found by adding up the two numbers before it.

He defines a new series called Geeky numbers. Here the next number is the sum of the K preceding numbers.
You are given an array of size K, GeekNum[ ], where the ith element of the array represents the ith Geeky number. Return
its Nth term.

Note: This problem can be solved in O(N2) time complexity but the user has to solve this in O(N). The Constraints are
less because there can be integer overflow in the terms.
"""


class Solution():

    def solve(self, N, K, GeekNum):
        # if Nth element of GeekNum has not been found yet
        if len(GeekNum) != N:
            # new value that will be added to GeekNum
            new_value = 0
            # find the sum of the last K elements of GeekNum and then append it as the new element
            for i in range(K):
                new_value += GeekNum[(i + 1) * -1]
            GeekNum.append(new_value)
            # iterate throughout array until Nth element has been found
            return self.solve(N, K, GeekNum)
        # Nth element of GeekNum has been found, return it
        else:
            return GeekNum[-1]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N, K = map(int, input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))

        print("~")

# } Driver Code Ends