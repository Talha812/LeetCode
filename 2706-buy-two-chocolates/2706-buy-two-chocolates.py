class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        first_min = float("inf")
        sec_min = float("inf")
        
        for p in prices:
            if p <= first_min:
                    sec_min = first_min
                    first_min = p
            elif p <= sec_min and p >= first_min:
                sec_min = p
                
        total_price = first_min + sec_min
        
        if total_price <= money:
            return money - total_price
        
        return money