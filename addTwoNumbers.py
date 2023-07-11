# Problem: Add Two Numbers
"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        output = ListNode()
        current = output # current is used to traverse linked list
        carry = 0

        while l1 is not None or l2 is not None or carry != 0 :
            l1_val = l1.val if l1 else 0 # if l1 is exhausted, set l1_val to 0
            l2_val = l2.val if l2 else 0 # if l2 is exhausted, set l2_val to 0
            sum = l1_val + l2_val + carry
            current.next = ListNode(sum % 10)
            carry = (l1_val + l2_val + carry) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return output.next
    

l1 = ListNode(2)
l1.next = ListNode(4)


l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

output = Solution().addTwoNumbers(l1, l2)
print([output.val, output.next.val, output.next.next.val])