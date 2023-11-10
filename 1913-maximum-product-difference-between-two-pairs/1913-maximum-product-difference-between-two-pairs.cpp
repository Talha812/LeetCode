class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        priority_queue<int> maxHeap;
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for(int num:nums){
            if(maxHeap.size() < 2)     maxHeap.push(num);
            else{
                if(maxHeap.top() > num){
                    maxHeap.pop();
                    maxHeap.push(num);
                }
            }
            if(minHeap.size() < 2)  minHeap.push(num);
            else{
                if(minHeap.top() < num){
                    minHeap.pop();
                    minHeap.push(num);
                }
            }
        }
        int maxP = minHeap.top();
        minHeap.pop();
        maxP *=minHeap.top();

        int minP = maxHeap.top();
        maxHeap.pop();
        minP *= maxHeap.top();

        return maxP-minP;
    }
};