# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checkSymmetry(left_node, right_node):
            
            #if not left_node and not right_node:
            #    return True
            if left_node == None and right_node == None:
                return True
            
            elif left_node == None and  right_node != None:
                return False
            
            elif left_node != None and  right_node == None:
                return False
            else:
                if left_node.val == right_node.val:
                    return checkSymmetry(left_node.left, right_node.right) and checkSymmetry(left_node.right, right_node.left)
                
                else:
                    return False
                
                
        return checkSymmetry(root.left, root.right)