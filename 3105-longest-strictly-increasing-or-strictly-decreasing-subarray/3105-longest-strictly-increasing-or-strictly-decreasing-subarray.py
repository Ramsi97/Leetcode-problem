class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        result , cur = 1, 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                cur = 1
            result = max(result, cur)
        
        cur = 1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                cur += 1
            else:
                cur = 1
            result = max(result, cur)
        return result