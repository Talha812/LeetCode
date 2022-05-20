class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        lessEle = []
        greatEle = []
        equalEle = []
        
        for i in nums:
            if(i<pivot):
                lessEle.append(i)
            elif(i>pivot):
                greatEle.append(i)
            else:
                equalEle.append(i)
            
        nums = lessEle + equalEle + greatEle
        return nums