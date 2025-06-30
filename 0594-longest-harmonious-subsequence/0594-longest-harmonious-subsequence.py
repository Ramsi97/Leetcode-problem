class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        left = 0
        result = 0 

        for right in range(n):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[left] != nums[right]:
                result = max(result, right - left + 1)
        return result