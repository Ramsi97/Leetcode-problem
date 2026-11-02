class Solution:
    def minMoves(self, nums: list[int]) -> int:

        nums.sort()
        cnt = 1
        result = 0
        n = len(nums)
        for i in range(n-2, -1, -1):
            result += cnt*(nums[i+1] - nums[i])
            cnt += 1
        return result
        
        