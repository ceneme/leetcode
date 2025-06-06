# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        tail = result
        carry = 0

        while (l1 or l2 or carry):
            l1_digit = l1.val if l1 is not None else 0
            l2_digit = l2.val if l2 is not None else 0

            column_sum = l1_digit + l2_digit + carry
            newNode = ListNode()

            if (column_sum > 9):
                newNode.val = column_sum % 10
                carry = 1
            else:
                newNode.val = column_sum
                carry = 0

            # iterate
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tail.next = newNode
            tail = tail.next
        
        return result.next