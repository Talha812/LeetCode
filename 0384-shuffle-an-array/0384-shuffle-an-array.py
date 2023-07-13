class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.record = list(nums)  

    def reset(self) -> List[int]:
        self.array = self.record
        self.record = list(self.record)
        return self.array

    def shuffle(self) -> List[int]:
        copy = self.array[:]
        
        for place_ind in range(len(self.array)):
            rem_ele_ind = random.randint(0, len(copy)-1)
            self.array[place_ind] = copy.pop(rem_ele_ind)

        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()