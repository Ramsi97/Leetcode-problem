from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        start = nums.index(0)

        inc = nums[(start - 1) % n] == n - 1

        if inc:
            for i in range(n):
                if nums[(start + i) % n] != i:
                    return -1
            
            return min(start, n - start+2)

        else:
            for i in range(n):
                if nums[(start - i) % n] != i:
                    return -1
            return min((start + 1) % n + 1, n - start)