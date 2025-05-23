class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        total = 0
        for i, v in enumerate(nums):
            total += v
            r = total%k
            if not r in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False