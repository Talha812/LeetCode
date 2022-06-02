# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if(head == None):
            return head
        
        curr = head
        prev = None
        
        while(curr != None):
            if(head.val == val):    #to Check Start values(Head Values)
                head = head.next
                curr = head
                
            elif(curr.val == val):
                prev.next = curr.next
                curr = curr.next
                
            else:
                prev = curr
                curr = curr.next
                
        return head