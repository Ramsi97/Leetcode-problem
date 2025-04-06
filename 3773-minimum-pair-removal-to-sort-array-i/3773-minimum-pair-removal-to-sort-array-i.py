class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        result = 0

        while sorted(nums) != nums:
            index = 0
            sum_ = nums[0]+nums[1]
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] < sum_:
                    index = i
                    sum_ = nums[i]+nums[i+1]
            nums[index] = sum_
            nums.pop(index+1)
            result += 1
            print(nums)
        return result