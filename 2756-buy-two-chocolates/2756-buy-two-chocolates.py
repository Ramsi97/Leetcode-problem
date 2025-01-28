class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        if(prices[0]+prices[1] <= money):
            result = money-(prices[0]+prices[1])
        else:
            result = money
        return result
        