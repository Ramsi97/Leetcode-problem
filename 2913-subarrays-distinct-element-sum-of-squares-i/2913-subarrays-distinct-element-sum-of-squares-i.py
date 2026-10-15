class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        result = 0
        n = len(nums)
        for i in range(n):
            dis = set()
            for j in range(i, n):
                dis.add(nums[j])
                result += len(dis)**2
        return result
