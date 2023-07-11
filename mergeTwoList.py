"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        if not list1:
            return list2
        elif not list2:
            return list1
        if not list1 and not list2:
            return 
        merged = ListNode(None)
        current = merged # current is used to traverse linked list
    
        while list1 and list2:
            # list1 : 1 -> 2 -> 4
            # list2 : 1 -> 3 -> 4
            # val1=1, val2=1
            val1 = list1.val
            val2 = list2.val
            if val1 != None or val2 != None:
                #print("val1: ", val1)
                #print("val2: ", val2)
                if val1 <= val2:
                    current.next = list1 # add val1
                    list1 = list1.next # move to next node
                else:
                    current.next = list2
                    list2 = list2.next
            current = current.next
            current.next = list1 or list2
        return merged.next # skip the first node


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print("list1: ", [list1.val, list1.next.val, list1.next.next.val])
print("list2: ", [list2.val, list2.next.val, list2.next.next.val])

merged = Solution().mergeTwoLists(list1, list2)

merged_list = []
while merged is not None:
    merged_list.append(merged.val)
    merged = merged.next
print("Merged List: ", merged_list)