class Solution(object):
    def findIndices(self, nums, d, v):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n):
            for j in range(i+d,n):
                if abs(nums[i] - nums[j]) >= v:
                    return [i,j]
        

        return [-1, -1]
        