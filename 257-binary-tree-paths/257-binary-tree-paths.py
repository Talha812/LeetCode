# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        
        def Dfs(root, String):
            if(root == None):
                return []
            
            if(root.left==None and root.right==None):
                String += str(root.val)
                result.append(String)
                return String
                
            if(root.left):
                Dfs(root.left,String + str(root.val) + "->")
                
            if(root.right):
                Dfs(root.right,String + str(root.val) + "->")
                
        Dfs(root, "")
        return result