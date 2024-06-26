# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
#         queue = collections.deque([[root, False]])
#         ans = 0
#         while queue:
#             node, isleft = queue.popleft()
            
#             if isleft:
#                 if not node.left and not node.right:
#                     ans += node.val
            
#             if node.left:
#                 queue.append([node.left, True])
                
#             if node.right:
#                 queue.append([node.right, False])
        
#         return ans
    
    
        stack = [[root, False]]
        ans = 0
        while stack:
            node, isleft = stack.pop()
            
            if isleft:
                if not node.left and not node.right:
                    ans += node.val
            
            if node.right:
                stack.append([node.right, False])
            
            if node.left:
                stack.append([node.left, True])
                
        return ans