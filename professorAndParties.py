"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/professor-and-parties2000/1

A professor attended a party and classified it into two categories based on the colors of the robes. If all party
members are wearing different colored robes, represented by positive integers in the array arr[], then it is a girl's
only party. If there is at least one duplicate color, it is a boy's party. Determine the type of party by returning
“true” if it’s a boy’s party, otherwise, return “false”.
"""


# User function Template for python3

class Solution:

    def PartyType(self, arr):
        # make array of found integers
        repeats = []
        # go through all elements in arr
        for i in arr:
            # if i has already been found, return true
            if i in repeats:
                return "true"
            # otherwise, add it to the list of found integers
            else:
                repeats.append(i)
        # no elements in arr were repeats, return false
        return "false"


# {
# Driver Code Starts.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.PartyType(arr)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends