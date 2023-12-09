# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        global ans
        ans = ""
        def preorder(root):
            global ans
            if root:
                ans += str(root.val)
                if not root.left and not root.right:
                    ans += ""
                
                if root.left:
                    ans += "("
                    preorder(root.left)
                    ans += ")"
                    
                if not root.left and root.right:
                    ans += "()"
                
                if root.right:
                    ans += "("
                    preorder(root.right)
                    ans += ")"

        preorder(root)
        return ans
                    