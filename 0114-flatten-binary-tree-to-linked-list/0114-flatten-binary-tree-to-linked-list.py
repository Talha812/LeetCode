# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def helper(root):
            if root:
                
                temp = root.right
                root.right = root.left
                root.left = None
                
                node = root
                while node.right:
                    node = node.right
                    
                node.right = temp
                
                helper(root.right)
            
        if not root:
            return
        
        helper(root)