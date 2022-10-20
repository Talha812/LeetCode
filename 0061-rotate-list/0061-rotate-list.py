# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
                
        if not head or not head.next:
            return head
    
        cur = head
        num = 1
        while cur.next:
            num += 1  
            cur = cur.next
        cur.next = head
        
        index = num - (k % num)    #index of new head
        # if index == 0:
        #     return head
        i = 0
        cur = head

        while i < index:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = None
        head = cur
        
        return head