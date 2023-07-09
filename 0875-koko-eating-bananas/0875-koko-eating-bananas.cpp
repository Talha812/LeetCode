// 875. Koko Eating Bananas

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, long h) {
        long maxVal = 0, res = 0;

        for(long pile:piles) maxVal = max(maxVal, pile);

        long l = 1, r = maxVal;

        while(l<=r){
            long mid = l + (r-l)/2; 
            long hoursNeeded = findHours(piles, mid);
            if(hoursNeeded > h)
                l = mid+1;
            else{
                res = mid;
                r = mid - 1;
            }
        }
        return res;
    }

    long findHours(vector<int>&piles, long hrs){
        long count = 0;

        for(int pile: piles){
            count += ceil(pile/double(hrs));
        }
        return count;
    }
};