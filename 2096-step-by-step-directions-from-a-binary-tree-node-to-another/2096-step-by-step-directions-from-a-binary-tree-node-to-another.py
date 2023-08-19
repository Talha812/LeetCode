# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        adj_List = defaultdict(list)
        
        queue = collections.deque([root])
        
        
        while queue:
            node = queue.popleft()
            
            if node.left:
                adj_List[node.val].append((node.left.val, "L"))
                adj_List[node.left.val].append((node.val, "U"))
                queue.append(node.left)
                
            if node.right:
                adj_List[node.val].append((node.right.val,"R"))
                adj_List[node.right.val].append((node.val,"U"))
                queue.append(node.right)
        
        
        queue = collections.deque()
        visited = set()
        
        queue.append((startValue, ""))
        
        while queue:
            
            nextt, path = queue.popleft()
            
            for neigh, dirr in adj_List[nextt]:
                if neigh not in visited:
                    if neigh == destValue:
                        return path + dirr
                    queue.append((neigh, path + dirr))
                    visited.add(neigh)