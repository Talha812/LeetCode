class TopVotedCandidate(object):

    def __init__(self, persons: List[int], times: List[int]):
        
        count = {}
        mostVotePersons = [0] * len(persons) # mostVotePersons[i] is the most vote person at times[i]
        largestVoteInd = -1 # keep largest vote person index
        for i in range(len(persons)):
            if persons[i] not in count:
                count[persons[i]] = 1
            else:
                count[persons[i]] += 1
                
            if largestVoteInd == -1 or count[persons[i]] >= count[largestVoteInd]:
                largestVoteInd = persons[i]
                
            mostVotePersons[i] = largestVoteInd
        
        self.times = times
        self.mostVotePersons = mostVotePersons
        print(count, mostVotePersons, largestVoteInd)

    def q(self, t: int) -> int:
        idx = self.findExactRight(self.times, t) - 1 # binary search on times to find the most recent time before t
        return self.mostVotePersons[idx]
    
    def findExactRight(self, nums, target):
        """
        Returns rightmost insertion point that target should be inserted in the sorted array
        """
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
            
        return left

    

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)