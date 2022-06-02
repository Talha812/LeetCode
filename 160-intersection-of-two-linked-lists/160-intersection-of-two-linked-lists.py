# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodes_addresses = set()
        h1 = headA
        while h1:
            nodes_addresses.add(h1)
            h1 = h1.next
            
        #print(nodes_addresses)
        
        h2 = headB
        while h2:
            if h2 in nodes_addresses:
                return h2
            h2 = h2.next
            
        return None