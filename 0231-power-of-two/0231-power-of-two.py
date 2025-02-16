class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return int(math.log2(n)) == math.log2(n)
        