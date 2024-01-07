# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        rec = []
        
        queue = collections.deque([[root, None, 0]])
        
        while queue:
            node, parent, depth = queue.popleft()
            
            if node.val == x:
                rec.append((parent, depth))
                
            if node.val == y:
                rec.append((parent, depth))

            if node.left:
                queue.append([node.left, node.val, depth + 1])
            
            if node.right:
                queue.append([node.right, node.val, depth + 1])

        if rec[0][1] == rec[1][1] and rec[0][0] != rec[1][0]:
            return True
        
        return False