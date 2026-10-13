class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        nums.sort(key = lambda x: abs(x), reverse = True)

        result = 0
        left = 0
        right = len(nums)-1

        while left <= right:
            result += nums[left]**2
            if left != right:
                result -= nums[right]**2
            left += 1
            right -= 1
        return result
