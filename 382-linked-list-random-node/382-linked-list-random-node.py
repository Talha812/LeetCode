# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.values = []
        curr = head
        while(curr):
            self.values.append(curr.val)
            curr = curr.next

    def getRandom(self) -> int:
        return self.values[randint(0,len(self.values)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()