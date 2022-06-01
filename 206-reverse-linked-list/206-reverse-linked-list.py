# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        values = []
        temp = answer = head
        
        while(temp):
            values.append(temp.val)
            temp = temp.next
        
        while(head):
            head.val = values.pop()
            head = head.next
        
        return answer
        
#         prev = None
#         curr = head
        
#         while(curr):
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
        
#         return prev

