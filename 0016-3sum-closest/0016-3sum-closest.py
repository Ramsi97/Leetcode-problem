class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ans = float("inf")
        n = len(nums)
        nums.sort()
        sum_ = 0
        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                sum_ = nums[i]+nums[left] +nums[right]
                if abs(sum_-target) < abs(ans - target):
                    ans = sum_
                if sum_ > target:
                    right -= 1
                else:
                    left += 1
            
        return ans
                
                





