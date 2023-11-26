class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    
        ans = []
        for i in range(len(l)):
            subarr = nums[l[i] : r[i]+1]
            
            mini = min(subarr)
            maxi = max(subarr)
            
            if mini == maxi:
                ans.append(True)
                continue

            if (maxi-mini)%(len(subarr)-1) != 0:
                ans.append(False)
            else:
                d = (maxi-mini)//(len(subarr)-1)
                flag = False
                arr_set = set(subarr)
                curr = mini + d
                while curr < maxi:
                    if curr not in arr_set:
                        ans.append(False)
                        flag = True
                        break
                        
                    curr += d
                    
                if not flag:
                    ans.append(True)
        
        return ans
        