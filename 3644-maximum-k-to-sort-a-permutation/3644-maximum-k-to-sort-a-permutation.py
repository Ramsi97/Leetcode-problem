class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        result = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if result == -1:
                    result = nums[i]
                else:
                    result &= nums[i]
        return (result if result != -1 else 0)