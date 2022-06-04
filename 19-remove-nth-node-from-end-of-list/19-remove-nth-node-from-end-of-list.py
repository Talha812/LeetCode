# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head):
            return head
        
        def size(self, head):
            sz = 0
            curr = head
            while(curr):
                sz += 1
                curr = curr.next
            
            return sz
        
        size = size(self, head)
        
        prev = None
        curr = head
        i = 1
        while(i < size-n+1):
            prev = curr
            curr = curr.next
            i += 1
        if prev is None:
            head = head.next
        else:
            prev.next = curr.next
        
        return head