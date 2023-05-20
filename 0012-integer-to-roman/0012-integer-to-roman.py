class Solution:
    def intToRoman(self, num: int) -> str:
        
        dic = {1 : "I", 4 : "IV", 5: "V", 9 : "IX", 10: "X", 40 : "XL",  50 : "L", 90 : "XC", 100 : "C",                  400 : "CD", 500 : "D", 900 : "CM", 1000 : "M"}
        
        ans = ""
        if num >= 1000:
            req_alpha_cnt = num//1000
            ans += (req_alpha_cnt * dic[1000])
            num = num%1000
            
        if num >= 900:
            req_alpha_cnt = num//900
            ans += (req_alpha_cnt * dic[900])
            num = num%900
            
        if num >= 500:
            req_alpha_cnt = num//500
            ans += (req_alpha_cnt * dic[500])
            num = num%500
            
        if num >= 400:
            req_alpha_cnt = num//400
            ans += (req_alpha_cnt * dic[400])
            num = num%400
                
        if num >= 100:
            req_alpha_cnt = num//100
            ans += (req_alpha_cnt * dic[100])
            num = num%100
            
        if num >= 90:
            req_alpha_cnt = num//90
            ans += (req_alpha_cnt * dic[90])
            num = num%90
            
        if num >= 50:
            req_alpha_cnt = num//50
            ans += (req_alpha_cnt * dic[50])
            num = num%50
            
        if num >= 40:
            req_alpha_cnt = num//40
            ans += (req_alpha_cnt * dic[40])
            num = num%40
            
        if num >= 10:
            req_alpha_cnt = num//10
            ans += (req_alpha_cnt * dic[10])
            num = num%10
            
        if num >= 9:
            req_alpha_cnt = num//9
            ans += (req_alpha_cnt * dic[9])
            num = num%9
                
        if num >= 5:
            req_alpha_cnt = num//5
            ans += (req_alpha_cnt * dic[5])
            num = num%5
            
        if num >= 4:
            req_alpha_cnt = num//4
            ans += (req_alpha_cnt * dic[4])
            num = num%4
            
        if num >= 1:
            ans += (num * dic[1])
            num = 0
        
        return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            