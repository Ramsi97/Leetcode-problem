class Solution {
public:
    bool canJump(vector<int>& nums) {
        
        int s = nums.size();
        int mxidx = 0;
        for(int i=0; i<s-1; i++)
        {
            if(i > mxidx)
            {
                return false;
            }
            mxidx = max(mxidx, i+nums[i]);
        }
        if(mxidx>= s-1)return true;
        return false;
    }
};