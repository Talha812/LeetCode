# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next : 
            return True
        
        def getMidPoint(curr):
            slow = curr
            fast = curr
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverseLinkedList(currN):
            prev = None
            curr = currN
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        mid = getMidPoint(head)
        revHead = reverseLinkedList(mid)
        
        while revHead:
            if revHead.val != head.val:
                return False
            head = head.next
            revHead = revHead.next
        
        return True