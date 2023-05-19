# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        nums = []
        def inorder(root):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)
        
        inorder(root)
        
        i = 0
        j = len(nums)-1
        
        while i<j:
            summ = nums[i] + nums[j]
            if summ < k:
                i += 1
            elif summ > k:
                j -= 1
            else:
                return True
        
        return False
        
    