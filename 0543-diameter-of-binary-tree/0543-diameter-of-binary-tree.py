# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        diameter = 0
        
        def getDiameter(root):
            global diameter
            if not root:
                return 0
            left =getDiameter(root.left)
            right = getDiameter(root.right)
            if left + right > diameter:
                diameter = left + right
                
            return 1 + max(left, right)
        
        if not root:
            return 0
        
        getDiameter(root)
        
        return diameter