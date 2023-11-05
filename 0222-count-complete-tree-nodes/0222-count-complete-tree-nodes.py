# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        
        if left_height == right_height:
            # If the left and right subtrees have the same height,
            # the left subtree is a perfect binary tree with 2^left_height - 1 nodes.
            # Add the root node, and the right subtree nodes recursively.
            return 2**left_height + self.countNodes(root.right)
        else:
            # If the heights are different, the right subtree is a perfect binary tree with 2^right_height - 1 nodes.
            # Add the root node, and the left subtree nodes recursively.
            return 2**right_height + self.countNodes(root.left)