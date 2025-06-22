"""
CodeSignal exercise
https://app.codesignal.com/practice-question/question/freeCoding?context=otherTypes

We can render an ASCII art pyramid with N levels by printing N rows of asterisks, where the top row has a single
asterisk in the center and each successive row has two additional asterisks on either side.

Here's what that looks like when N is equal to 3.

  *
 ***
*****

And here's what it looks like when N is equal to 5.

    *
   ***
  *****
 *******
*********

Can you write a program that generates this pyramid with an N value of 10?
"""


def solution(n):
    # the array that will be populated with strings that represent pyramid rows
    return_arr = []
    # get the length of each row of the pyramid
    row_length = ((n - 1) ** 2) + 1
    # iterate n times
    for i in range(n):
        # the new row that will be populated by spaces and asterisks
        new_row = ""
        # iterate row_length times to find each element of the row
        for j in range(row_length):
            # calculate the distance between j and the center of the current row
            center_dist = abs(n - (j + 1))
            # if center_dist is less than the row index, it is within range to be an asterisk
            if center_dist <= i:
                new_row += "*"
            # otherwise, it is outside and is a space
            else:
                new_row += " "
        # add new_arr as the ith element of return_arr
        return_arr.append(new_row)
    # return return_arr to be printed
    return return_arr

if __name__ == "__main__":
    n = 10
    pyramid = solution(n)
    for i in range(len(pyramid)):
        print(pyramid[i])