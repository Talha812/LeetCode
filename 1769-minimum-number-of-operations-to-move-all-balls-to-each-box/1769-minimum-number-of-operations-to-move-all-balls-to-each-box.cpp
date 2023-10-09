class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();

        vector<int> leftSideOps(n, 0), rightSideOps(n, 0);

        int cnt = 0;
        cnt = boxes[0] == '1'?cnt+1:cnt;

        for(int i=1; i<n; i++){
            leftSideOps[i] = leftSideOps[i-1] + cnt;
            cnt = boxes[i] == '1'?cnt+1:cnt;
        }
        cnt = 0;
        cnt = boxes[n-1] == '1'?cnt+1:cnt;
        for(int i=n-2; i>=0; i--){
            rightSideOps[i] = rightSideOps[i+1] + cnt;
            cnt = boxes[i] == '1'?cnt+1:cnt;
        }

        vector<int> result(n, 0);
        for(int i=0; i<n; i++){
            result[i] = leftSideOps[i] + rightSideOps[i];
        }
        return result;
    }
};