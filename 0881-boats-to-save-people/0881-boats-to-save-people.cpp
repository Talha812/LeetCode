class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());

        int l = 0, r = people.size()-1, trips = 0;

        while(l<=r){
            int capacity = limit - people[r];
            if(capacity >= people[l]) l++;
            r--;
            trips++;
        }
        return trips;
    }
};