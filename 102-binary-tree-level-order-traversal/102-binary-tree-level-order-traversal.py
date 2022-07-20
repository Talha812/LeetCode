# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if(root == None):
            return []
        
        result = []
        
        q = collections.deque()
        q.append(root)
        
        while(q):
            temp = []
            size = len(q)
            for i in range(size):
                node = q[0]
                temp.append(node.val)
                q.popleft()
                
                if(node.left):
                    q.append(node.left)
                    
                if(node.right):
                    q.append(node.right)
                
                
            
            result.append(temp)
            
        return result