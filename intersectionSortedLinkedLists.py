"""
GeeksforGeeks exercise
https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1

Given that two linked lists are sorted in increasing order, create a new linked list representing the intersection of
the two linked lists. The new linked list should be made without changing the original lists.

Note: The elements of the linked list are not necessarily distinct.
"""

class Solution:
    def findIntersection(self,head1,head2):
        # if head1 and head2 are equal, add it to the linked list that will be returned
        if head1.data == head2.data:
            return_node = Node(head1.data)
            # if head1 and head2 are the tails of each linked list, return the current node
            if head1.next is None and head2.next is None:
                return return_node
            # if head1 is not the tail of its linked list, next iteration will use its next node
            new_head1 = head1
            if new_head1.next is not None:
                new_head1 = new_head1.next
            # if head2 is not the tail of its linked list, next iteration will use its next node
            new_head2 = head2
            if new_head2.next is not None:
                new_head2 = new_head2.next
            # iterate function with the new head nodes
            return_node.next = self.findIntersection(new_head1, new_head2)
            return return_node
        # head1 is less than head2
        elif head1.data < head2.data:
            # if head1 is not the tail node of its linked list, iterate the function again with its next node
            if head1.next is not None:
                return self.findIntersection(head1.next, head2)
            return None
        # head2 is less than head1
        elif head1.data > head2.data:
            # if head2 is not the tail node of its linked list, iterate the function again with its next node
            if head2.next is not None:
                return self.findIntersection(head1, head2.next)
            return None


#{
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = input().split()
        input2 = input().split()

        head1, tail1 = None, None
        for item in input1:
            new_node = Node(int(item))
            if not head1:
                head1 = new_node
                tail1 = new_node
            else:
                tail1.next = new_node
                tail1 = new_node

        head2, tail2 = None, None
        for item in input2:
            new_node = Node(int(item))
            if not head2:
                head2 = new_node
                tail2 = new_node
            else:
                tail2.next = new_node
                tail2 = new_node

        ob = Solution()
        result = ob.findIntersection(head1, head2)
        print_list(result)
        print("~")

# } Driver Code Ends