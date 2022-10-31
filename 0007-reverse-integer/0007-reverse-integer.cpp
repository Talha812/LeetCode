// 7. Reverse Integer

class Solution {
public:
    int reverse(int n) {
        int ans = 0;
        
        while(n){
            if(ans > INT_MAX/10 || ans < INT_MIN/10)  
                return 0;
            else{
                ans = ans*10 + (n%10);
                n /= 10;
            }
        }
        return ans;
    }
};