# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        global maxLength
        maxLength = 0
        # True mean left,    False mean Right
        def dfs(node, step, direction):
            global maxLength
            if node:
                maxLength = max(maxLength, step)
                if direction:
                    dfs(node.right, step+1, False)
                    dfs(node.left, 1, True)
                    
                if not direction:
                    dfs(node.left, step+1, True)
                    dfs(node.right, 1, False)
        
        dfs(root, 0, True)
        
        return maxLength