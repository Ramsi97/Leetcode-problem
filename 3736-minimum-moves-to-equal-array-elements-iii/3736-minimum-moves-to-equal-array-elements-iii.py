class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        max_ = max(nums)
        result = 0
        for num in nums:
            result += max_ - num
        return result