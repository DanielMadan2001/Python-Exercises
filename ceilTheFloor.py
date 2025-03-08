"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1

Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than
smallest element of arr[].
Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than
greatest element of arr[].

Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not
present.
"""


#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        floor = -1
        ceil = -1
        for i in arr:
            if i <= x and i > floor:
                floor = i
            if i >= x and (i < ceil or ceil == -1):
                ceil = i
        return floor, ceil


#{
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends