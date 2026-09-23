class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        n = len(nums)
        pre, suf = [0]*(n+1), [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i]+nums[i]
        for i in range(n-1, -1, -1):
            suf[i] = suf[i+1]+nums[i]
        
        index = {suf[i]: i for i in range(n+1)}
        
        result = n+1
        for i in range(n):
            cur = i + n - index.get(x- pre[i], -n-1)
            result = min(result, cur)
        return result if  result != n+1 else -1