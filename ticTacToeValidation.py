"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/tic-tac-toe2412/1

A Tic-Tac-Toe board of size 3X3 is given after all the moves are played, i.e., all nine spots are filled. Find out if
the given board is valid, i.e., is it possible to reach this board position after a set of moves or not.

Note that every arbitrarily filled grid of 9 spaces isn’t valid, e.g., a grid filled with 3 X and 6 O isn’t a valid
situation because each player needs to take alternate turns.

Note: The game starts with X
"""

class Solution:

    def isValid(self, board):
        # number of spaces with x
        x_count = 0
        # number of spaces with o
        o_count = 0
        # if a winning path appears
        wins = 0
        for i in range(len(board)):
            # checks if a winning path can be found using the current space
            can_win = False
            # check for vertical win
            can_win = can_win or (board[i % 3] == board[i] and board[(i % 3) + 3] == board[i] and board[(i % 3) + 6] == board[i])
            # check for horizontal win
            can_win = can_win or (board[(i // 3) * 3] == board[i] and board[(i // 3) * 3 + 1] == board[i] and board[(i // 3) * 3 + 2] == board[i])
            # check for diagonal win (NW - SE)
            if i in [0, 4, 8]:
                can_win = can_win or (board[0] == board[i] and board[4] == board[i] and board[8] == board[i])
            # check for diagonal win (NE - SW)
            if i in [2, 4, 6]:
                can_win = can_win or (board[2] == board[i] and board[4] == board[i] and board[6] == board[i])
            # if a winning path is found, add to the total (invalid if more than 1 exists)
            if can_win:
                wins += 1
            # checks if current space is X or O
            if board[i] == 'X':
                # adds to the count of x/o value (used to ensure there are 5 x's and 4 o's)
                x_count += 1
            else:
                o_count += 1
        # return true if sum of spaces equals 9, there is one more x than o and only one of x and o can win
        if x_count + o_count == 9 and x_count - o_count == 1 and wins <= 3:
            return True
        # otherwise, return false
        else:
            return False

#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        board = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.isValid(board)
        if ans:
            print("Valid")
        else:
            print("Invalid")
        tc -= 1

        print("~")
# } Driver Code Ends