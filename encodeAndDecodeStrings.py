"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/encode-and-decode-strings/1

Given an array of strings s[], you are required to create an algorithm in the encode() function that can convert the
given strings into a single encoded string, which can be transmitted over the network and then decoded back into the
original array of strings. The decoding will happen in the decode() function.

You need to implement two functions:
1. encode(): This takes an array of strings s[] and encodes it into a single string.
2. decode(): This takes the encoded string as input and returns an array of strings containing the original array as
    given in the encode method.

Note: You are not allowed to use any inbuilt serialize method.
"""

class Solution:
    def encode(self, s):
        # string that will be returned after s has been encoded
        return_string = ""
        # iterate through every element in s
        for i in s:
            # add current element to return_string, followed by a "/"
            return_string += i + "/"
        # return encoded string, minus final element
        return return_string[0:-1]

    def decode(self, s):
        # array of strings that will be returned after s has been decoded
        return_array = []
        # current string of elements that will be added to return_array
        current_string = ""
        # iterate through every character in s
        for i in s:
            # if current character is a "/", previous series of characters were their own string prior to encoding
            if i == "/":
                # add new string to array and reset current_string
                return_array.append(current_string)
                current_string = ""
            # current element is not a "/" and the character should be added to the current string
            else:
                current_string += i
        # return decoded array of strings, with current_string being the final element
        return_array.append(current_string)
        return return_array
        # code here


#{
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())  # Number of test cases

    for _ in range(tc):
        input_str = input().split(' ')

        obj = Solution()
        encoded_string = obj.encode(input_str)
        decoded_strings = obj.decode(encoded_string)

        # Printing the decoded strings
        print(" ".join(decoded_strings))
        print("~")

# } Driver Code Ends