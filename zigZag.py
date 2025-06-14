"""
CodeSignal exercise
https://app.codesignal.com/practice-question/question/gcfSingleFunction

Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a
zigzag. More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the
output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.
"""


def solution(numbers):
    # array that will be populated with 0s and 1s
    return_arr = []
    # iterate through the second to second-last elements in numbers
    for i in range(1, len(numbers) - 1):
        # if left and right elements of numbers[i] are larger than it, add 1 to return_arr
        if (numbers[i - 1] < numbers[i]) and (numbers[i + 1] < numbers[i]):
            return_arr.append(1)
        # if left and right elements of numbers[i] are smaller than it, add 1 to return_arr
        elif (numbers[i - 1] > numbers[i]) and (numbers[i + 1] > numbers[i]):
            return_arr.append(1)
        # otherwise, add 1 to return_arr
        else:
            return_arr.append(0)
    # return the finalized return_arr
    return return_arr