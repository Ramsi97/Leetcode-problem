class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        nums.sort()
        result = []

        for i in range(0,len(nums),2):
            f = nums[i]
            s = nums[i+1]
            result.append(s)
            result.append(f)
        return result
        