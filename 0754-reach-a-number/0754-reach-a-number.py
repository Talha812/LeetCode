class Solution:
    def reachNumber(self, target: int) -> int:
        
#         q = collections.deque([(0,0)])
                
#         while q:
#             for i in range(len(q)):
#                 node, step = q.popleft()
                
#                 if node == target:
#                     return step-1
                
#                 q.append((node-step, step+1))
#                 q.append((node+step, step+1))

                
                
                
        target = abs(target)

        ans = 0

        pos = 0

        # keep moving to the target until we have passed the target

        while pos < target:

            ans += 1

            pos += ans

        # find the first pos that has even delta 
        while (pos - target) % 2:

            ans += 1

            pos += ans

        return ans