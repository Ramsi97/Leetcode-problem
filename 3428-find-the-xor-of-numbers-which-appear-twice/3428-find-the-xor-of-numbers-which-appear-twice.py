class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        result = 0
        dup = Counter(nums)

        for key, value in dup.items():
            if value == 2:
                result ^= key
        return result