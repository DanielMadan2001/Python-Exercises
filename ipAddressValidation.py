"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/1

You are given a string s in the form of an IPv4 Address. Your task is to validate an IPv4 Address, if it is valid return
true otherwise return false.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging
from 0 to 255, separated by dots, e.g., "172.16.254.1"

A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255. Thus, we can write the generalized
form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)

Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.
"""


# User function Template for python3
class Solution:

    # checks substring to see if it conforms to the rules of
    def stringCheck(self, s):
        # invalid if empty
        if s == "":
            return False
        # invalid if substring begins with zero but is not equal to zero
        elif s[0] == "0" and len(s) >= 2:
            return False
        # invalid if substring is not between 0 and 255
        elif int(s) > 255 or int(s) < 0:
            return False
        # otherwise, valid
        return True

    def isValid(self, s):
        # current string that is being added to through iteration, consists of only digits
        current_string = ""
        # number of digit combinations checked (valid IP addresses require 4)
        iterationCount = 1
        # iterates through every character in s
        for i in range(len(s)):
            # if not a period, s[i] is added to current string
            if s[i] != ".":
                current_string += s[i]
            else:
                # checks current string for validity
                if not self.stringCheck(current_string):
                    return False
                else:
                    # resets current string
                    current_string = ""
                    # increases the iteration count by 1
                    iterationCount += 1
        # final substring check and ensuring iteration count is the required amount
        return self.stringCheck(current_string) and iterationCount == 4



# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input("Number of inputs you'd like to enter:\n"))
    for _ in range(0, t):
        s = input("\nInput new IP address:\n")
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends