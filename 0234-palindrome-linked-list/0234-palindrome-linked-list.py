# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def findMid(head):
            slow = head
            fast = head
            
            while(fast and fast.next):
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverse(mid):
            prev = None
            curr = mid
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            return prev
        
        mid = findMid(head)
        reverse = reverse(mid)
        
        curr = reverse
        
        while curr:
            if(curr.val != head.val):
                return False
            curr = curr.next
            head = head.next
        
        return True