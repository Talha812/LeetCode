class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        queue = collections.deque([(0,0)])
        ans = []
        
        while queue:
            size = len(queue)
            for k in range(size):
                i, j = queue.popleft()
                ans.append(abs(nums[i][j]))

                if i+1 < len(nums) and j < len(nums[i+1]) and nums[i+1][j] >= 0:
                    queue.append((i+1, j))
                    nums[i+1][j] = -1*nums[i+1][j]

                if j+1 < len(nums[i]) and nums[i][j+1] >= 0:
                    queue.append((i, j+1))
                    nums[i][j+1] = -1*nums[i][j+1]
        return ans