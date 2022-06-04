# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head):
            return head
        
        def reverse(self, head):
            prev = None
            curr = head
            
            while(curr):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        reversed_LL = reverse(self, head)
        
        
        i = 1
        prev_rev = None
        curr_rev = reversed_LL
        #print(curr_rev)
        while(curr_rev and i != n):
            prev_rev = curr_rev
            curr_rev = curr_rev.next
            i += 1

        if prev_rev is None:
            reversed_LL = reversed_LL.next
        else:
            prev_rev.next = curr_rev.next
        
        again_retrieve_order = reverse(self, reversed_LL)
        
        return again_retrieve_order