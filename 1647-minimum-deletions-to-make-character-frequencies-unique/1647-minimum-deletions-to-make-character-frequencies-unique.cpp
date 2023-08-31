class Solution {
public:
    int minDeletions(string s) {
        unordered_map<char, int> map;

        int maxFreq = 0;

        for(char ch: s){
            map[ch]++;
            maxFreq = max(maxFreq, map[ch]);
        }
        vector<int>freqMap(maxFreq+1, 0);

        for(auto it:map){
            freqMap[it.second]++;
        }
        int count = 0;
        for(int i=freqMap.size()-1; i>0; i--){
            while(i>0 && freqMap[i]>1){
                count += (freqMap[i] - 1);
                freqMap[i-1] += (freqMap[i] - 1);
                i--;
            }
        }
        return count;
    }
};