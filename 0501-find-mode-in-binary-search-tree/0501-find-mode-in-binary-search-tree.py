# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        dic = {}
        def preOrderTraversal(root):
            if root:
                if root.val in dic:
                    dic[root.val] += 1
                else:
                    dic[root.val] = 1
                    
                preOrderTraversal(root.left)
                preOrderTraversal(root.right)
        
        preOrderTraversal(root)
        
        mode = max(dic.values())
        
        ans = []
        for k, v in dic.items():
            if v == mode:
                ans.append(k)
        
        return ans
        