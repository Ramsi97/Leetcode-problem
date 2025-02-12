class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        sum_digit = defaultdict(list)
        def sum_d(num):
            s = 0
            while num:
                s+=(num%10)
                num//=10
            return s
        for i in nums:
            sum_ = sum_d(i)
            sum_digit[sum_].append(i)
        result = -1

        for key, value in sum_digit.items():
            if len(value) > 1:
                value.sort()
                result = max(result, value[-1]+value[-2])
        return result


        