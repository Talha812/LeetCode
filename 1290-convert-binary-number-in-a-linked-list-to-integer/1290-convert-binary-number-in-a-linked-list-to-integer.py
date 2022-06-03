# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        if not head:
            return 0
        
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
        #print(reversed_LL)
        power = 0
        ans = 0
        curr = reversed_LL
        
        while(curr):
            ans += curr.val * (2**power)
            power += 1
            curr = curr.next
            
        return ans