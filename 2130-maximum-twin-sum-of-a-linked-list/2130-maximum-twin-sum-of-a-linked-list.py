# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        array = []
        curr = head
        while(curr):
            array.append(curr.val)
            curr= curr.next
        
        max_twin_sum = -1
        
        for i in range(len(array)//2):
            twin_sum = array[i]+array[len(array)-1-i]
            max_twin_sum = max(max_twin_sum, twin_sum)
        
        return max_twin_sum