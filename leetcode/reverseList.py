class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        while head:
            print(f"{head.val} --> ", end="")
            head = head.next

    def reverseList(self, head):
        if head.next == None:
            return head
        new = head
        if head.next:
            new = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return new
    
    
    def reverseInPlace(self, head):
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        #slow = self.reverseList(slow.next)
        slow = self.reverseInPlace(slow.next)
        print(self.printList(slow))
        while slow:
            print(f"slow: {slow.val}, head: {head.val}")
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
    
head = ListNode(1, ListNode(0, ListNode(3, ListNode(4, ListNode(0, ListNode(1))))))
s = Solution()
print(s.printList(head))
print(s.isPalindrome(head))