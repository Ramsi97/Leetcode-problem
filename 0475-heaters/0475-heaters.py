class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        left = 0
        right = max(max(houses), max(heaters))
        houses.sort()
        heaters.sort()
        def isposible(k):
            l = 0
            r = 0

            while l < len(houses) and r < len(heaters):

                if heaters[r] - k <= houses[l] <= heaters[r] + k:
                    l += 1
                else:
                    r += 1
            return l == len(houses)
        while left <= right:
            
            mid = left + (right - left)//2

            if isposible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        