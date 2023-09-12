"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copied = {None : None}
        
        curr = head
        
        while curr:
            copy = Node(curr.val)
            copied[curr] = copy
            curr = curr.next
    
        
        curr = head
        
        while curr:
            node = copied[curr]
            node.next = copied[curr.next]
            node.random = copied[curr.random]
            curr = curr.next
            
        
        return copied[head]