class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit_achieve = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if(prices[i]>buy):
                profit_achieve += prices[i]-buy
                buy = prices[i]
            else:
                buy = prices[i]
                
        return profit_achieve