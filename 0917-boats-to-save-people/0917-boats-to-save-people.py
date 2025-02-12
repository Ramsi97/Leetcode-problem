class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        n = len(p)
        l = 0
        r = n-1
        result = 0
        p.sort()
        while l<r:
            if p[l]+p[r] > limit:
                result += 1
                r -= 1
            else:
                result += 1
                r -= 1
                l += 1
        if l == r:
            result += 1
        return result
        