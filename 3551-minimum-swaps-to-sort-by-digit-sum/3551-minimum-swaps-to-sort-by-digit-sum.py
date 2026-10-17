class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        def sum(num):
            result = 0
            while num:
                result += num%10
                num //= 10
            return result
        sorted_nums = sorted(nums, key = lambda x: (sum(x), x))
        target_index = {num: i for i, num in enumerate(sorted_nums)}

        n = len(nums)
        visited = [False]*n
        cycle = 0
        for i in range(n):
            if visited[i]:
                continue
            cycle += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = target_index[nums[j]]
        return n - cycle
                
        