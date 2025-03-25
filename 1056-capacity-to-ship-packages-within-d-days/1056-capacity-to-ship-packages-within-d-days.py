class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def ispossible(capacity):
            sum_ = 0
            day = 0
            for i in range(n):
                sum_ += weights[i]
                if sum_ > capacity:
                    day += 1
                    sum_ = weights[i]
            day += 1
            return days >= day
        
        low = max(weights)
        high = sum(weights)

        while low <= high:

            capacity = (high+low)//2

            if ispossible(capacity):
                high = capacity - 1
            else:
                low = capacity + 1
        return low