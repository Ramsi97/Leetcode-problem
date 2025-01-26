class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if(not nums):
            return []
        result = []
        l = r = nums[0] 
        for i in range(1,len(nums)):
            if(nums[i-1]+1 == nums[i]):
                r = nums[i]
            else:
                if l!=r :
                    result.append(str(l)+"->"+str(r))
                else:
                    result.append(str(l))
                l = r = nums[i]
        if l!=r :
            result.append(str(l)+"->"+str(r))
        else:
            result.append(str(l))
        return result