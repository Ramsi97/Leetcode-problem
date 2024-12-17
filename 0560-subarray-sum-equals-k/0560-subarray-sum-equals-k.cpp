class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int size = nums.size();
        unordered_map<int, int> prefix_sum{{0,1}};
        int res = 0;
        int cursum = 0;
        for(int i=0; i<size; i++)
        {
            cursum+=nums[i];
            if( prefix_sum.find(cursum-k) != prefix_sum.end())
            {
                res+=prefix_sum[cursum-k];
            }

            prefix_sum[cursum]++;
        }

        return res;
    }
};