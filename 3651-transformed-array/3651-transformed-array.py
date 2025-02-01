class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(nums[(i+nums[i])%n])
            elif nums[i] == 0:
                result.append(nums[i])
            else:
                result.append(nums[ (i+nums[i]) % n ])
        return result
 
 