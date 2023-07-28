from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new = head
        if head.next:
            new = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return new

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new = self.reverseList(head)
        print(f"Reversed List: {self.printList(new)}")
        dummy1, dummy2 = head, new
        while dummy1 and dummy2:
            print(dummy1.val, dummy2.val)
            if dummy1.val != dummy2.val:
                return False
            dummy1, dummy2 = dummy1.next, dummy2.next
        return True
    
head = ListNode(1, ListNode(1, ListNode(2, ListNode(1))))
s = Solution()
print(s.isPalindrome(head))