"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        q = collections.deque([root])
        height = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                
                for child in node.children:
                    q.append(child)
            
            height += 1
    
        return height
    