from collections import defaultdict
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        while head != None:
            print(head.val, "-> ", end="" if head.next != None else "None \n")
            head = head.next

    def deleteDups(self, head):
        if head == None or head.next == None:
            return head
        
        dups = defaultdict(int)
        # 2 or more nodes
        curr = head
        while curr:
            dups[curr.val] += 1
            curr = curr.next
        
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            if dups[curr.next.val] < 2:
                curr = curr.next
            else:
                while curr.next and dups[curr.next.val] >= 2:
                    curr.next = curr.next.next
        return dummy.next
    
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(4)


s = Solution()
s.printList(head)
head = s.deleteDups(head)
s.printList(head)


