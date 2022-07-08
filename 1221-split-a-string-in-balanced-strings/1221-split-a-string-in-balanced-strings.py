class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_L=0
        count_R=0
        amount=0
        for i in s:
            if i=='R':
                count_R+=1
            if i=="L":
                count_L+=1
            if count_L==count_R:
                amount+=1
        return amount