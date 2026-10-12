class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        
        MOD = 10**9 + 7
        bits = [0]*32
        n = len(nums)
        for j in range(n):
            for i in range(32):
                if nums[j] & (1 << i):
                    bits[i] += 1
        result = 0
        for j in range(k):
            cur = 0
            for i in range(32):
                if bits[i]:
                    bits[i] -= 1
                    cur |= (1 << i)
            s = (cur*cur)%MOD
            result = (result+s)%MOD
        return result%MOD