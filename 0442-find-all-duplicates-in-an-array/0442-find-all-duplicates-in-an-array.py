class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []
        for key, value in count.items():
            if value == 2:
                result.append(key)
        return result
        