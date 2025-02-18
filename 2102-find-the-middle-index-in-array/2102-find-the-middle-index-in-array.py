class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        presum = [nums[0]]
        presum_back = [0]*(len(nums)+1)

        for i in range(1,len(nums)):
            presum.append(presum[-1]+nums[i])
        for i in range(len(nums)-1, -1, -1):
            presum_back[i] = presum_back[i+1]+nums[i]
        for i in range(len(nums)):
            if presum[i] == presum_back[i]:
                return i
        return -1
        

        
        