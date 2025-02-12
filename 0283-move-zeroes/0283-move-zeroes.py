class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        placeholder = 0

        for seeker in range(len(nums)):
            if not nums[placeholder] and nums[seeker] :
                nums[placeholder], nums[seeker] =nums[seeker], nums[placeholder] 
            if nums[placeholder]:
                placeholder+=1

        