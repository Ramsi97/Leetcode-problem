class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        pair , remain = 0 , 0
        for value in count.values():
            pair += value//2
            remain += value%2
        return [pair, remain]

        