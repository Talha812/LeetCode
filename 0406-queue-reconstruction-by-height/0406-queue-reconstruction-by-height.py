class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
                   
        for p in people:
            p[0] = -1*p[0]
        
        people.sort()
        
        for p in people:
            p[0] = -1*p[0]
        
        ans = []
        for p in people:
            ans.insert(p[1], p)   
            
        return ans