class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
#         pairs.sort()
#         def calculate(pairs, memo, ind):
#             global ans
#             if len(pairs) == 1:
#                 return 1
            
#             if memo[ind] != -1:
#                 return memo[ind]
            
#             memo[ind] = -1
            
#             for i in range(ind, len(pairs)):
#                 memo[ind] = max(calculate(pairs[i+1:], memo, i), memo[ind])
                
                
#             return memo[ind]
        
    
#         memo = [-1]*len(pairs)
        
#         calculate(pairs, memo, 0)
        
#         return max(memo)

        # pairs=sorted(pairs, key=lambda x: x[1])
        # ans=[]
        # ans.append(pairs[0])
        # i=1
        # while i <len(pairs):
        #     elem=pairs[i]
        #     top=ans[-1]
        #     # append
        #     if elem[0]>top[1]:
        #         ans.append(elem)
        #     i+=1
        # return len(ans)

        ans, chainEnd = 0, -inf
        pairs.sort(key = lambda x: x[1])

        for l, r in pairs:
            if l > chainEnd:
                ans+= 1
                chainEnd = r

        return  ans
        