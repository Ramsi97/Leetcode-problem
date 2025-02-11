class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        set1 = set()

        for num in nums:
            set1.add(num)
            set1.add(int("".join(reversed(str(num)))))
        return len(set1)
        