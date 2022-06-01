class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for num_index in range(len(numbers)):
            sec_num = target-numbers[num_index]
            if(sec_num in dic):
                return [dic[sec_num]+1, num_index+1]
            else:
                dic[numbers[num_index]] = num_index