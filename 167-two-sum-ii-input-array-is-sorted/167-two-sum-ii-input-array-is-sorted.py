class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i in range(len(numbers)):
            sec_num = target-numbers[i]
            if sec_num in dic:
                return [dic[sec_num]+1, i+1]
            dic[numbers[i]] = i
        
        