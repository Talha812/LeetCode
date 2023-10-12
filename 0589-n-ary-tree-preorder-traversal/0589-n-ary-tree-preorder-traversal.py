"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        global ans
        ans = []
        
        def Preorder_Traversal(root):
            global ans
            if root:
                ans.append(root.val)
                for neighbor in root.children:
                    Preorder_Traversal(neighbor)
        
        Preorder_Traversal(root)
        return ans