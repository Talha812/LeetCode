class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        # occurrence = Counter(str(n))
        # print(occurrence)
        # for i in range(30):
        #     if (occurrence == Counter(str(2**i))):
        #         return True
        # return False
        
        def getDigitCount(n):
            
            dic = {}
            
            while n > 0:
                rem = n%10
                if rem in dic:
                    dic[rem] += 1
                else:
                    dic[rem] = 1
                
                n = n//10
                           
            # n = str(n)
            # for d in n:
            #     if d in dic:
            #         dic[d] += 1
            #     else:
            #         dic[d] = 1
                
            return dic
        
        
        org_no_digit_count = getDigitCount(n)
        
        for i in range(30):
            if org_no_digit_count == getDigitCount(pow(2,i)):
                return True
            else:
                continue
        
        return False