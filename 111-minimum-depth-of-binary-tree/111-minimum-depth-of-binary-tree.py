# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if(root == None):
            return 0
        
        
        q = collections.deque()
        
        q.append(root)
        level = 1
        
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                
                if(node.left == None and node.right == None):
                    return level
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            
            level += 1
        
        return level
        
        
        """
        if not root:
            return 0
        
        # q = [(root,1)]
        
        q = collections.deque()
        q.append((root,1))
        
        while q:
            # node,depth = q.pop(0)
            node,depth = q.popleft()
            
            if not node.left and not node.right:
                return depth
            
            if node.left:
                q.append((node.left , depth+1))
            
            if node.right:
                q.append((node.right , depth+1))
                

"""