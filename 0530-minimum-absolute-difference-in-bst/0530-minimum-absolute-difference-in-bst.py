# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        global diff
        diff = float("inf")
        global prevNodeVal
        prevNodeVal = float("inf")
        def inOrderTraversal(root):
            global diff
            global prevNodeVal
            if root:
                left = inOrderTraversal(root.left)
                    
                if abs(prevNodeVal-root.val) < diff:
                    diff = min(diff, abs(prevNodeVal - root.val))
                    
                prevNodeVal = root.val
                
                right = inOrderTraversal(root.right)
                    
        inOrderTraversal(root)
        
        return diff