class Solution {
public:
    int findTheWinner(int n, int k) {
        vector<int> players(n, 1);
        int eleminated = 0;

        int i = 0;

        while(true){
            int cnt = k-1;
            while(cnt>0 || players[i]<0){
                if(players[i] < 0) {
                    i++;
                    i = i%n;
                    continue;
                }
                cnt--;
                i++;
                i = i%n;
            }
            if(eleminated == n-1)   return i+1;
            players[i] = -1;
            eleminated++;
            i++;
            i = i%n;
        }
    }
};