class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        result = 0
        for i in range(n):
            gcd_, lcm_, prod = 0, 1, 1
            for j in range(i, n):
                gcd_ = gcd(gcd_, nums[j])
                lcm_ = lcm(lcm_, nums[j])
                prod *= nums[j]

                if lcm_*gcd_== prod:
                    result = max(result, j - i +1)
        return result

