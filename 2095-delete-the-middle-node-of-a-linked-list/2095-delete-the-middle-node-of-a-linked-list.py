# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(head.next == None):
            return None
        
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        prev = None
        curr = head
        while curr:
            if(mid == curr):
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        
        return head