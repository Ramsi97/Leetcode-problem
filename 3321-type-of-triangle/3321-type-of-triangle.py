class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0]+nums[1] <= nums[2]:
            return "none"
        triangle = set(nums)
        if len(triangle) == 1:
            return "equilateral"
        elif len(triangle) == 2:
            return "isosceles"
        else:
            return "scalene"