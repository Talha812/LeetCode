class Solution:
    def minimumSum(self, num: int) -> int:
        
        
        num = str(num)
        
        sorted_arr = sorted(num)
        print(sorted_arr)
        return (int(sorted_arr[0] + sorted_arr[2])) + (int(sorted_arr[1] + sorted_arr[3])) 
        
        