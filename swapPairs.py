class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def printList(head):
        while head:
            print(head.val, "-> ", end="" if head.next else "None \n")
            head = head.next
    
def swapPairs(head):
    if head == None or head.next == None:
        return head
    
    dummy = ListNode(0, head)
    curr = dummy

    while curr.next and curr.next.next:
        first = curr.next
        second = curr.next.next
        first.next = second.next
        second.next = first
        curr.next = second
        curr = curr.next.next
    return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

ListNode.printList(head)

head = swapPairs(head)
ListNode.printList(head)

