class Solution:
    def largestInteger(self, num: int) -> int:
        
        digits = [int(ch) for ch in str(num)]
        
        odd = []
        even = []
        
        for d in digits:
            if d%2 == 0:
                even.append(d)
            else:
                odd.append(d)
        
        odd.sort(reverse=True)
        even.sort(reverse=True)
        
        ans = ""
        e_ind = 0
        o_ind = 0
        for d in digits:
            if d%2 == 0:
                ans += str(even[e_ind])
                e_ind += 1
            else:
                ans += str(odd[o_ind])
                o_ind += 1
        
        return int(ans)