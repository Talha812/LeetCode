class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        e1_s, e1_e = event1
        e2_s, e2_e = event2
               
        
        if e2_s <= e1_s <= e2_e or e2_s <= e1_e <= e2_e or e1_s <= e2_s <= e1_e or e1_s <= e2_e <= e1_e:
            return True
        
        return False