class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
               
        five = []
        ten = []
        twenty = []
        for money in bills:
            
            if money>5:
                if len(five) == 0:
                    return False
                
                if money == 10:
                    five.pop()
                    ten.append(10)
                    
                elif money == 20:
                    if 10 not in ten:
                        if len(five)<3:
                            return False
                        five.pop()
                        five.pop()
                        five.pop()
                        twenty.append(20)
                        
                    else:
                        five.pop()
                        ten.pop()
                        twenty.append(20)
                        
            else:
                five.append(5)
                
        return True