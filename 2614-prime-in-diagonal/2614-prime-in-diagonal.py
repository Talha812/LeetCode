class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def isPrime(n):
            if n == 1:
                return False
            i = 2
            while i <= int(math.sqrt(n)):
                if n%i == 0:
                    return False
            
                i += 1
            return True
        
        dic = {}
        prime = 0
        
        for i in range(len(nums)):
            first = nums[i][i]
            sec = nums[i][len(nums)-i-1]
            flag1 = False
            if first in dic:
                if dic[first] == True:
                    prime = max(prime, first)
                    
            elif isPrime(first):
                flag1 = True
                prime = max(prime, first)
                
            dic[first] = flag1
                
            flag2 = False
            if sec in dic:
                if dic[sec] == True:
                    prime = max(prime, sec)
                    
            elif isPrime(sec):
                flag2 = True
                prime = max(prime, sec)
                
            dic[sec] = flag2
            
        return prime
    
#         def is_prime(n, memo={}):
#             if n < 2:
#                 return False
#             if n in memo:
#                 return memo[n]
            
#             for i in range(2, int(n**0.5) + 1):
#                 if n % i == 0:
#                     memo[n] = False
#                     return False
            
#             memo[n] = True
#             return True