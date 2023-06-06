# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        def dfs(root, currSum):
            if not root:
                return False
            
            currSum += root.val
            if not root.left and not root.right:
                if currSum == targetSum:
                    return True
            
            left = dfs(root.left, currSum)
            right = dfs(root.right, currSum)
            
            return left or right
        
        return dfs(root, 0)
        