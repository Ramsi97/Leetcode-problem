class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        
        int n = nums.size();
        int result = INT_MAX;
        for(int i= 0; i<n; i++){
            int sum_ = 0;
            for(int j = i; j <n; j++){
                int s = j-i+1;
                sum_ += nums[j];
                if(s >= l && s <= r && sum_ > 0){
                    result = min(result, sum_);
                }
            }
        }
        if(result == INT_MAX){
            return -1;
        }
        return result;
    }
};