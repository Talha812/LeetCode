# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def findDepth(self, root):
            if(root==None):
                return 0
            return max(findDepth(self, root.left)+1, findDepth(self, root.right)+1)
        
        
        maxDepth = findDepth(self, root)
        print(maxDepth)
        
        global add
        add = 0
        def calculateSum(self, root, currDepth, maxDepth):
            if(root!=None):
                if(currDepth == maxDepth):
                    global add
                    add = add + root.val
                calculateSum(self, root.left, currDepth+1, maxDepth)
                calculateSum(self, root.right, currDepth+1, maxDepth)
                
        calculateSum(self, root, 1, maxDepth)
                        
        return add 
                            
                    