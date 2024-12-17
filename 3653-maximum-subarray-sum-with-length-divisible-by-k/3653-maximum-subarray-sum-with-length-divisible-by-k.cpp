class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        long size = nums.size();
        vector<long long> prefix_sum;
        prefix_sum.push_back(0);
        long long sum = 0;
        for(int i=0; i<size; i++)
        {
            sum+=nums[i];
            prefix_sum.push_back(sum);
        }

        long long max_sum = LLONG_MIN;
        vector<long long> minprefixsum (k, LLONG_MAX);

        for(int i = 0; i <= size; i++)
        {
            long remainder = i%k;

            if(i >= k)
            {
                max_sum = max(max_sum, prefix_sum[i] - minprefixsum[remainder]);
            }

            minprefixsum[remainder] = min(minprefixsum[remainder], prefix_sum[i]);
            
        }

        return max_sum == LLONG_MIN ? 0: max_sum;
    }
};