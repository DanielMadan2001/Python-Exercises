"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/decode-the-pattern1138/1

Given an integer n. Return the nth row of the following look-and-say pattern.
    1
    11
    21
    1211
    111221

Look-and-Say Pattern:
To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the
number of digits in groups of the same digit. For example:

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    1211 is read off as "one 1, one 2, then two 1s" or 111221.
    111221 is read off as "three 1s, two 2s, then one 1" or 312211.
"""


class Solution:
    def countAndSay(self, n):
        # the current array being iterated through, [1] by default
        current_array = [1]
        # iterate n - 1 times
        for i in range(1, n):
            # the current value being compared to each future element, starts with the first element
            val = current_array[0]
            # the current number of duplicates of val that have been found
            val_duplicates = 1
            # the new array that will replace the contents of current_array
            new_array = []
            # iterate through all elements in current_array
            for j in range(1, len(current_array)):
                # if this element is a duplicate of the elements preceding it
                if val != current_array[j]:
                    # add the number of duplicates to the new_array, followed by the value that was duplicated
                    new_array.append(val_duplicates)
                    new_array.append(val)
                    # change the new variable to be the value of the current element
                    val = current_array[j]
                    # reset the duplicates to 0
                    val_duplicates = 0
                # increase the duplicates count by 1
                val_duplicates += 1
            # for the final element(s), add the current duplicate and values to new_array
            new_array.append(val_duplicates)
            new_array.append(val)
            # update current_array with new_array's elements
            current_array = new_array
        # convert current_array to string and return it
        return_string = ""
        for i in current_array:
            return_string += str(i)
        return return_string


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends