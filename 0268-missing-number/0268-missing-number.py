class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        set1 = set(nums)
        for i in range(n+1):
            if not i in set1:
                return i
        

        