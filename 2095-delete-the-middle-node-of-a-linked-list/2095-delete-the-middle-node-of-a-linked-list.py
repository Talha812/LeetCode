# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        count = 0
        while current:
            current = current.next
            count = count + 1
        if count == 1:
            head = head.next
        middle = count//2
        l = 0
        current = head
        while l < middle:
            if l == middle - 1:
                current.next = current.next.next
            l = l + 1
            current = current.next
        return head