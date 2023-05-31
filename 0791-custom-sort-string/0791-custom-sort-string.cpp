class Solution {
public:
    string customSortString(string order, string s) {
        
        unordered_map<char, int> map;
        for(int i =0; i<order.size(); i++){
            map[order[i]] = i;
        }
        
        int val = order.size();
        for(int i=0; i<s.size(); i++){
            if(map.count(s[i]) == 0){
                map[s[i]] = val++;
            }
        }
        sort(s.begin(), s.end(), [&map](char c1, char c2) {
            return map[c1] < map[c2];
        });
//         sort(s.begin(), s.end(), [](char &c1, char &c2){
//             return map[c1] < map[c2];
            
//         });
        
        return s;
        
    }
};