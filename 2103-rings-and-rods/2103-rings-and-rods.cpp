class Solution {
public:
    int countPoints(string rings) {
        int count = 0;
        unordered_map<int, unordered_set<char>> s;
        for(int i = 1; i<rings.size(); i+=2){
            s[rings[i] - '0'].insert(rings[i-1]);
        }
        for(int i= 0; i<10; i++){
            if(s.find(i) != s.end()){
                if(s[i].size() == 3)    count++;
            }
        }
        return count;
    }
};