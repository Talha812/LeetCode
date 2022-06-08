class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        ans = []
        for i in range(len(ops)):
            if(ops[i] == "D"):
                ans.append(ans[-1]*2)
            elif(ops[i] == "C"):
                ans.pop()
            elif(ops[i] == "+"):
                ans.append(ans[-1]+ans[-2])
            else:
                ans.append(int(ops[i]))
        
        return sum(ans)
            