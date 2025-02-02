class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        first = max(nums)
        return (first + first + k -1) *k /2
        