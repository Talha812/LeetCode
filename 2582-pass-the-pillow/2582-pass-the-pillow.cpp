class Solution {
public:
    int passThePillow(int n, int time) {
       int t2 = time %( 2*(n-1));
       if(t2 > (n-1)){
           int t3 = t2 - (n-1);
           return n-t3;
       } 
       return t2 + 1;
    }
};