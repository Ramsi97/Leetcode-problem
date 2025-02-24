class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        result = 0
        for i in range(2, n):
            if nums[i-2]+nums[i-1] > nums[i]:
                result = nums[i-2]+nums[i-1]+nums[i]
        return result
        