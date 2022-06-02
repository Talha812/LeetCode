# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sort_LL = None
        curr = head
        while(curr):
            temp = curr.next
            prev = None
            dummy = sort_LL
            
            if(dummy == None):
                sort_LL = curr
                sort_LL.next = None
            
            else:
                while(dummy != None and curr != None and dummy.val < curr.val):
                    prev = dummy
                    dummy = dummy.next
                if(prev is None):
                    curr.next = sort_LL
                    sort_LL = curr
                else:
                    prev.next = curr
                    curr.next = dummy
            
            curr = temp
            
        return sort_LL