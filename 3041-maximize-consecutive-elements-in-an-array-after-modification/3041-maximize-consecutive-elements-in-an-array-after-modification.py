class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        dp = [0]*1000006
            
        for num in nums:
            dp[num+1] = max(dp[num+1], dp[num] + 1)
            dp[num] = 1
            dp[num] = max(dp[num], dp[num-1] + 1)
        # print(dp)
        return max(dp)