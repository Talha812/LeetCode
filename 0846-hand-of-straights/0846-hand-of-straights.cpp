class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size()%groupSize != 0)  return false;
        int n = hand.size();
        map<int, int> mp;

        for(int card : hand){
            mp[card]++;
        } 

        for(auto &it:mp){
            if(it.second == 0)  continue;
            while(it.second){
                for(int j = 0; j < groupSize; j++){
                    int currCard = it.first + j;

                    if(mp[currCard] == 0)   return false;

                    mp[currCard]--;
                    n--;
                }
            }
        }
         return n == 0;
    }
};