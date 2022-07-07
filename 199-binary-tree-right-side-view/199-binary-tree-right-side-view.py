# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        q = collections.deque([root])
        
        while(q):
            rightSide = None
            
            for i in range(len(q)):
                node = q.popleft()
                if(node):
                    rightSide = node
                    if(node.left):
                        q.append(node.left)
                    if(node.right):
                        q.append(node.right)
                
            if(rightSide):
                ans.append(rightSide.val)
        
        return ans