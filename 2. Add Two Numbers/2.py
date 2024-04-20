# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], 
                            l2: Optional[ListNode]) -> Optional[ListNode]:
        # Took inspiration from a digital logic lab class I took in college
        # in which we implemented a logic gate adder/half-adder using the
        # "carry" concept, which is also used in the std algorithm we use for
        # adding two numbers with a pen & paper

        # Time complexity here seems to be O(n), since we're iterating once
        # through all lists simultaneously, n being the size of the largest
        # list -----------------------------------------------------------

        # we define a sentinel 'pre-node' as to facilitate the loop below
        sentinel = ListNode()
        tail = sentinel         # 'iterator'
        carry = 0               # instantiate carry for first loop run check

        # will run while at least one of l1, l2 or carry are not None/zero
        while (l1 or l2 or carry):
            l1_digit = l1.val if l1 is not None else 0
            l2_digit = l2.val if l2 is not None else 0

            # we add all elements from the current 'column',
            # as we do with a pen & paper
            column_sum = l1_digit + l2_digit + carry
            new_digit = column_sum % 10         # this goes to the new list
            carry = 1 if column_sum > 9 else 0  # carries over to next iter

            # create a new node with info above
            newNode = ListNode(new_digit)

            # append new node to the end of the list
            tail.next = newNode

            # move everything to the next node before looping
            tail = tail.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return sentinel.next
