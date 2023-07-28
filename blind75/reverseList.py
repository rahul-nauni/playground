from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    new = head
    if head.next:
        new = reverseListRecursive(head.next)
        head.next.next = head
    head.next = None
    return new

def printList(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    printList(head)
    #printList(reverseList(head))
    printList(reverseListRecursive(head))

if __name__ == "__main__":
    main()
        
