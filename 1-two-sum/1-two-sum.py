class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            sec_num = target - nums[i]
            if(dic.get(sec_num) != None):
                return [dic[sec_num],i]
            dic[nums[i]] = i