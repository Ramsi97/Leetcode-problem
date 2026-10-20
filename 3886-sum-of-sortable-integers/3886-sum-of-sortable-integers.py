class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        N = len(nums)

        def globaly_sortable(k):
            min_ = float("inf")
            max_ = float("-inf")
            prev = 0

            for i in range(k, N + 1, k):
                s, m, M = cyclically_sortable(prev, i)
                if s and m >= max_:
                    min_ = m
                    max_ = M
                else:
                    return False
                prev = i

            return True

        def cyclically_sortable(left, right):
            sortable = True
            min_ = nums[left]
            max_ = nums[left]

            breakpoint = 0

            for i in range(left + 1, right):
                if nums[i] < nums[i - 1]:
                    breakpoint += 1

                if breakpoint > 1:
                    return False, 0, 0

                min_ = min(min_, nums[i])
                max_ = max(max_, nums[i])

            if right - left > 1 and nums[left] < nums[right - 1]:
                breakpoint += 1

            if breakpoint > 1:
                return False, 0, 0

            return sortable, min_, max_

        result = 0

        for i in range(1, N + 1):
            if N % i == 0:
                if globaly_sortable(i):
                    result += i

        return result