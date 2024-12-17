class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int res =nums.size()+1;
        int l=0, r=0;

        int sum = 0;

        while(r<nums.size())
        {
            sum+= nums[r];
            while(sum >= target)
            {
                sum-=nums[l];
                res = min(res, r-l+1);
                l++;
            }
            
            r++;
        }
        
        return res == nums.size()+1 ? 0 : res;
    }
};