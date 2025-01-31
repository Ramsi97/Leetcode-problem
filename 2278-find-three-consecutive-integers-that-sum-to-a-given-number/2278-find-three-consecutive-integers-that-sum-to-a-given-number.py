class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3 != 0:
            return []
        n = num/3
        return [n-1, n, n+1]
        